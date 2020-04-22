from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('', views.show, name='show'),
    path('login/', views.my_login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.my_logout, name='logout'),
]

urlpatterns += staticfiles_urlpatterns()