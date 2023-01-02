from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views


urlpatterns = [
    path('status/', views.api_status),
    path('tasks/', views.get_tasks),
    path('tasks/<int:id>', views.get_task_by_id),
    path('tags/', views.get_tags),
    path('tags/<int:id>/', views.get_tags_by_id),
    path('tags/<int:id>/tasks/', views.get_tasks_by_tag),
]

# adding .json to end of api slug formats the data to json
# works with views by passing format=None as an arg
urlpatterns = format_suffix_patterns(urlpatterns)
