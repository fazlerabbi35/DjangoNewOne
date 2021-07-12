from django.shortcuts import render
from .models import blueberry
# Create your views here.

def indexPage(request):

    blog = blueberry.objects.all()

    context = {
        'blog': blog
    }
    return render(request, 'blog/index.html', context)
