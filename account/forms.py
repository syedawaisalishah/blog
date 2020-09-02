from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm,PasswordChangeForm


from django import forms
class Signupform(UserCreationForm):
    password1=forms.CharField(max_length=70,label='Password',widget=forms.PasswordInput(attrs={'class': 'form-input','placeholder': 'Password'}))
    password2=forms.CharField(max_length=70,label='Confirm Password',widget=forms.PasswordInput(attrs={'class': 'form-input','placeholder': 'Repeat your password'}))
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email']
        widgets={
            'username':forms.TextInput(attrs={'class': 'form-input','placeholder': 'Your Name'}),
            'first_name':forms.TextInput(attrs={'class': 'form-input','placeholder': 'First Name'}),
            'last_name':forms.TextInput(attrs={'class': 'form-input','placeholder': 'Last Name'}),
            'email':forms.EmailInput(attrs={'class': 'form-input','placeholder': 'Email'}),
            'password':forms.PasswordInput(attrs={'class': 'form-input','placeholder': 'Password'})
        }

     
class logins(AuthenticationForm):
    username=forms.CharField(max_length=40,widget=forms.TextInput(attrs={'class': 'form-input' ,'placeholder': 'Username '}))    
    password=forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={'class': 'form-input','placeholder': 'Password'}))    
class changePassword(PasswordChangeForm):
    old_password=forms.CharField(max_length=40,label='Old password:',widget=forms.PasswordInput(attrs={'class': 'form-input'}))    
    new_password1=forms.CharField(max_length=40,label='New password:',widget=forms.PasswordInput(attrs={'class': 'form-input'}))    
    new_password2=forms.CharField(max_length=40,label='New password confirmation:',widget=forms.PasswordInput(attrs={'class': 'form-input'}))    
# Model form
