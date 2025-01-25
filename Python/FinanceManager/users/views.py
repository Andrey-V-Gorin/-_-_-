from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import RegistrationForm, LoginForm, UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Регистрация прошла успешно!')
            return redirect("profile")
        else:
            messages.error(request, 'Регистрация не удалась. Пожалуйста, повторите попытку.')
    else:
        form = RegistrationForm(request.GET)
    return render(request, "users/registration.html", {"form":form})

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get['username']
            password = form.cleaned_data.get['password']
            user = authenticate(request, username = username, password1 = password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Вы успешно вошли в систему!')
                return redirect ("profile")
            else:
                messages.error(request, 'Неверный логин или пароль.')
        else:
            messages.error(request, 'Неверный логин или пароль.')
    else:
        form = LoginForm()
    return render(request, "users/login.html", {"form":form})

@login_required
def logout_view(request):
    logout(request)
    return redirect("/")

@login_required
def profile (request):
    return render(request, "users/profile.html")

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


@login_required
def update_profile(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')

        # Обновляем данные пользователя
        user = request.user
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.save()

        messages.success(request, 'Ваш профиль был успешно обновлен!')
        return redirect('profile')  # Переход на страницу профиля

    # Отображаем текущие данные в форме
    return render(request, 'users/update_profile.html', {
        'user': request.user,
    })

    

    



    