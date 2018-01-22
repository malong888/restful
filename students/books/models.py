from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=100, default='')

    class Meta:
        db_table = 'books'
