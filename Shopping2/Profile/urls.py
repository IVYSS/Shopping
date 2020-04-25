from django.urls import path
from . import views

urlpatterns = [
    path('', views.showprofile, name='showprofile'),
]
