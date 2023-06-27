from django import forms
from .models import apply

class PostModelForm(forms.ModelForm):
    class Meta:
        model = apply
        fields = ['name', 'number', 'instrument', 'link', 'body']
