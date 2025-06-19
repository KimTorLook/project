from django.http import HttpResponse

def unauthenticated_user_only(view):
    def wrapper(request, *arg, **kwarg):
        if request.user.is_authenticated:
            return HttpResponse("you are not allowed to be on this page")
        else:
            return view(request, *arg, **kwarg)
    return wrapper