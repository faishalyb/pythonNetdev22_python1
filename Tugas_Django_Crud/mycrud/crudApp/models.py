from django.db import models

# Create your models here.
class Student(models.Model):
    rollno = models.IntegerField()
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)