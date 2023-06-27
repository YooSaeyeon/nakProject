from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User

# Create your views here.
def accounts(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        repeat_password = request.POST['repeat']
        
        if password == repeat_password:
            if User.objects.filter(username=username).exists():
                return render(request, 'bad_accounts.html')
            else:
                new_user = User.objects.create_user(username=username, password=password)
                auth.login(request, new_user)
                print('회원가입 성공')
                return redirect('index')
        else:
            return render(request, 'bad_accounts.html')
    return render(request, "accounts.html")

def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(request, username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            print('로그인 성공')
            return redirect('index')
        else:
            return render(request, 'bad_login.html')
    return render(request, 'accounts.html')

def logout(request):
    auth.logout(request)
    return redirect('index')