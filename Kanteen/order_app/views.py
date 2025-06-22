from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from order_app.models import Order, Main_Course, Restaurant, Student
from random import choice, choices
from .forms import OrderForm, Order2Form
from django.contrib.auth.decorators import login_required
from sign_up.decorators import allowed_users

@login_required
def mode_selection(request):
        return render(request, 'order_app/mode_selection.html')


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

@login_required
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
@login_required
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
                    
@login_required
def orderConfirmation(request):
    form = OrderForm(request.POST)
    total_price = 0

    if request.method == 'POST':
        if form.is_valid():
            if int(request.GET.get("confirmed", 0)) == 1:
                order = form.save()
                uuid = order.order_id
                print("saved")
                return redirect('order_app:thanks', order_uuid=uuid)
        else:
            return redirect('order_app:daily')

            # 直接從 cleaned_data 獲取 Main_Course 物件
        meal1 = form.cleaned_data.get('meal1')
        if meal1:
            total_price += meal1.main_course_price if meal1.main_course_price else 0
        meal2 = form.cleaned_data.get('meal2')
        if meal2:
            total_price += meal2.main_course_price if meal2.main_course_price else 0
        meal3 = form.cleaned_data.get('meal3')
        if meal3:
            total_price += meal3.main_course_price if meal3.main_course_price else 0
        meal4 = form.cleaned_data.get('meal4')
        if meal4:
            total_price += meal4.main_course_price if meal4.main_course_price else 0
        meal5 = form.cleaned_data.get('meal5')
        if meal5:
            total_price += meal5.main_course_price if meal5.main_course_price else 0

    context = {
        "form":form,
        "meal1":meal1,
        "meal2":meal2,
        "meal3":meal3,
        "meal4":meal4,
        "meal5":meal5,
        "total_price":total_price,
        "confirmed": 0
    }
    return render(request, "order_app/orderConfirmation.html", context)



@login_required
@allowed_users(allowed_roles=['admin'])
def delete_order(request, order_id):
    order = Order.objects.get(order_id = order_id)
    order.delete()
    return redirect('/auth/order_list')


@login_required
def thanks(request, order_uuid):
    display = Order.objects.get(order_id = order_uuid)
    
    context={
        'display': display,
        'order_uuid': order_uuid
    }
    return render(request, 'order_app/thanks.html', context)