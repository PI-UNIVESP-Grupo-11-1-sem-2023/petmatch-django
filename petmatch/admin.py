from django.contrib import admin

# Register your models here.
from .models import Pet,  ONG

admin.site.register(Pet)
admin.site.register(ONG)