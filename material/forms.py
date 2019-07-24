from django import forms
from .models import Material


class Material_form(forms.ModelForm):
    class Meta:
        model = Material
        fields = '__all__'
        exclude = ['locado']
        widgets = {
            'caracteristicas':forms.Textarea(attrs={'cols':15,'rows':4}),
            'observacoes': forms.Textarea(attrs={'cols': 15, 'rows': 4})
        }