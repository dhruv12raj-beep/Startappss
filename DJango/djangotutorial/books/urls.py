from django.urls import path 
from . import views

urlpatterns= [
    path("", views.book),
    path("<int:id>/",views.book_details),
]

