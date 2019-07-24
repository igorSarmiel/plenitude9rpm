from .models import Publico, Dependentes, Locacao
from django.forms import ModelForm
from django import forms

class Publico_form(ModelForm):
    class Meta:
        model = Publico
        fields = '__all__'
        exclude = ['observacoes']
        widgets = {
            "observacoes":forms.Textarea(attrs={'cols':80, 'rows':20}),
            "data_nascimento":forms.DateInput(attrs={'class':'data'}),
            "telefone1":forms.TextInput(attrs={'class':'telefone'}),
            "telefone2": forms.TextInput(attrs={'class': 'telefone'})
        }


class Dependentes_form(ModelForm):
    class Meta:
        model = Dependentes
        fields = '__all__'
        exclude = ['observacoes']
        widgets = {
             "responsavel":forms.HiddenInput(),
             "data_nascimento":forms.DateInput(attrs={'class':'data',}),
        }

class Obs_publico_form(ModelForm):
    class Meta:
        model = Publico
        fields = ['observacoes']
        widgets = {
            "observacoes": forms.Textarea(attrs={'cols': 80, 'rows': 15}),
        }

class Obs_dependente_form(ModelForm):
    class Meta:
        model = Dependentes
        fields = ['observacoes']
        widgets = {
            "observacoes": forms.Textarea(attrs={'cols': 80, 'rows': 15}),
        }

class Locacao_form(ModelForm):
    class Meta:
        model = Locacao
        fields = "__all__"
        widgets ={
            "locador":forms.HiddenInput(),
            "data_locado":forms.DateInput(attrs={"class":"data",}),
            "data_devolucao":forms.DateInput(attrs={'class':'data'}),
            "observacoes": forms.Textarea(attrs={'cols': 80, 'rows': 10}),
        }