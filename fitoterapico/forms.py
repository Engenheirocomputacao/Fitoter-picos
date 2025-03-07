from django import forms
from fitoterapico.models import Fitoterapico




class FitoterapicoModelForm(forms.ModelForm):
    class Meta:
        model = Fitoterapico
        fields = '__all__'

    def clean_preco(self):
        preco = self.cleaned_data.get('preco')
        if preco < 1:
            self.add_error('preco', 'O preço deve ser maior que R$1,00.')
        return preco