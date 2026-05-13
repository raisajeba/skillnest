from django import forms

from .models import ExchangeRequest

class ExchangeForm(forms.ModelForm):
    class Meta:
        model = ExchangeRequest
        fields = ['sender', 'receiver', 'message']
