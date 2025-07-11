from django import forms
from .models import Movie

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'year', 'director', 'genre', 'synopsis', 'picture']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control bg-dark text-white border-primary',
                'placeholder': 'Ice Age'
            }),
            'year': forms.NumberInput(attrs={
                'class': 'form-control bg-dark text-white border-primary',
                'placeholder': '2002'
            }),
            'director': forms.TextInput(attrs={
                'class': 'form-control bg-dark text-white border-primary',
                'placeholder': 'Chris Wedge'
            }),
            'genre': forms.TextInput(attrs={
                'class': 'form-control bg-dark text-white border-primary',
                'placeholder': 'Animación'
            }),
            'synopsis': forms.TextInput(attrs={
                'class': 'form-control bg-dark text-white border-primary',
                'placeholder': 'Hace 20.000 años.....'
            }),
            'picture': forms.ClearableFileInput(attrs={
                'class': 'form-control bg-dark text-white border-primary',
                'id': 'image_field',
            }),
        }
