from django.urls import path
from .views import RecommendationData, QlikDashboard



urlpatterns = [
    path(
        "dashboard/recommendationdata/",
        RecommendationData.as_view(template_name="dashboard_analytics.html"),
        name="index",
    ),
    path(
        "dashboard/qlikdashboard/",
        QlikDashboard.as_view(template_name="qlikdashboard.html"),
        name="QlikDashboard",
    ),
]
