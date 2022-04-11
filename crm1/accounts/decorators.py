from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_user(view_function):
    '''Redirecting user to home if they are logged in
    and accessing to non-logged-in routes.
    '''
    def wrapper_function(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')

        return view_function(request, *args, **kwargs)
    
    return wrapper_function

def allowed_users(allowed_roles = []):
    def decorator(view_function):
        def wrapper_function(request, *args, **kwargs):
            group = None

            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group in allowed_roles:
                return view_function(request, *args, **kwargs)
            
            return HttpResponse('You are not authorised to view this page')
    
        return wrapper_function
    
    return decorator

def admin_only(view_function):
    def wrapper_function(request, *args, **kwargs):
        group = None

        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
        
        if group == 'customer':
            return redirect('user-page')
        
        if group == 'admin':
            return view_function(request, *args, **kwargs)
        
    return wrapper_function