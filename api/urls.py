# Endpoints
from django.urls import path

from . import views


urlpatterns = [
    path('status/', views.api_status),
    path('tasks/', views.get_tasks),
    path('labels/', views.get_labels),
]
