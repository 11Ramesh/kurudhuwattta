from django import forms
from .models import UserRegister
from django.contrib.auth.forms import AuthenticationForm


class UserRegisterForm(forms.ModelForm):
    username = forms.CharField(max_length=100, widget=forms.TextInput())
    email = forms.EmailField(max_length=100, widget=forms.EmailInput())
    adress = forms.CharField(max_length=255, widget=forms.TextInput())
    password = forms.CharField(max_length=100, widget=forms.PasswordInput())
    password1 = forms.CharField(max_length=100, widget=forms.PasswordInput(),label='Conform Password')
    eexample = forms.CharField(max_length=100, widget=forms.TextInput())

   
    
    class Meta:
        model = UserRegister
        fields = ['username', 'email', 'adress', 'password']


    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password1 = cleaned_data.get("password1")

        if password and password1 and password != password1:
            self.add_error('password1', "Passwords do not match")
        return cleaned_data
    


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
