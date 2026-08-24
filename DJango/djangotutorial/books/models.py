from django.db import models

# Create your models here.
class Student(models.Model):
    name= models.CharField(max_length=100)
    email= models.EmailField(unique=True)
    age= models.PositiveIntegerField()
    city= models.CharField(max_length=20)
    course = models.CharField(max_length=100,null= True, blank=True)
    is_active= models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class StudentProfile(models.Model):
    student = models.OneToOneField(Student,on_delete=models.CASCADE,related_name="profile",)
    bio= models.TextField(blank=True)
    phone = models.CharField(max_length=15,blank =True)
    address = models.TextField(blank = True)

    def __str__(self):
        return f"profile-{self.student.name}"


class StudentQuerySet(models.QuerySet):
    def active(self):
        return self.filter(is_active = True)
    
class StudentQuerySet(models.QuerySet):
    def inactive(self):
        return self.filter(is_active = False)
    
class StudentQuerySet(models.QuerySet):
    def adults(self):
        return self.filter(age__gte = True)

