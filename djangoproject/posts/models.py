from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser

# Create your models here.
#DRAWBACK: you have to define foreign keys explicitly (whatever that means)
#benefits of using migrations to autoamtically generate the table is that your less likely to make errors

class CustomUser(AbstractUser):
    is_student = models.BooleanField('student status', default=False)
    is_teacher = models.BooleanField('teacher stats', default=False)

class meeting(models.Model):
    lect_name = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='teacher')
    m_date = models.DateField()
    m_time = models.TimeField()
    student_name = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='student')
    descript = models.CharField(max_length=500)
    attended = models.BooleanField(blank=True, null=True) #OPTIONS: PRESENT, LATE, NOT PRESENT, LEGIT EXCUSE
    #lecturer_details = models.CharField(max_length=2000, blank=True, null=True)
    #include fields you don't need because it allows future scalability (e.g. venue)

    def __str__(self):
        return self.descript
