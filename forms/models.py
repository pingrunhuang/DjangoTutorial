from django.db import models

# Create your models here.
from django import forms

class FileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()

class NameForm(forms.Form):
    name = forms.CharField(label="Your name", max_length=100)

class Contact(forms.Form):
    
    # template_name = "contact_form.html" # https://docs.djangoproject.com/en/5.0/ref/forms/api/#ref-forms-api-outputting-html
    subject = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)



