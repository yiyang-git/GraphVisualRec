from django.urls import path
from .views import DataTableView



urlpatterns = [
    path(
        "datamanage/datatable/",
        DataTableView.as_view(template_name="data_table.html"),
        name="datamanage_datatable",
    )
]
