from django.contrib import admin
from books.models import Student, StudentProfile

# Register your models here.
admin.site.register(Student)


@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):
    list_display =["id", "student", "bio","phone", "address"]

    search_fields= ["name", "email", "city"]