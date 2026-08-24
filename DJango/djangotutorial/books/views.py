from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def book(request):
    context = {'name': "hello",
    'data':"this is a view of books page"}
    return render(request,"books/home.html",)

def book_details(request, id):
    return HttpResponse(f"Book id {id}")