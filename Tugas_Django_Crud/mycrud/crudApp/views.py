from django.shortcuts import render
from django.shortcuts import redirect  # new
from .forms import StudentForm  # new
from .models import Siswa  # new
from django.contrib import messages  # new

# Create your views here.
def addStudent(request):
    if request.method == "POST":
        fm = StudentForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request, 'Data Berhasil Ditambahkan')
        else :
            messages.error(request, 'Gagal Menambahkan Data')
    fm = StudentForm()
    studata = Siswa.objects.all()
    return render(request, 'index.html', context={'fm': fm, 'studata': studata})

def deleteStudent(request, id):
    Siswa.objects.get(pk=id).delete()
    messages.success(request, 'Student Record Deleted')
    return redirect('/')

def edit(request, id):
    instance = Siswa.objects.get(pk=id)
    if request.method == "POST":
        fm = StudentForm(request.POST, instance=instance)
        if fm.is_valid():
            fm.save()
            messages.success(request, 'Student Record Updated')
            return redirect('/')
    fm = StudentForm(instance=instance)
    return render(request, 'edit.html', context={'fm': fm})