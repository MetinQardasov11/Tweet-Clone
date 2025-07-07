from django import forms
from django.forms import ModelForm
from .models import Tweet


class AddTweetForm(forms.Form):
    message = forms.CharField(
        required=True,
        label='Message',
        widget=forms.Textarea(attrs={'class': 'form-control'})
    )
    
    

class AddTweetModelForm(ModelForm):
    class Meta:
        model = Tweet
        fields = ['message']
        widgets = {
            'message': forms.Textarea(attrs={'class': 'form-control'})
        }