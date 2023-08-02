from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('about/', views.about, name='about'),
    path('services/kids/', views.services, name='services'),
    path('contacts/', views.contacts, name='contacts'),
]