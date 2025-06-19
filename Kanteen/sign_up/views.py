from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import Student_profileForm
from django.http import HttpResponse
from .decorators import unauthenticated_user_only


# Create your views here.
def homepage(request):
    return render(request, "introduction.html")

def sign_up_index(request):
    return render(request, "sign_up/index.html")

@unauthenticated_user_only
def signup(request):
    if request.user.is_authenticated:
        return HttpResponse("you are not authorized to be on this page !!!")
    else:
        if request.method == "POST":
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect("index")
        else:
            form = UserCreationForm()
        return render(request, 'sign_up/signup.html', {"form": form})

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




