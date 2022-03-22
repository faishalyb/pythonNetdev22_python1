from django import forms
from .models import Siswa
class StudentForm(forms.ModelForm):
    class Meta:
        model = Siswa
        fields = ['id', 'Nomor', 'Nama', 'Email']