from django.db import models

# Create your models here.

class Profile(models.Model):

    name = models.CharField(max_length=30)
    picture = models.ImageField(upload_to='Profile/')
    age = models.IntegerField()
    address = models.TextField()