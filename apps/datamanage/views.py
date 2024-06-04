from django.views.generic import TemplateView
from web_project import TemplateLayout
# from ConstructionKG.MultimodalFeatureExtra.models.Sound_PCA_Kmeans import GearboxAudioProcessor
import os
from .models import FileRecord
import time
import datetime
from django.db import models
import openpyxl
import subprocess
from django.apps import apps
import pandas as pd
from .forms import ExcelUploadForm
from .utils import generate_model_code, model_exists, clean_column_name, file_exists_in_uploads
from pathlib import Path
from django.conf import settings
from django.http import JsonResponse
from django.urls import reverse
from django.utils.dateparse import parse_datetime
from django.utils.timezone import make_aware
import threading
from django.utils import timezone
from django.shortcuts import render, redirect
from django.core.paginator import Paginator

"""
This file is a view controller for multiple pages as a module.
Here you can override the page view layout.
Refer to tables/urls.py file for more pages.
"""


# class TableView(TemplateView):
#     # Predefined function
#     def get_context_data(self, **kwargs):
#         # A function to init the global layout. It is defined in web_project/__init__.py file
#         context = TemplateLayout.init(self, super().get_context_data(**kwargs))
#         file_name = self.request.GET()
#
#         return context


class DataTableView(TemplateView):

    def get_context_data(self, **kwargs):
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        model_info = get_all_models_info()
        context['model_info'] = model_info
        return context

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        file_name = self.request.POST.get('dataselection', 'FileRecord')
        file_name_chinese = '数据特征文本'
        if file_name:
            try:
                # 动态获取模型类
                model = apps.get_model('datamanage', file_name)
                file_record = FileRecord.objects.filter(file_name=file_name).first()
                if file_name != 'FileRecord':
                    file_name_chinese = file_record.file_name_chinese
            except LookupError:
                model = FileRecord
        else:
            model = FileRecord

        file_records = model.objects.all()
        file_records = file_records.order_by('id')

        paginator = Paginator(file_records, 20)  # 每页显示20条数据
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        # 获取列名
        column_names = [field.verbose_name for field in model._meta.fields if field.name != 'id']

        # 获取字段数据
        records = []
        for record in page_obj:
            record_data = {field.verbose_name: getattr(record, field.name) for field in model._meta.fields if
                           field.name != 'id'}
            records.append(record_data)

        context.update({
            'page_obj': page_obj,
            'column_names': column_names,
            'records': records,
            'file_name': file_name,
            'file_name_chinese': file_name_chinese,
        })

        return self.render_to_response(context)

def get_all_models_info():
    model_info = []
    for record in FileRecord.objects.all():
        model_info.append({
            'file_name': record.file_name,
            'file_name_chinese': record.file_name_chinese
        })
    return model_info
