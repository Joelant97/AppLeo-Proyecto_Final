from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
#from phonenumber_field.formfields import PhoneNumberField
#from django.contrib.auth.forms import AuthenticationForm
#from phonenumber_field.phonenumber import PhoneNumber
from .models import Profesor

class RegistroForm(UserCreationForm):

    class Meta:
        model = User
        fields = [
                'username',
                'first_name',
                'last_name',
                'email',

        ]
        labels = {
                'username': 'Nombre de usuario',
                'first_name': 'Nombre',
                'last_name': 'Apellidos',
                'email': 'Correo',
        }


#Para Acceder al String que contiene el Field con el telefono del Profesor: -->( profesor.telefono.as_e164 )
#Profesor {{ profesor.nombre }} tiene el Teléfono de contacto {{ profesor.telefono }}

class ProfesorForm(UserCreationForm):  #Maybe a uthenticationForm
    class Meta:
        model = Profesor
        fields = [
                'nombre',
                'direccion',
                'telefono',

        ]
                                #if don't work with the field "phone" change for "telefono" in the same line.
    #telefono = PhoneNumberField()
    #phone = PhoneNumber.from_string(phone_number=+(829-555-5555), region='DO').as_e164

