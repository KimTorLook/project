from django.shortcuts import render
from order_app.models import Order, Main_Course, Restaurant
from random import choice, choices

def random_restaurent_for_5_days():
    random_restaurent_list = []
    restaurents = Restaurant.objects.all()
    for x in range(5):
        x = choices(restaurents)
        random_restaurent_list.append(x)  
    return random_restaurent_list

def get_main_course():
    restaurant_list = random_restaurent_for_5_days()
    random_main_course_for_a_day = []
    for x in restaurant_list:
        random_main_course_for_day_x=[]
        random_main_course_1 = Main_Course.objects.get(restaurant = x)
        random_main_course_2 = Main_Course.objects.get(restaurant = x)
        random_main_course_for_day_x.append(random_main_course_1,random_main_course_2)
        random_main_course_for_a_day.extend(random_main_course_for_day_x)
    print(random_main_course_for_a_day)
    # main_course = Main_Course.objects.filter(restaurant__restaurant_name="cafe de coral")



def ordering(request):
         
    if request.method == "GET":
        orders = Order.objects.all() 
        context = {
            "orders": orders,
            "random_restaurent_list":random_restaurent_for_5_days(),
            "random_main_course" : get_main_course()
        }

        return render(request, "order_app/ordering.html", context)
    elif request.method == "POST":
         pass


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
