from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from app.models import CustomUser,ToDo

admin.site.register(CustomUser, UserAdmin)
admin.site.register(ToDo)