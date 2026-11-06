
from django.urls import path
from . import views

urlpatterns = [
    path('', views.student, name='student'),
    path('students/', views.students, name='students'),
]
