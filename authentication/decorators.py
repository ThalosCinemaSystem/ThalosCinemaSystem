from django.shortcuts import redirect


def unauthenticated(url=''):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            if request.user.is_authenticated:
                return redirect(url)
            else:
                return view_func(request, *args, **kwargs)
        return wrapper_func
    return decorator
