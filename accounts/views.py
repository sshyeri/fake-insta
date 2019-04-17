from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model, update_session_auth_hash
from .forms import UpdateUserForm, ProfileForm
from .models import Profile

# Create your views here.
def signup(request):
    if request.user.is_authenticated:
        return redirect('posts:list')
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user) # 프로필도 생성
            auth_login(request, user)
            return redirect('posts:list')
    else:
        form = UserCreationForm()
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
    
def people(request, username):
    people = get_object_or_404(get_user_model(), username=username)
    context = {'people': people, }
    return render(request, 'accounts/people.html', context)
    
@login_required
def update(request):
    if request.method=='POST':
        form = UpdateUserForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('people', request.user.username )
    else:
        form = UpdateUserForm(instance=request.user)
    context = {'form' : form, }
    return render(request, 'accounts/update.html', context) 
    
@login_required
def password(request):
    if request.method=='POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('people', request.user.username )
    else:
        form = PasswordChangeForm(request.user)
    context = {'form' : form, }
    return render(request, 'accounts/password.html', context) 
    
@login_required
def delete(request):
    if request.method=='POST':
        request.user.delete()
    return redirect('posts:list')
    
@login_required
def profile_update(request):
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('people', request.user.username)
    else:
        profile_form = ProfileForm(instance=request.user.profile)
    context = {'profile_form': profile_form,}
    return render(request, 'accounts/profile_update.html', context)