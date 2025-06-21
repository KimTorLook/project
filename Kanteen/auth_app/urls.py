from django.urls import path

from auth_app import views
urlpatterns = [
    path("student_list", views.Student_list.as_view(), name = "student_list"),
    path("student_detail/<int:pk>/", views.Student_detail.as_view(), name= "student_detail"),
    path('order_list', views.Order_list.as_view(), name = "order_list"),
    path("order_detail/<uuid:pk>/", views.Order_detail.as_view(), name= "order_detail"),
]