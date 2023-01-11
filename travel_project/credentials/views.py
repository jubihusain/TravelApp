from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def register(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name = request.POST['last_name']
        user_name = request.POST['user_name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1==password2 :
            if User.objects.filter(username=user_name).exists():
                messages.info(request, "User already exist.Plz try another")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "email already exist")
                return redirect('register')
            else:
                user = User.objects.create_user(username=user_name, first_name=first_name, last_name=last_name,
                                                email=email, password=password1)
                user.save()
                messages.info(request, 'User created')
                return redirect('login')
        else:
            messages.info(request, 'Password not match')
            return redirect('register')

    return render(request,'register.html')


def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Invalid credentials")
            return redirect('login')

    return render(request,'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')