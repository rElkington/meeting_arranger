from django.db import models
from datetime import datetime

# Create your models here.
#benefits of using migrations to autoamtically generate the table is that your less likely to make errors

class PostModel(models.Model):
    lect_name = models.CharField(max_length=200)
    time = models.TimeField()
    date = models.DateField()
    descript = models.CharField(max_length=300)

