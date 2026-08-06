from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def books(request):
    return HttpResponse("Welcome to books!")

def book_details(request, id):
    return HttpResponse(f"Book id {id}")