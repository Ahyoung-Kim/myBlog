from django.shortcuts import redirect, render
from django.contrib import auth

# Create your views here.


def login(request):
    if request.method == 'POST':
        uname = request.POST['username']
        pwd = request.POST['password']
        user = auth.authenticate(request, username=uname, password=pwd)

        if user is not None:
            auth.login(request, user)
            return redirect('base')
        else:
            return render(request, 'bad_login.html')

    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('base')
