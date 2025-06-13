from django.shortcuts import render
from order_app.models import Order, Main_Course, Restaurant
from random import choice, choices


def get_main_course(): #random select 2 main courser for every weekday
    #loop the day 
    list_for_the_week=[]
    restaurents = list(Restaurant.objects.all())
    for day in range(1,6):
        #random the restaurent
        restaurent = choices(restaurents)  #done
        print(restaurent)
        list_for_today = []
        #random the meal1
        main_course_1_list = list(Main_Course.objects.filter(restaurant__restaurant_name = restaurent[0]))
        main_course_1_list_str = []
        for main_course in main_course_1_list:
            main_course_str = str(main_course)
            main_course_1_list_str.append(main_course_str)
        main_course_1 = choice(main_course_1_list_str)
        #print("main_course1",main_course_1)

        #random the meal2
        #print("course_1_list", main_course_1_list_str)
        main_course_1_list_str.remove(main_course_1)
        #print("course_2_list", main_course_1_list_str)
        main_course_2 = choice(main_course_1_list_str)
        #print("main_course2", main_course_1_list_str)
        list_for_today.append(main_course_1)
        list_for_today.append(main_course_2)
        list_for_the_week.append(list_for_today)
    # main_course = Main_Course.objects.filter(restaurant__restaurant_name="cafe de coral")
    print(list_for_the_week)
    return list_for_the_week

def get_photo():
    #main_course_list():
    main_course = list(Main_Course.objects.all())
    main_course_list = []
    for x in main_course:
        y = str(x)
        main_course_list.append(y)
    selected_main_course = get_main_course()
    

def ordering(request):
    mainCourse = get_main_course()
    #畀相
    #main_course_list1 = main_course_list()

    Monday_A = mainCourse[0][0]
    Monday_B = mainCourse[0][1]
    Tuesday_A = mainCourse[1][0]
    Tuesday_B = mainCourse[1][1]
    Wensday_A = mainCourse[2][0]
    Wensday_B = mainCourse[2][1]
    Thuesday_A = mainCourse[3][0]
    Thuesday_B = mainCourse[3][1]
    Friday_A = mainCourse[4][0]
    Friday_B = mainCourse[4][1]
        

    #畀錢
    context = {
        "Monday_A" : Monday_A,
        "Monday_A_photo" : Monday_B.main_course_image,
        "Monday_B" : Monday_B,
        #畀錢
        "Tuesday_A" : Tuesday_A,
        "Tuesday_B" : mainCourse[1][1],
        "Wensday_A" : mainCourse[2][0],
        "Wensday_B" : mainCourse[2][1],
        "Thuesday_A" : mainCourse[3][0],
        "Thuesday_B" : mainCourse[3][1],
        "Friday_A" : mainCourse[4][0],
        "Friday_B" : mainCourse[4][1],
        
        }
    
    return render(request, 'order_app/ordering.html', context)

def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()  # save 時會自動計算 total_price
            return redirect('order_success')
    else:
        form = OrderForm()
    return render(request, 'order_form.html', {'form': form})

"""  OrderForm
     price 必須要有value

from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['school', 'student_name', 'meal1', 'meal2', 'meal3', 'meal4', 'meal5', 'payment_method', 'confirm_payment']
        # 排除 total_price，因為它由模型自動計算
"""


    
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

#def ordering(request):
         
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
