from django import forms
from .models import product

class Productform(forms.ModelForm):
    class Meta:
        model= product
        fields=['name','size','colour','price','image']