from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from app.models import ToDo

admin.site.register(ToDo)
