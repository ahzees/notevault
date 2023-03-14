from django.forms import ModelForm, PasswordInput, TextInput

from .models import CustomUser


class RegisterForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ("email", "first_name", "last_name", "password")
        widgets = {
            "email": TextInput(attrs={"class": "email"}),
            "password": PasswordInput(attrs={"class": "password_input"}),
            "first_name": TextInput(attrs={"class": "first_name"}),
            "last_name": TextInput(attrs={"class": "last_name"}),
        }
