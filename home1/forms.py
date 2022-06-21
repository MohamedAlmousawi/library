from django import forms

from home1.models import Book, Category


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            'title',
            'auther',
            'book_image',
            'auther_image',
            'pages',
            'status',
            'prise',
            'rented_prise_day',
            'rented_time',
            'book_category',
        ]
        widgets ={
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'auther':forms.TextInput(attrs={'class':'form-control'}),
            'book_image':forms.FileInput(attrs={'class':'form-control'}),
            'auther_image':forms.FileInput(attrs={'class':'form-control'}),
            'pages':forms. NumberInput(attrs={'class':'form-control'}),
            'status':forms.Select(attrs={'class':'form-control'}),
            'prise':forms.NumberInput(attrs={'class':'form-control'}),
            'rented_prise_day':forms.NumberInput(attrs={'class':'form-control'}),
            'rented_time':forms.NumberInput(attrs={'class':'form-control'}),
            'book_category':forms.Select(attrs={'class':'form-control'}),

        }
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = [
            'category'
        ]
        widgets = {
            "category":forms.TextInput(attrs={'class':'form-control'})
        }