from django.db import models
from datetime import datetime

# Create your models here.
#DRAWBACK: you have to define foreign keys explicitly (whatever that means)
#benefits of using migrations to autoamtically generate the table is that your less likely to make errors

class meeting(models.Model):
    lect_name = models.CharField(max_length=200)
    m_date = models.DateField()
    m_time = models.TimeField()
    descript = models.CharField(max_length=500)
    #attendance = models.BooleanField(blank=True, null=True) #OPTIONS: PRESENT, LATE, NOT PRESENT, LEGIT EXCUSE
    #lecturer_details = models.CharField(max_length=2000, blank=True, null=True)
    #include fields you don't need because it allows future scalability (e.g. venue)

#GET RID OF USER TABLE AND REPLACE IT WITH TWO SEPERATE TABLES: STUDENT AND STAFF
#HAVE A BOOLEAN FIELD IN STAFF FOR ADMINISTRATIVE PRIVELLAGES
#the rationale for this is to avoid having two forgeing keys connecting to the same table
#this allows the whole cacade thing
class student_users(models.Model):
    username = models.CharField(max_length=100)
    email_address = models.EmailField()

class staff_users(models.Model):
    username = models.CharField(max_length=100)
    email_address = models.EmailField()
    admin = models.BooleanField()

#STEPS
#create the models
#fill in some records in the php my admin
#play around with python to get it to work
#THEN add the bells and whistles for the interface