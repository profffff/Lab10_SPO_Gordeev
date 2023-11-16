from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput, NumberInput, FileInput


class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'autor', 'owner']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Name'
            }),
            'autor': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Name_autor'
            }),
            'owner': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Summary'
            }),

        }