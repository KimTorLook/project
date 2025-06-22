from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_user_only(view):
    def wrapper(request, *arg, **kwarg):
        if request.user.is_authenticated:
            return HttpResponse("你不被允許存取此頁面")
        else:
            return view(request, *arg, **kwarg)
    return wrapper

def allowed_users(allowed_roles=[]):
    def decorator(view):
        def wrapper(request, *args, **kwargs):
            if request.user.groups.exists():
                groups = request.user.groups.all()
                for x in groups:
                    if x.name in allowed_roles:
                        return view(request, *args, **kwargs)
                    else:
                        return redirect("unauthorized")
            else:
                return HttpResponse("No roles defined")
        return wrapper
    return decorator