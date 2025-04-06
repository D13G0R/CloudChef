from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.forms import authenticate
from django import forms
from .models import Users, Roles, Restaurantes


class registerEnterprise(forms.ModelForm):
    class Meta:
        model = Restaurantes
        fields = ["numero_identificacion_tributaria", "rues", "contraseña_restaurante", "direccion_restaurante", "tipo_restaurante", "cedula_propietario"]

        labels = {
        "numero_identificacion_tributaria" : "NIT",
        "rues" : "Nombre del Restaurante (Rues)",
        "contraseña_restaurante" : "Contraseña",
        "direccion_restaurante" : "Direccion",
        "tipo_restaurante": "Gastronomía",
        "cedula_propietario" : "Cedula del Propietario"
        }

        widgets = {
            "numero_identificacion_tributaria" : forms.TextInput(attrs = {
                "placeholder": "Ingrese su NIT",
                "class": "text-2xl font-bold rounded-md p-2"
            }),
            "rues" : forms.TextInput(attrs = {
                "placeholder" : "Ingrese su RUES",
                "class": "text-2xl font-bold rounded-md p-2"
            }),
            "contraseña_restaurante" : forms.PasswordInput(attrs = {
                "placeholder" :  "Ingrese la contraseña de restaurante",
                "class": "text-2xl font-bold rounded-md p-2"
            }),
            "direccion_restaurante" : forms.TextInput(attrs = {
                "placeholder" : "Ingrese la direccion del restaurante",
                "class": "text-2xl font-bold rounded-md p-2"
            }),
            "tipo_restaurante" : forms.TextInput(attrs = {
                "placeholder": "¿Que tipo de comida venden?",
                "class": "text-2xl font-bold rounded-md p-2"
            }),
               "cedula_propietario" : forms.TextInput(attrs = {
                "placeholder" : "Ingrese su cedula",
                "class": "text-2xl font-bold rounded-md p-2"
               })
        }

class registerForm(UserCreationForm):
#     fk_rol_id = forms.ModelChoiceField(
#         queryset=Roles.objects.all(), label="Rol",
#         widget=forms.Select(attrs=
#        {
#            'class': 'border border-gray-300 rounded-md p-2 text-sm w-full',
#
#        })
# )
    class Meta:
        model = Users

        fields = ["first_name", "last_name", "username", "email", 'password1', 'password2', 'fk_rol']  # Incluye 'Rol' aquí
        labels = {
            "first_name": "Nombre",
            "last_name": "Apellido",
            "username": "Nombre de Usuario",
            "email": "Correo",
            "password1" : "Contraseña",
            "password2" : "Confirmacion de contraseña",
            "fk_rol" : "Rol"
        }
        widgets = {
        'first_name': forms.TextInput(attrs={
            'class': 'border border-gray-300 rounded-md p-1 text-sm w-full',
            'placeholder': 'Ingresa tu nombre'
            }),
        'last_name': forms.TextInput(attrs={
                'class': 'border border-gray-300 rounded-md p-1 text-sm w-full',
                'placeholder': 'Ingresa tu apellido'
            }),
        'username': forms.TextInput(attrs={
                'class': 'border border-gray-300 rounded-md p-1 text-sm w-full',
                'placeholder': 'Elige un nombre de usuario'
            }),
        'email': forms.EmailInput(attrs={
                'class': 'border border-gray-300 rounded-md p-1 text-sm w-full',
                'placeholder': 'Ingresa tu correo electrónico'
            }),
        'password1': forms.PasswordInput(attrs={
                'class': 'border border-gray-300 rounded-md p-1 text-sm w-full',
                'placeholder': 'Crea una contraseña'
            }),
        'password2': forms.PasswordInput(attrs={
                'class': 'border border-gray-300 rounded-md p-1 text-sm w-full',
                'placeholder': 'Confirma tu contraseña'
            }),
        }

class loginForm(AuthenticationForm):
    username = forms.CharField(
        label="Nombre de Usuario",
        widget=forms.TextInput(attrs={
            'placeholder' : 'Ingresa tu usuario',
            'class': 'border border-gray-300 rounded-md p-1 text-sm w-full',
        })
    )
    password = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(attrs={
            'placeholder': "Ingresa tu contraseña",
            'class': 'border border-gray-300 rounded-md p-1 text-sm w-full'
        })
    )
    class Meta:
        model= Users
        fields = ["username", "password"]

class formAddUser(forms.ModelForm):
    class Meta:
        model = Users
        fields = ["first_name", "last_name", "username", "email", "fk_rol"]

        labels = {
            "first_name" : "Nombre",
            "last_name" : "Apellido",
            "username" : "Nombre de Usuario",
            "email" : "Correo",
            "fk_rol":"Rol"
        }

        widgets = {
            'first_name': forms.TextInput(attrs = {
                'class': 'border border-gray-300 rounded-md p-1 text-sm w-full',
                'placeholder' : "Ingresa el primer nombre"
            }),
            'last_name' : forms.TextInput(attrs = {
                'class': 'border border-gray-300 rounded-md p-1 text-sm w-full',
                'placeholder': "Ingresa el apellido"
            }),
            'username': forms.TextInput(attrs={
                'class': 'border border-gray-300 rounded-md p-1 text-sm w-full',
                'placeholder': 'Elige un nombre de usuario'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'border border-gray-300 rounded-md p-1 text-sm w-full',
                'placeholder': 'Ingresa tu correo electrónico',
            }),
        }