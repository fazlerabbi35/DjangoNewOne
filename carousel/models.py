from django.db import models

# Create your models here.

class C_model(models.Model):

    heading = models.CharField(max_length=100)
    image = models.ImageField(upload_to='carousel/')
    paragraph = models.TextField()
    