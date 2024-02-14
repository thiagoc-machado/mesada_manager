from django.shortcuts import render

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.conf import settings




def my_login(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            if request.user.is_staff:
                return redirect('parents')
            else:
                return redirect('kids')
            
        users = User.objects.all()
        print(users)
        return render(request, 'login.html', {'users': users})
    
    elif request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        remember_me = request.POST.get('remember', None)
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            if remember_me:
                request.session.set_expiry(604800) # 1 semana em segundos
                print("remenber")
            else:
                request.session.set_expiry(0)
                print("not_remenber")
            if user.is_staff:
                return redirect('parents')
            else:
                return redirect('kids')
        else:
            messages.add_message(request, constants.ERROR, 'Usuário ou senha incorretos')
            users = User.objects.all()
            return render(request, 'login.html', {'users': users})

        # return HttpResponse(f'{username} {password} {remember}')


def sair(request):
    logout(request)
    users = User.objects.all()
    return render(request, 'login.html', {'users': users})


