from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


# Registration form for the user
class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    # validation
    # def clean(self):
    #     cleanedData = super().clean()
    #     password = cleanedData.get('password')
    #     passwordConfirm = cleanedData.get('passwordConfirm')        
    #     # Check if the passwords match
    #     if password and passwordConfirm and password != passwordConfirm:
    #         raise forms.ValidationError("Passwords do not match!")