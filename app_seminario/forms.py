from django import forms
from .models import Inscrito, Institucion


class InscritoForm(forms.ModelForm):
    class Meta:
        model = Inscrito
        fields = ['nombre_participante', 'email', 'nro_personas', 'telefono', 'institucion', 'estado', 'observacion']

    def clean_nombre_participante(self):
        nombre = self.cleaned_data['nombre_participante']
        if len(nombre) > 100:
            raise forms.ValidationError("El nombre del participante no puede superar los 100 caracteres.")
        return nombre

class InstitucionForm(forms.ModelForm):
    class Meta:
        model = Institucion
        fields = ['nombre']

class InscritoForm(forms.ModelForm):
    class Meta:
        model = Inscrito
        fields = [
            'nombre_participante', 
            'email', 
            'nro_personas', 
            'telefono', 
            'institucion', 
            'estado', 
            'observacion'
        ]

        
        widgets = {
            'nombre_participante': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre completo'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'ejemplo@correo.com'}),
            'nro_personas': forms.NumberInput(attrs={'class': 'form-control', 'min': '1', 'max': '30'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Teléfono de contacto'}),
            'institucion': forms.Select(attrs={'class': 'form-select'}),
            'estado': forms.Select(attrs={'class': 'form-select'}),
            'observacion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Observaciones adicionales (opcional)'}),
        }