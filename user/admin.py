from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'first_name', 'last_name')
    list_filter = ('id', )



