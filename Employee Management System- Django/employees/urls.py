from django.urls import path
from .import views

urlpatterns= [ path('',views.home, name ="employees"),
    path('about',views.about,name= "about"),
    path('contact',views.contact, name= "contact"),
    path('<int:id>',views.employee_details, name = "employee_detail"),
    path("create",views.create_employee, name = "create_emp"),
    path("register",views.register, name = "register"),
    path("login",views.login, name = "login"),
    ] 