# from dataclasses import fields
# from socket import fromshare
from django import forms
from .models import Csv

class CsvForm(forms.ModelForm):
    class Meta:
        model = Csv
        fields = ('file_name',)