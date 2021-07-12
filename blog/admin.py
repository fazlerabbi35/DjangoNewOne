from django.contrib import admin
from .models import blueberry
# Register your models here.

class blueberryAdmin(admin.ModelAdmin):

    list_display = [
        'title',
        'thumbnail',
        'short_description',
        'description',
        'creation'
    ]
admin.site.register(blueberry, blueberryAdmin)