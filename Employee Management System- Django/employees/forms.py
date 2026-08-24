from django import forms

from .models import Employee


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Student

        fields = [
            "user", "name", "branch", "city", 'department', "email"
        ]

        widgets = {
            "demo":forms.CheckboxSelectMultiple()
        }

class Department(forms.ModelForm):
    class Meta:
        model = ["bio", "phone"
                 ]
        pass