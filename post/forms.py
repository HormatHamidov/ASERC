from cProfile import label
from django import forms
from django.forms import ModelForm
from matplotlib import widgets

from .models import Submission
    
    
class SubmissionForm(ModelForm):
    class Meta:
        model = Submission
        fields = ('articletitle','author_name','affiliation_name','author_email','country','firstname','lastname','email','keywords','abstracted')
        
        labels = {
            'articletitle': 'Article title',
            'author_name':"Corresponding author's name",
            'affiliation_name':"Corresponding author's primary affiliation",
            'country':'Country of primary affiliation',
            'author_email':"Corresponding author's email",
            'firstname':'Name',
            'lastname':'Surname',
            'email':'Email',
            'keywords':'Keywords (5-8 keywords)',
            'abstracted':'Abstract (150-200 words)', 
        }
        
        widgets = {
            'articletitle': forms.TextInput(attrs={'class':'form-control'}),
            'author_name':forms.TextInput(attrs={'class':'form-control'}),
            'affiliation_name':forms.TextInput(attrs={'class':'form-control'}),
            'author_email':forms.EmailInput(attrs={'class':'form-control'}),
            'country':forms.TextInput(attrs={'class':'form-control'}),
            'firstname':forms.TextInput(attrs={'class':'form-control'}),
            'lastname':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'keywords':forms.TextInput(attrs={'class':'form-control','placeholder':'keyword1/keyword2/keyword3'}),
            'abstracted':forms.Textarea(attrs={'class':'form-control'}),
        }
        