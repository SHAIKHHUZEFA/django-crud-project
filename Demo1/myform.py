from django import forms
from .import models

class ProductForm(forms.ModelForm):
    class Meta:
        model= models.Product
        fields= ['pname','pprice','pquantity']