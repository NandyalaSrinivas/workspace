from django import forms
from .models import RecipesName


class RecipesForm(forms.ModelForm):
    class Meta:
        model = RecipesName
        fields = '__all__'
