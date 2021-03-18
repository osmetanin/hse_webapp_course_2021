from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required


@login_required(login_url='/hello/login')
def index(request):
    return HttpResponse("<h3>Hello, %s!</h3>" % request.user.username)


def log_in(request):
    if request.method == 'POST':
        logout(request)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(request.GET['next'])
        else:
            error = 'Invalid credentials!'
    else: # GET
        error = None
    return HttpResponse(render(request, 'hello/login.html', {'error': error}))
