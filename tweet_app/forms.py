from django import forms
from django.forms import ModelForm
from .models import Tweet


class AddTweetForm(forms.Form):
    username = forms.CharField(
        max_length=100,
        required=True,
        label='Username',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    message = forms.CharField(
        required=True,
        label='Message',
        widget=forms.Textarea(attrs={'class': 'form-control'})
    )
    
    

class AddTweetModelForm(ModelForm):
    class Meta:
        model = Tweet
        fields = ['username', 'message']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control'})
        }