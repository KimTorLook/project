from django.urls import path
from sign_up import views

urlpatterns = [
    path("", views.sign_up_index, name="sign_up_index"),
    path("signup/", views.signup, name="signup"),
    path("signup_profile/", views.signup_profile, name="signup_profile"),
    path("unauth/", views.sign_up_unauthorized, name="unauthorized"),
    path("homepage/", views.homepage, name="homepage"),
]