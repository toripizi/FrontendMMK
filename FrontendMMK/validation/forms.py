from django.forms import ModelForm
from django import forms
from .models import LogMessage


class UploudLogMessage(ModelForm):
    value = forms.TextInput()

    class Meta:
        model = LogMessage
        fields = ["value"]
        