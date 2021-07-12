from django.db import models

# Create your models here.
class blueberry(models.Model):

    title = models.CharField(max_length=90)
    thumbnail = models.ImageField(upload_to="blueberry/")
    short_description = models.TextField()
    description = models.TextField()
    creation = models.DateTimeField(auto_now_add=True)