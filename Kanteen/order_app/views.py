from django.shortcuts import render
from order_app.models import Order, Main_Course, Restaurant
from random import choice, choices

def random_restaurent():
    restaurents = Restaurant.objects.all()
    random_restaurents = choices(restaurents)
    return random_restaurents

def random5():
    random_restaurent_list = []
    for x in range(5):
        x = random_restaurent()
        random_restaurent_list.append(x)  
    return random_restaurent_list

def ordering(request):
        
    if request.method == "GET":
        orders = Order.objects.all() 
        context = {
            "orders": orders,
            "random_restaurent_list":random5()  
        }

        return render(request, "order_app/ordering.html", context)
    elif request.method == "POST":
         pass

def ordering_bak(request):
        orders = Order.objects.all() 
        context = {
            "orders": orders
        }
        return render(request, "order_app/ordering.html", context)


"""
#ordering 的view code
meal1 = Main_Course.objects.create(name="乾炒牛")
meal2 = Main_Course.objects.create(name="abcxxx")

# 創建產品並關聯標籤
order = Order.objects.create(ord_id = "{}", papayment_methodyment = "COD")
order = Order.meals.add(meal1, meal2)

#查詢
print(order.meals.all())  # 輸出: <QuerySet [<Tag: new>, <Tag: popular>]>


#過濾
Order.objects.filter(tags__name="new")
"""
