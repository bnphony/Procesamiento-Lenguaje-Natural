from django import forms
from django.forms import Textarea

from core.erp.models import Auxiliar
from django.forms import ModelForm


class IngresoRelatoUsuarioForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    # relatoUsuario = forms.CharField(widget=forms.Textarea(attrs={
    #     'placeholder': 'Ingrese un relato de usuario',
    #     # 'class': 'form-control',
    #     'autocomplete': 'off',
    #     'style': 'width: 60%; margin: 20px'
    # }))

    class Meta:
        model = Auxiliar
        fields = '__all__'
        widgets = {
            'relatoUsuario': Textarea(
                attrs={
                    'placeholder': 'Ingrese un relato de usuario',
                    'autocomplete': 'off',
                    'style': 'width: 60%; margin: 20px'
                }
            )
        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data
