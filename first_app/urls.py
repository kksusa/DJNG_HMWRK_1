from django.urls import path
from . import views

urlpatterns = [
    path('', views.general, name='general_info'),
    path('about/', views.about, name='about_me'),
]