from django.shortcuts import render
from .models import Profile
# Create your views here.

def ViewProfile(request):

    profiles = Profile.objects.all()

    context = {
        'profiles' : profiles
    } 
    return render(request, 'Profile/index.html', context)
