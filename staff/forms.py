from django import forms
import datetime


class Notices(forms.Form):
    n_date=day = forms.DateTimeField()
    n_title=forms.CharField(max_length=255)
    n_data=forms.CharField(widget=forms.Textarea)
