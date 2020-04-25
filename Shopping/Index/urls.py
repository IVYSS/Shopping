from django.urls import path
from . import views
from .views import (
    add_to_cart,
    remove_from_cart,
    remove_single_product_from_cart
)
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import include
urlpatterns = [
    path('', views.show, name='show'),
    path('login/', views.my_login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.my_logout, name='logout'),
    path('detail/<product_id>/', views.detail, name='product_detail'),
    path('add-to-cart/<product_id>/',add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<product_id>/',remove_from_cart, name='remove-from-cart'),
    path('remove-single-product-from-cart/<product_id>/',remove_single_product_from_cart, name='remove-single-productfrom-cart'),
    path('order-summary/',views.OrderSummary, name='order-summary'),    
    path('checkout/',views.Checkout, name='checkout'),    
    path('order-summary',views.OrderSummary, name='order-summary'),
    path('make-product/',views.make_product, name='make_product'),
    path('payment/<payment_option>/',views.PaymentView, name='payment'),
    path('type/<int:id>/', views.show_type, name='show_type'),
    path('api/comment/',views.comment, name='comment')
]

urlpatterns += staticfiles_urlpatterns()