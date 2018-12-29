from django.urls import path
from . import views

urlpatterns = [
    path('', views.indexThanks, name='indexThanks')
]