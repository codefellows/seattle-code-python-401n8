from django.contrib import admin
# import the model from models.py
from .models import Thing

# Register your models here.
admin.site.register(Thing)
