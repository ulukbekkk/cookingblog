from django import forms
from .models import Recipe, Image
from datetime import datetime

class RecipeForm(forms.ModelForm):
    create = forms.DateTimeField(initial=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), required=False)
    class Meta:
        model = Recipe
        fields = '__all__'


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('image', )