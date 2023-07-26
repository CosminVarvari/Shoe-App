from django import forms

from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'store', 'price', 'description', 'is_available', 'producer']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'store': forms.Select(attrs={'class': 'form-control'}),
            'price': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'is_available': forms.CheckboxInput(),
            'producer': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'name': 'Enter Product Name:',
            'store': 'Select Store: ',
            'price': 'Enter a price: ',
            'description': 'Enter a Description: ',
            'is_available': 'Is the product available?',
            'producer': 'Select Producer',
        }
