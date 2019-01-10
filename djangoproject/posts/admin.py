from django.contrib import admin
from .models import meeting, staff_users, student_users

# Register your models here.

admin.site.register(meeting)
admin.site.register(staff_users)
admin.site.register(student_users)