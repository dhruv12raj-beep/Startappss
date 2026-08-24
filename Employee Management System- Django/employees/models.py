from django.db import models

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    branch = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    phone_number = models.CharField(max_length=15)


    def __str__(self):
        return self.name