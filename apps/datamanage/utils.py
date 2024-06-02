# utils.py
import os
import pandas as pd
import re
import pytz
from django.utils import timezone
from django.apps import apps
from django.core.exceptions import ImproperlyConfigured
from django.conf import settings

def clean_column_name(name):
    # 删除空格
    name = name.replace(' ', '')
    # 用下划线替换其他非字母数字字符，并确保字段名不以数字开头
    cleaned_name = re.sub(r'\W|^(?=\d)', '_', name)
    # 确保字段名不以下划线结尾
    if cleaned_name.endswith('_'):
        cleaned_name = cleaned_name[:-1]
    # 确保字段名不以下划线开头
    if cleaned_name.startswith('_'):
        cleaned_name = cleaned_name.lstrip('_')
    # 确保字段名不包含双下划线
    while '__' in cleaned_name:
        cleaned_name = cleaned_name.replace('__', '_')
    # 确保字段名不与 Python 保留字冲突
    if cleaned_name in {'class', 'def', 'return', 'if', 'else', 'elif', 'try', 'except', 'finally', 'for', 'while', 'import', 'from', 'as', 'pass', 'break', 'continue', 'with', 'lambda', 'nonlocal', 'global', 'assert', 'yield', 'raise', 'True', 'False', 'None', 'and', 'or', 'not', 'is', 'in', 'del', 'print', 'exec'}:
        cleaned_name = cleaned_name + '_field'
    return cleaned_name
def file_exists_in_uploads(file_name):
    upload_dir = settings.UPLOAD_ROOT
    return os.path.exists(os.path.join(upload_dir, file_name))

def model_exists(model_name):
    try:
        print(model_name)
        models = apps.get_models()
        model_names = [model.__name__ for model in models]
        print(model_names)
        apps.get_model('DataManage', model_name)
        return True
    except LookupError:
        return False


def generate_model_code(file_path):
    model_name = clean_column_name(os.path.splitext(os.path.basename(file_path))[0]+'_uploaded')

    df = pd.read_excel(file_path)
    fields = []
    for column in df.columns:
        if pd.api.types.is_datetime64_any_dtype(df[column]):
            df[column] = df[column].apply(lambda x: timezone.make_aware(x) if pd.notnull(x) else x)
    for column in df.columns:
        clean_column = clean_column_name(column)
        field_type = get_field_type(df[column], column)
        if field_type == "CharField":
            fields.append(f"{clean_column} = models.{field_type}(max_length=255, null=True)")

        else:
            fields.append(f"{clean_column} = models.{field_type}(null=True)")

    model_code = """
class {model_name}(models.Model):
    {fields}
""".format(model_name=model_name, fields='\n    '.join(fields))

    return model_code, model_name,'DataManage.models'


def get_field_type(series, column_name):
    if 'Code' in column_name:
        return "CharField"
    elif pd.api.types.is_integer_dtype(series):
        return "IntegerField"
    elif pd.api.types.is_float_dtype(series):
        return "FloatField"
    elif pd.api.types.is_bool_dtype(series):
        return "BooleanField"
    elif pd.api.types.is_datetime64_any_dtype(series):
        return "DateTimeField"
    elif pd.api.types.is_datetime64_ns_dtype(series):
        return "DateTimeField"
    elif pd.api.types.is_timedelta64_dtype(series):
        return "DurationField"
    elif pd.api.types.is_string_dtype(series):
        max_length = series.str.len().max()
        if max_length is not None and max_length >= 255:
            return "TextField"
        elif max_length is not None:
            return f"CharField"
        else:
            return "TextField"
    else:
        return "CharField"
