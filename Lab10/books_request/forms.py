from .models import Books_request
from django.forms import ModelForm, TextInput, DateTimeInput, NumberInput, FileInput


class Books_requestForm(ModelForm):
    class Meta:
        model = Books_request
        fields = ['user_id', 'book_id', 'date_added', 'date_checked_by_admin', 'date_withdrawal', 'status']

        widgets = {
            'user_id': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'user_id'
            }),
            'book_id': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'book_id'
            }),
            'date_added': DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'date_added'
            }),
            'date_checked_by_admin': DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'date_checked_by_admin'
            }),

            'date_withdrawal': DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'date_withdrawal'
            }),
            'status': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'status'
            }),
        }