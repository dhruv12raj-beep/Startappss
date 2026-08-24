from django.shortcuts import render, get_object_or_404 , redirect
from django.http import HttpResponse
from .models import Employee
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    all_employees = Employee.objects.all()
    return render(request,
                  "employees/employees.html",
                  {"employees" : all_employees})

def about(request):
    return render(request, "employees/about.html")

def contact(request):
    return render(request, "employees/contact.html")

def employee_details(request,id):
    employee = get_object_or_404(Employee,id=id)
    return render(
        request, "employees/employee_details.html",
        {"employee":employee})


    #     def create_employee(request):
    #         if request.method =="POST":
    #             form = StudentForm 
    # )

def create_employee(request):
    if request.method =="POST":
        name = request.POST.get("name")
        department = request.POST.get("department")
        branch = request.POST.get("branch")
        city = request.POST.get("city")
        email = request.POST.get("email")
        phone_number = request.POST.get("phone_number")

        Employee.objects.create(
            name=name,
            department=department,
            branch=branch,
            city=city,
            email=email,
            phone_number=phone_number
        )

        return redirect("employees:employees")
    return render(request, "employees/create_employee.html")


def register(request):
    if request == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        User.objects.create_user(username= username , email  = email , password = password )
        return redirect('login')
    return render(request, "employees/register.html",)



def login(request):
    if request.method == "POST":
        username = request.POST.get(username)
        password= request.POST.get(password)


        user = authenticate(request, username =username , password = password )
        if user is not None:
            login(request,user)
            return redirect("employee-detail")

        return render(request,"employee/home")

@login_required
def dashboard  (request):
    student = Employee.objects.all()
    return render(request,"employee/dashboard.html", {'employee':Employee})