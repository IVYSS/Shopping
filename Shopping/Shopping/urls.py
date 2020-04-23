from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url

from django.conf import settings
from django.views.static import serve
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('profile/', include('Profile.urls')),
    path('index/', include('Index.urls')),
    path('accounts/', include('allauth.urls')),
    path('', TemplateView.as_view(template_name = 'Index/home.html'))
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
