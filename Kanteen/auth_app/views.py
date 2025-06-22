from django.shortcuts import render
from django.views.generic import ListView, DetailView
from order_app.models import Student, Order
from django.utils.decorators import method_decorator
from sign_up.decorators import allowed_users


# Create your views here.

@method_decorator(allowed_users(allowed_roles=['admin']), name='dispatch')
class Student_list(ListView):
    model = Student

@method_decorator(allowed_users(allowed_roles=['admin']), name='dispatch')
class Student_detail(DetailView):
    model = Student
@method_decorator(allowed_users(allowed_roles=['admin']), name='dispatch')
class Order_list(ListView):
    model = Order

@method_decorator(allowed_users(allowed_roles=['admin']), name='dispatch')
class Order_detail(DetailView):
    model = Order

