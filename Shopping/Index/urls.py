from django.urls import path
from . import views

urlpatterns = [
    path('', views.show, name='show'),
    path('login/', views.login, name='login'),
    path('signin/', views.signin, name='signin'),
]
