'''Employee model declared'''
import profile
from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=20)
    employee_number = models.CharField(max_length=20)
    salary = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    date_of_birth = models.DateTimeField(null=True)
    profile_picture = models.ImageField(upload_to="media/pictures", null=True)