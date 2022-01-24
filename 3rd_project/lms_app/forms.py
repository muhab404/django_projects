from django import forms
from .models import *

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields =['category_name']
        widgets={
            'category_name': forms.TextInput(attrs={'class':'form-control'})
        }


class BookForm(forms.ModelForm):
    class Meta:
        model=Book
        fields = [
            
        'title',
        'author',
        'photo_book', 
        'photo_author', 
        'pages',   
        'price' ,
        'rental_price_day', 
        'rental_period', 
        'rental_total',
        'status',
        'category', 
        ]
       
        Widgets ={
            
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'author': forms.TextInput(attrs={'class':'form-control'}),
            'price': forms.TextInput(attrs={'class':'form-control'}),
            'rental_price_day': forms.TextInput(attrs={'class':'form-control', 'id':'rentalprice'}),
            'rental_period': forms.TextInput(attrs={'class':'form-control','id':'rentalperiod'}),
            'rental_total': forms.TextInput(attrs={'class':'form-control','id':'rentaltotal'}),
            'category': forms.Select(attrs={'class':'form-control'}),
        }
        