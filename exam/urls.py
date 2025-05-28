from django.urls import path
from . import views

urlpatterns = [
    path('', views.exham_list, name='exham_list'),
]
