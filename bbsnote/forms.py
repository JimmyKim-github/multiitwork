from django import forms
from bbsnote.models import Board

class Boardform(forms.ModelForm):
    class Meta:
        model = Board
        fields = ['subject', 'content']
        