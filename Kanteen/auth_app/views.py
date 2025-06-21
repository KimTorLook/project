from django.shortcuts import render
from django.views.generic import ListView, DetailView
from order_app.models import Student, Order

# Create your views here.

class Student_list(ListView):
    model = Student

class Student_detail(DetailView):
    model = Student

class Order_list(ListView):
    model = Order

class Order_detail(DetailView):
    model = Order

