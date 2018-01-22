from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100, default='')

    class Meta:
        db_table = 'students'
