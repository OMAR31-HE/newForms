
from django.shortcuts import render, redirect
from .forms import StudentForm
from .models import Student


def student(request):
    form = StudentForm(request.POST or None, request.FILES or None)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('students')

    return render(request, 'pages/student.html', {'form': form})


def students(request):
    data = Student.objects.all()
    return render(request, 'pages/students.html', {'data': data})
