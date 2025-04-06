from django import forms
from .models import Platos

class createPlatoForm(forms.ModelForm):
    class Meta:
        model = Platos
        fields = ["nombre_plato", "descripcion_plato", "precio"]

        labels = {
            "nombre_plato" : "Nombre del Plato",
            "descripcion_plato": "Descripcion",

            "precio": "Precio"
        }

        widgets = {
            "nombre_plato": forms.TextInput(attrs={
                "class": "text-xl border border-gray-200 rounded-lg p-2",
                "placeholder": "Nombre del plato",
            }),
            "descripcion_plato": forms.Textarea(attrs={
                "class": "text-xl border border-gray-200 rounded-lg p-2",
                "placeholder": "Describe el plato",
                "rows": 3,
            }),
            "precio": forms.NumberInput(attrs={
                "class": "text-xl border border-gray-200 rounded-lg p-2",
                "placeholder": "Precio del producto",
            })
        }

class EditPlatoForm(forms.ModelForm):
    class Meta:
        model = Platos
        fields = ["nombre_plato", "descripcion_plato", "precio"]

        labels = {
            "nombre_plato": "Nombre del Plato",
            "descripcion_plato": "Descripción",
            "precio": "Precio del Producto"
        }
        widgets = {
            "nombre_plato": forms.TextInput(attrs={
                "class": "text-xl border border-gray-200 rounded-lg p-2",
                "placeholder": "Nombre del plato",
            }),
            "descripcion_plato": forms.Textarea(attrs={
                "class": "text-xl border border-gray-200 rounded-lg p-2",
                "placeholder": "Describe el plato",
                "rows": 3,
            }),
            "precio": forms.NumberInput(attrs={
                "class": "text-xl border border-gray-200 rounded-lg p-2",
                "placeholder": "Precio del producto",
            })
        }