from django.urls import path, include
from . import views


app_name = 'boost'
urlpatterns = [
    path('', views.ViewProfile, name="ViewProfile")
]