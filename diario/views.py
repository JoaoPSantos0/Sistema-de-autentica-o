from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User


# Create your views here.

def home(request):
    print(request.method)
    if request.method == 'GET':
        return render(request,'home.html')
    elif request.method == 'POST':
        user = request.POST.get('user')
        senha = request.POST.get('password')

        user = authenticate(request,username=user,password=senha)

        if user:
            #
            return redirect ('home')
        else:
            return HttpResponse("Nome de usuário ou senha inválidos.")


def sign_up(request):
    print(request.method)

    if request.method == 'GET':
        #lista = User.objects.all()
        #print(lista)
        return render(request,'signup.html')
    elif request.method == 'POST':
        user = request.POST.get('user')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirmed_password = request.POST.get('password_confirm')

        if password == confirmed_password:
            """user = User(
                name = user,
                email = email,
                senha = password
            )"""
            new_user = User.objects.create_user(username=user, email=email ,password=password)

            new_user.save()
            return redirect('login')
        else:
            return HttpResponse.charset('Senhas inválidas')
        
        

def menu(request):
    return render(request,'menu.html')