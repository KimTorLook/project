from django.urls import path
from  order_app import views
from django.shortcuts import render

app_name = 'order_app'

urlpatterns = [
    path("daily", views.ordering, name="daily"),
    path("daily/confirmation/<str:order_id/", views.orderConfirmation, name="order_confirmation"),
    path('order/create/', views.create_order, name='create_order'),
    path('order/success/', lambda request: render(request, 'order_success.html'), name='order_success'),

]
