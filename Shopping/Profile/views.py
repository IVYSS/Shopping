from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from Profile.models import My_User
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def showprofile(request):
     user = request.user.id
     test = request.user
     testtwo = My_User.objects.all()
     print(testtwo)
     print(test)
     information = My_User.objects.get(pk=user)
     
     
     print('--------------------------')
     print(user)
     print(information)
     
     context={
          'information': information
     }
     return render(request, 'Profile/profile.html', context=context)

# Chang information profile
@csrf_exempt
def profile_change(request):
     return None