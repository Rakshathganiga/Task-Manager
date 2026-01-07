from django.urls import path
from .views import tasks_collection, task_item

urlpatterns = [
    path("tasks", tasks_collection),
    path("tasks/<str:task_id>", task_item),
    
]
