from django.urls import path
from  order_app import views

urlpatterns = [
    path("", views.ordering, ),
]
