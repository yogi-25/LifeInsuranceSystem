from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.hi, name='hi'),
    path('hi/', views.hi, name='hi'),
]

