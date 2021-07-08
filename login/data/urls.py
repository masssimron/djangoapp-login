from django.urls import include, path
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.index, name='index'),
    
]