from django.http import request
from django.shortcuts import render, redirect, HttpResponse
from app.EmailBackEnd import EmailBackEnd
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from app.models import CustomUser


def BASE(request):
    return render(request, 'base.html')


def LOGIN(request):
    return render(request, 'login.html')


def doLogin(request):
    if request.method == "POST":
        user = EmailBackEnd.authenticate(request,
                                         username=request.POST.get('email'),
                                         password=request.POST.get('password'),
                                         )
        if user != None:
            login(request, user)
            user_type = user.user_type
            if user_type == '1':
                return redirect('hod_home')
            elif user_type == '2':
                return HttpResponse('This is Stuff Panel')
            elif user_type == '3':
                return HttpResponse('This is Student Panel')
            else:
                # message
                return redirect('login')
        else:
            messages.error(request, 'Email and Password are Invalid!')
            return redirect('login')

    return None


def doLogout(request):
    logout(request)
    return redirect('login')


def PROFILE(request):
    user = CustomUser.objects.get(id=request.user.id)
    context = {
        "user": user,
    }
    return render(request, 'profile.html', context)


def PROFILE_UPDATE(request):
    if request.method == "POST" :
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('passoword')

        try:
            pass
        except:
            pass

    return render(request, 'profile.html')