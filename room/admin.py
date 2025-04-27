from django.contrib import admin

# Register your models here.
from .models import Room , Chat

admin.site.register(Room)
admin.site.register(Chat)
