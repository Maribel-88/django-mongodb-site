# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('api/register/', views.register_user_api, name='register_api'),
]
