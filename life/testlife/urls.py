from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.hello_world, name='hello_world'),
    path('hi/', views.hi, name='hi'),
]

