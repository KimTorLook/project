from django.urls import path
from  order_app import views

urlpatterns = [
    path("daily", views.ordering, name="daily"),
]
