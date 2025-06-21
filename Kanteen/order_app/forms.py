from django.forms import ModelForm
from .models import Order

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['student_name', 'meal1', 'meal2', 'meal3', 'meal4', 'meal5', 'payment_method']
        labels = {
            'meal1': '星期一餐點',
            'meal2': '星期二餐點',
            'meal3': '星期三餐點',
            'meal4': '星期四餐點',
            'meal5': '星期五餐點',
            }

class Order2Form(ModelForm):
    class Meta:
        model = Order
        fields = ['student_name', 'meal1', 'meal2', 'meal3', 'meal4', 'meal5', 'payment_method']
        labels = {
            'meal1': '星期一餐點',
            'meal2': '星期二餐點',
            'meal3': '星期三餐點',
            'meal4': '星期四餐點',
            'meal5': '星期五餐點',
        }