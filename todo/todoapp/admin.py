from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from todoapp.models import ToDo

admin.site.register(ToDo)
