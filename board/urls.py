from django.urls import path
from .views import get_notices, create_notice, feedback_list_create

urlpatterns = [
    path('notices/', get_notices, name='get_notices'),
    path('notices/create/', create_notice, name='create_notice'),
    path('feedback/', feedback_list_create, name='feedback_list_create'),
]
