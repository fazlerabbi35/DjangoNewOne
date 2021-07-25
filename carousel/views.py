from django.shortcuts import render

from .models import C_model
# Create your views here.

def viewPage(request):

    carosuel = C_model.objects.all()

    context = {
        'carosuel': carosuel
    }
    return render(request, 'carousel/index.html', context)