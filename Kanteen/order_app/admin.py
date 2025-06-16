from django.contrib import admin
from .models import Student,School, Restaurant, Main_Course, Order
# Register your models here.


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'order_date_time', 'payment_method')
    list_filter = ['payment_method']
    search_fields = ('order_id',)
    extra = 5 

@admin.register(Main_Course)
class MainCourseAdmin(admin.ModelAdmin):
    list_display = ('main_course_name', 'restaurant', 'main_course_price', 'main_course_cost')
    list_filter = ('restaurant',)
    search_fields = ('main_course_name', 'restaurant__restaurant_name')  
    readonly_fields = ('main_course_id',)
    fieldsets = (
        (None, {
            'fields': ('main_course_id', 'main_course_name', 'restaurant', 'main_course_cost', 'main_course_price', 'main_course_img')
        }),
    )

# Restaurant Admin
@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('restaurant_name',)  
    list_filter = () 
    search_fields = ('restaurant_name',)

# School Admin
@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ('school_name',)  
    list_filter = ()
    search_fields = ('school_name',)

# Student Admin
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_id', 'first_name', 'last_name', 'date_of_birth', 'Email','school','is_active' )  
    list_filter = ('school',)
    search_fields = ('first_name',)
