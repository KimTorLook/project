from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from order_app.models import Order, Main_Course, Restaurant
from random import choice, choices
from .forms import OrderForm

#做ording html
def get_main_course(): #random select 2 main courser for every weekday
    #loop the day 
    list_for_the_week=[]
    restaurents = list(Restaurant.objects.all())
    for day in range(1,6):
        #random the restaurent
        restaurent = choices(restaurents)  #done
        #print(restaurent)
        list_for_today = []
        #random the meal1
        main_course_1_list = list(Main_Course.objects.filter(restaurant__restaurant_name = restaurent[0]))
        main_course_1 = choice(main_course_1_list)
        #random the meal2
        main_course_1_list.remove(main_course_1)
        main_course_2 = choice(main_course_1_list)
        list_for_today.append(main_course_1)
        list_for_today.append(main_course_2)
        list_for_the_week.append(list_for_today)
    return list_for_the_week

def ordering(request):
    mainCourse = get_main_course()
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = OrderForm()

    context ={
        "Monday_A" : mainCourse[0][0],
        "Monday_B" : mainCourse[0][1],
        "Tuesday_A" : mainCourse[1][0],
        "Tuesday_B" : mainCourse[1][1],
        "Wednesday_A" : mainCourse[2][0],
        "Wednesday_B" : mainCourse[2][1],
        "Thursday_A" : mainCourse[3][0],
        "Thursday_B" : mainCourse[3][1],
        "Friday_A" : mainCourse[4][0],
        "Friday_B" : mainCourse[4][1],
        "form" : form
        }
    return render(request, 'order_app/ordering2.html', context)

#做Ording
def create_order(request):
    if request.method == "POST":
        order_id = request.POST.get(order_id)
        order_date_time = request.POST.get(order_date_time)
        school = request.POST.get(school)
        student_name = request.POST.get(student_name)
        meal1 = request.POST.get("meal_1")
        meal2 = request.POST.get("meal_2")
        meal3 = request.POST.get("meal_3")
        meal4 = request.POST.get("meal_4")
        meal5 = request.POST.get("meal_5")
        total_price = request.POST.get(total_price)
        payment_method = request.POST.get(payment_method)
        confirm_payment = request.POST.get(confirm_payment)
        try:
            # 將餐點 ID 轉換為 Main_Course 物件
            order_id = Main_Course.objects.get(order_id=order_id) if meal1 else None
            order_date_time = Main_Course.objects.get(order_date_time=order_date_time) if meal1 else None
            school = Main_Course.objects.get(school=school) if meal1 else None
            student_name = request.POST.get(student_name = student_name)
            meal1_obj = Main_Course.objects.get(id=meal1) if meal1 else None
            meal2_obj = Main_Course.objects.get(id=meal2) if meal2 else None
            meal3_obj = Main_Course.objects.get(id=meal3) if meal3 else None
            meal4_obj = Main_Course.objects.get(id=meal4) if meal4 else None
            meal5_obj = Main_Course.objects.get(id=meal5) if meal5 else None
            total_price = Main_Course.objects.get(total_price=total_price) if meal5 else None
            payment_method = Main_Course.objects.get(payment_method=payment_method) if meal5 else None
            confirm_payment = Main_Course.objects.get(confirm_payment=confirm_payment) if meal5 else None

            student = request.user.student  # 使用 OneToOneField
            school = student.school
            
            # 創建新訂單
            order = Order.objects.create(
                school=school,
                student_name=student,
                meal1=meal1_obj,
                meal2=meal2_obj,
                meal3=meal3_obj,
                meal4=meal4_obj,
                meal5=meal5_obj,
            )
            
            # 計算總價格（假設 Order 模型有 calculate_total_price 方法）
            order.total_price = order.calculate_total_price()
            order.save()
            
            # 重定向到確認頁面
            return redirect('order_app:daily/confirmation')  # 確保 URL 名稱正確
        except Main_Course.DoesNotExist:
            # 如果餐點 ID 無效，返回錯誤訊息
            return render(request, 'order_app/ordering2.html', {'error': '請選擇有效的餐點'})
    return render(request, 'order_app/ordering2.html')
                    
"""
def create_order(request):  
    if request.method == 'POST':
        meal1 = request.POST.get('meal1')
        meal2 = request.POST.get('meal2')
        meal3 = request.POST.get('meal3')
        meal4 = request.POST.get('meal4')
        meal5 = request.POST.get('meal5')
        # 創建 Order 實例
        order = Order.objects.create(
            student_name=request.user.student,  # 假設用戶關聯學生
            meal1=Main_Course.objects.get(id=meal1) if meal1 else None,
            meal2=Main_Course.objects.get(id=meal2) if meal2 else None,
            meal3=Main_Course.objects.get(id=meal3) if meal3 else None,
            meal4=Main_Course.objects.get(id=meal4) if meal4 else None,
            meal5=Main_Course.objects.get(id=meal5) if meal5 else None,
        )
        order.total_price = order.calculate_total_price()  # 假設有此方法
        order.save()
        return redirect('order_success')
    return render(request, 'order_form.html', {'form': form})

    #OrderForm
    #price 必須要有value

"""

def orderConfirmation(request):
    form = OrderForm(request.POST)

    if int(request.GET.get("confirmed", 0)) == 1:
        form.save()
        print("saved")

    context = {
        "form":form,
        "confirmed": 0
    }
    return render(request, "order_app/orderConfirmation.html", context)

def orderConfirmation_bk(request):
    # 假設獲取最新訂單（或根據 order_id 查詢）
    try:
        # 如果你想根據 order_id 查詢，需從 request 中傳遞 order_id
        # 例如：order = Order.objects.get(order_id=request.GET.get('order_id'))
        order = Order.objects.latest('order_date_time')  # 獲取最新訂單
    except Order.DoesNotExist:
        order = None

    # 準備上下文數據
    confirmedData = {
        'Monday': {
            'mealImage': order.meal1.main_course_img.url if order and order.meal1 else None,
            'mealName': order.meal1.main_course_name if order and order.meal1 else '未選擇',
            'price': order.meal1.main_course_price if order and order.meal1 else 0,
        },
        'Tuesday': {
            'mealImage': order.meal2.main_course_img.url if order and order.meal2 else None,
            'mealName': order.meal2.main_course_name if order and order.meal2 else '未選擇',
            'price': order.meal2.main_course_price if order and order.meal2 else 0,
        },
        'Wednesday': {
            'mealImage': order.meal3.main_course_img.url if order and order.meal3 else None,
            'mealName': order.meal3.main_course_name if order and order.meal3 else '未選擇',
            'price': order.meal3.main_course_price if order and order.meal3 else 0,
        },
        'Thursday': {
            'mealImage': order.meal4.main_course_img.url if order and order.meal4 else None,
            'mealName': order.meal4.main_course_name if order and order.meal4 else '未選擇',
            'price': order.meal4.main_course_price if order and order.meal4 else 0,
        },
        'Friday': {
            'mealImage': order.meal5.main_course_img.url if order and order.meal5 else None,
            'mealName': order.meal5.main_course_name if order and order.meal5 else '未選擇',
            'price': order.meal5.main_course_price if order and order.meal5 else 0,
        },
    }

    total_price = order.total_price if order and order.total_price else sum(meal['price'] for meal in confirmedData.values())

    context = {
        'Monday': confirmedData['Monday'],
        'Tuesday': confirmedData['Tuesday'],
        'Wednesday': confirmedData['Wednesday'],
        'Thursday': confirmedData['Thursday'],
        'Friday': confirmedData['Friday'],
        'total_price': total_price,
    }
    return render(request, "order_app/orderConfirmation.html", context)
