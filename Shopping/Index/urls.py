from django.urls import path
from . import views
from .views import (
    add_to_cart
)
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('', views.show, name='show'),
    path('login/', views.my_login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.my_logout, name='logout'),
    path('detail/<product_id>/', views.detail, name='product_detail'),
    path('add-to-cart/<product_id>/',add_to_cart, name='add-to-cart')
]

urlpatterns += staticfiles_urlpatterns()