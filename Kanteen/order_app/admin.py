from django.contrib import admin
from .models import Student,School, Restaurant, Order, Main_Course
# Register your models here.
admin.site.register(Student)
admin.site.register(School)
admin.site.register(Restaurant)
admin.site.register(Order)
admin.site.register(Main_Course)