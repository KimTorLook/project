from django.shortcuts import render
from order_app.models import Order, Main_Course, Restaurant
from random import choice, choices

def random_restaurent_for_5_days():
    random_restaurent_list = []
    restaurents = Restaurant.objects.all()
    for x in range(5):
        x = choices(restaurents)
        random_restaurent_list.append(x)  
    return random_restaurent_list # <QuerySet [<Restaurant: Tai Hing>, <Restaurant: Tsui Wah>, <Restaurant: Tsui Ho>, <Restaurant: Ngan Lung>]>

"""def get_main_course():
    #loop the day 
    list_for_the_week={}
    restaurents = list(Restaurant.objects.all())
    for day in range(1,6):
        #random the restaurent
        restaurent = choices(restaurents)
        list_for_today = []
        #random the meal1
        main_course_1_list = list(Main_Course.objects.filter(Restaurant__restaurant_name = restaurent))
        main_course_1 = choice(main_course_1_list)
        #random the meal2
        main_course_2_list = main_course_1_list.remove(main_course_1)
        main_course_2 = choice(main_course_2_list)
        list_for_today.append(main_course_1)
        list_for_today.append(main_course_2)
    list_for_the_week[day] = list_for_today
    # main_course = Main_Course.objects.filter(restaurant__restaurant_name="cafe de coral")
"""

def ordering(request):
         
    if request.method == "GET":
        orders = Order.objects.all() 
        context = {
            "orders": orders,
            "random_restaurent_list":random_restaurent_for_5_days(),
            #"random_main_course" : get_main_course()
        }

        return render(request, "order_app/ordering.html", context)
    elif request.method == "POST":
         pass
    
def orderConfirmation(request):
    confirmedData = {
        'Monday': {'mealImage.url': 'pathToImage', 'mealName': 'chosenMealName', 'price': 0},
        'Tuesday': {'mealImage.url': 'pathToImage', 'mealName': 'chosenMealName', 'price': 0},
        'Wednesday': {'mealImage.url': 'pathToImage', 'mealName': 'chosenMealName', 'price': 0},
        'Thursday': {'mealImage.url': 'pathToImage', 'mealName': 'chosenMealName', 'price': 0},
        'Friday': {'mealImage.url': 'pathToImage', 'mealName': 'chosenMealName', 'price': 0},
    }

    total_price = sum(meal['price'] for meal in confirmedData.values())

    context = {
        'Monday': confirmedData['Monday'],
        'Tuesday': confirmedData['Tuesday'],
        'Wednesday': confirmedData['Wednesday'],
        'Thursday': confirmedData['Thursday'],
        'Friday': confirmedData['Friday'],
        'Total Price': total_price,
    }

    return render(request, "order_app/orderConfirmation.html", context)

