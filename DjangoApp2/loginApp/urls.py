from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('loginUser/', views.loginUser, name='loginUser'),
    path('logoutUser/', views.logoutUser, name='logoutUser'),
]