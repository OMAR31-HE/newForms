from enum import unique

from django.db import models
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    university_id = models.IntegerField(unique=True)
    id_number = models.IntegerField()
    mobile_no = models.IntegerField()
    address = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    image = models.ImageField(upload_to='images/')
    def __str__(self):
        return self.name
#