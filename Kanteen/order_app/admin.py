from django.contrib import admin
from .models import Student,School, Restaurant, Main_Course, Order
# Register your models here.
admin.site.register(Student)
admin.site.register(School)
admin.site.register(Restaurant)
admin.site.register(Main_Course)
admin.site.register(Order)

"""
@admin.register(MealCombination)
class MealCombinationAdmin(admin.ModelAdmin):
    list_display = ('meal1','meal2', 'meal3', 'meal4', 'meal5')
    list_filter = ( 'combination_id', "meal1")
    search_fields = ('main_course__main_course_name',)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'order_date_time', 'payment_method', 'school')
    list_filter = ('school', 'payment_method')
    search_fields = ('order_id',)
    #inlines = [MealCombinationnline]  # 內聯顯示 OrderMeal
    extra = 5 

class MealCombinationInline(admin.TabularInline):
    model = MealCombination
    extra = 5

from django.contrib import admin
from .models import Student,School, Restaurant, Order, Main_Course, MealCombination
# Register your models here.
admin.site.register(Student)
admin.site.register(School)
admin.site.register(Restaurant)
admin.site.register(Order)
admin.site.register(Main_Course)
admin.site.register(MealCombination)"""