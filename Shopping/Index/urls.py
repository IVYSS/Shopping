from django.urls import path
from . import views

urlpatterns = [
    path('', views.show, name='show'),
    path('login/', views.my_login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.my_logout, name='logout'),
    path('detail/<int:product_id>/', views.detail, name='product_detail'),
]
