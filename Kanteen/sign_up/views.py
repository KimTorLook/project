from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import Student_profileForm


# Create your views here.
def sign_up_index(request):
    return render(request, "sign_up/index.html")


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("homepage")
    else:
        form = UserCreationForm()

    context = {
        "form": form
    }

    return render(request, "sign_up/signup.html", context)

def signup_profile(request):
    form = Student_profileForm(request.POST)
    if form.is_valid():
        form.save()  # ✅ Saves form data to the database
        return redirect('login')

    else:
        form = Student_profileForm()

    return render(request, "sign_up/signup_profile.html", {"form": form})



def sign_up_unauthorized(request):
    return render(request, "sign_up/unauthorized_user.html")

def homepage(request):
    return render(request, "sign_up/homepage.html")




