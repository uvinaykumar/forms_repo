from django.contrib import admin
from .models import formsmodel

class AdminName(admin.ModelAdmin):
    list_display = ['name','email','sal','loc','mobile']

admin.site.register(formsmodel,AdminName)

