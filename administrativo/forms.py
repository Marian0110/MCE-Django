from django import forms
from mce.models import Pais

class paisForm(forms.ModelForm):
    class Meta:
        model = Pais
        fields = ['nombre', 'codigo']
        labels = {'nombre':'Pais: ' , 'codigo' : 'Codigo: '}