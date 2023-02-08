from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'custom-class'}))

    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']
        widgets = {
        'name': forms.TextInput(attrs={'class': 'form-control'}),
        'email': forms.TextInput(attrs={'class': 'form-control'}),
        'message': forms.TextInput(attrs={'class': 'form-control'}),
        
    }