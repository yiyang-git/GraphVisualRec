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


"""
This file is a view controller for multiple pages as a module.
Here you can override the page view layout.
Refer to tables/urls.py file for more pages.
"""


class TableView(TemplateView):
    # Predefined function
    def get_context_data(self, **kwargs):
        # A function to init the global layout. It is defined in web_project/__init__.py file
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))

        return context
