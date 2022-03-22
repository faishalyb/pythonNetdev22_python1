from django.db import models

# Create your models here.
class Siswa(models.Model):
    Nomor = models.IntegerField()
    Nama = models.CharField(max_length=100)
    Email = models.EmailField(max_length=100)