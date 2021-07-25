from django.contrib import admin

from .models import C_model
# Register your models here.

class carosuelAdmin(admin.ModelAdmin):

    list_display = [

        'heading',
        'image',
        'paragraph'
    ]
admin.site.register(C_model, carosuelAdmin)