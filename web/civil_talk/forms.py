from .models import Articles
from django.forms import ModelForm, TextInput, Textarea
from django import forms
from django.contrib.auth.forms import UserCreationForm, User
from django.contrib.auth.forms import AuthenticationForm


class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title_talk', 'full_text']

        widgets = {
            'title_talk': TextInput(attrs={
                'class': 'circulate_request',
                'placeholder': 'введите тему обращения'
            }),
            'full_text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст обращения'
            }),
        }


