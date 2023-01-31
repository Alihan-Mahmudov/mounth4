from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from users.forms import AuthForm,RegisterForm
from django.contrib.auth.models import User

# Create your views here.

def auth_view(request):
    if request.method == 'GET':
        context = {
            'form': AuthForm
        }

        return render(request, 'users/login.html', context=context)

    if request.method == 'POST':
        form = AuthForm(data=request.POST)

        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data.get('username'),
                password=form.cleaned_data.get('password')
            )
            if user:
                login(request, user)
                return redirect('/products')
            else:
                form.add_error('username', 'Ты боб!!')
        return render(request, 'users/login.html', context={
            'form': form
        })

def logout_view(request):
    if request.method == 'GET':
        logout(request)

    return redirect('/')

def reg_view(request):
    if request.method == 'GET':
        context = {
            'form': RegisterForm
        }

        return render(request, 'users/register.html', context=context)
    if request.method == 'POST':
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            password1, password2 = form.cleaned_data.get('password1'), form.cleaned_data.get('password1')
            if password1 == password2:
                User.objects.create_user(
                    username=form.cleaned_data.get('username'),
                    password=form.cleaned_data.get('password1')
                )
                return redirect('/users/auth')
            else:
                form.add_error('password2', 'Пароли не свпадают!!')

        return render(request, 'users/register.html', context={'form': form})