from django.shortcuts import render
from order_app.models import Order, Main_Course


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
