from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'custom-class'}))

    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']