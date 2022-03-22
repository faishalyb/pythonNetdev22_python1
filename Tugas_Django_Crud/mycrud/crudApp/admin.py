from django.contrib import admin
from .models import Siswa  # new

# Register your models here.
@admin.register(Siswa)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'Nomor', 'Nama', 'Email']