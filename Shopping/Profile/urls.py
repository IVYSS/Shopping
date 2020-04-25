from django.urls import path
from . import views

urlpatterns = [
    path('', views.showprofile, name='showprofile'),
    path('profile_change/', views.profile_change, name='profile_change'),
]
