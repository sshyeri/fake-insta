from django.shortcuts import render, redirect
from .forms import CreateUserForm
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def signup(request):
    if request.user.is_authenticated:
        return redirect('posts:list')
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('posts:list')
    else:
        form = CreateUserForm()
    context = { 'form': form }
    return render(request, 'accounts/signup.html', context )
    
def login(request):
    if request.user.is_authenticated:
        return redirect('posts:list')
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'posts:list')
        form.add_error(None, '사용자 이름과 비밀번호를 확인해주세요')
    else:
        form = AuthenticationForm()
    context = {'form' : form }
    return render(request, 'accounts/login.html', context)

@login_required
def logout(request):
    auth_logout(request)
    return redirect('posts:list')