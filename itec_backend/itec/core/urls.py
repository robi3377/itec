from django.urls import path
from django import views
from . import views

urlpatterns = [

    path('text', views.index, name='index'),
    path('', views.apiPost )

]