from django.contrib import admin
from .models import meeting, CustomUser
from django.contrib.auth.admin import UserAdmin

# Register your models here.

UserAdmin.fieldsets += ('Custom fields set', {'fields': ('is_student', 'is_teacher')}),

admin.site.register(meeting)
admin.site.register(CustomUser, UserAdmin)