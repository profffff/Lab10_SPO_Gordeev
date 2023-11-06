from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput, NumberInput, FileInput


class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'autor', 'anons', 'full_text_pdf', 'quantity']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Name'
            }),
            'autor': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Name_autor'
            }),
            'anons': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Summary'
            }),

            'full_text_pdf': FileInput(attrs={
                'class': 'form-control',
                'placeholder': 'Book'
            }),
            'quantity': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Quantity_of_available_books'
            }),
        }