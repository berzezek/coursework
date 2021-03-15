from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from django.forms import ModelForm



class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(
        label='Введите Email',
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите Email'})
    )
    username = forms.CharField(
        label='Введите логин',
        required=True,
        help_text='Нельзя вводить символы: @, /, _',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите логин'})
    )

    password1 = forms.CharField(
        label='Введите пароль',
        required=True,
        help_text='Пароль не должен быть маленьким и простым',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Введите пароль'})
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        del self.fields['password2']

    class Meta:
        model = User
        fields = ['username', 'email', 'password1']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(
        label='Введите Email',
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите Email'})
    )
    username = forms.CharField(
        label='Введите логин',
        required=True,
        help_text='Нельзя вводить символы: @, /, _',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите логин'})
    )

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileImageForm(forms.ModelForm):
    img = forms.ImageField(
        label='Загрузить фото',
        required=False,
        widget=forms.FileInput
    )

    mailcheck = forms.BooleanField(
        label='Соглашение про отправку почты',
        required=False,
    )

    CHOICE = (
        ('0', ''),
        ('1', 'Мужской'),
        ('2', 'Женский'),
    )

    u_sex = forms.CharField(
        label='Выберите пол',
        required=False,
        max_length=1,
        widget=forms.Select(attrs={'class': 'form-control'}, choices=CHOICE,),

        )

    class Meta:
        model = Profile
        fields = ['u_sex', 'img', 'mailcheck']
