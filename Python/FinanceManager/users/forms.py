from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError

class RegistrationForm(UserCreationForm):
    #password = forms.CharField(widget=forms.PasswordInput, label='Пароль')
    #password_confirm = forms.CharField(widget=forms.PasswordInput, label='Подтверждение пароля')

    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email", "password1", "password2"]
        labels = {
            "first_name": "Имя",
            "last_name": "Фамилия",
            "email": "Электронная почта",
            "username": "Логин",
            "password1": "Пароль",
            "password2": "Подтвердить парол"
        }

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        for name, fields in self.fields.items():
            fields.widget.attrs.update({"class":"form-control"})

# Форма входа
#class LoginForm(forms.Form):
    #username = forms.CharField(label="Логин", max_length=100)
    #password = forms.CharField(label="Пароль", widget=forms.PasswordInput)

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))


#from .models import CustomUser

# Форма регистрации пользователя
#class CustomUserCreationForm(UserCreationForm):
    #class Meta:
        #model = CustomUser
        #fields = ['username', 'email', 'password1', 'password2']

    #def __init__(self, *args, **kwargs):
        #super().__init__(*args, **kwargs)
        #for field in self.fields.values():
            #field.widget.attrs.update({'class': 'form-control'})