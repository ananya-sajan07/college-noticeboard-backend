from django.urls import path
from .views import get_notices
from . import views


urlpatterns = [
    path('notices/', get_notices, name='get_notices'),
    path('notices/create/', views.create_notice, name='create_notice'),

]
