from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
#from phonenumber_field.formfields import PhoneNumberField
#from django.contrib.auth.forms import AuthenticationForm
#from phonenumber_field.phonenumber import PhoneNumber
from .models import Profesor
from django import forms

class RegistroForm(UserCreationForm):
    first_name = forms.CharField(max_length=140, required=True)
    last_name = forms.CharField(max_length=140, required=False)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'password1',
            'password2',
        )
        labels = {
            'username': 'Nombre de usuario',
            'email': 'Correo',
            'first_name': 'Nombre(s)',
            'last_name': 'Apellido(s)',
            'password1': 'Contraseña',
            'password2': 'Confirme la Contraseña',

        }

