from django import forms
from .models import Donaciones

class DonacionForm(forms.ModelForm):
    class Meta:
        model = Donaciones
        # fields = '__all__'
        fields = ['nombre', 'apellido_pat', 'apellido_mat','monto']
        labels = {
            'nombre': 'Nombre',
            'apellido_pat': 'Apellido Paterno',
            'apellido_mat':'Apellido Materno',
            'monto':'Monto',
            }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido_pat': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido_mat': forms.TextInput(attrs={'class': 'form-control'}),
            'monto': forms.CheckboxSelectMultiple(attrs={'class': 'form-control'}),
        }
