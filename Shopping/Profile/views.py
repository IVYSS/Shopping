from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
# Create your views here.


def showprofile(request):
     
     information = User.objects.get(pk=1)

     
     context={
          'information': information
     }
     return render(request, 'Profile/profile.html', context=context)
