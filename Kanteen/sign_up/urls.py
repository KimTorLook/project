from django.urls import path
from sign_up import views

urlpatterns = [
    path("", views.signup, name="signup"),
    path("signup_profile/", views.signup_profile, name="signup_profile"),
    path("unauth/", views.sign_up_unauthorized, name="unauthorized"),
]