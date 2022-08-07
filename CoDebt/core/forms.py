from django import forms


class ContactForm(forms.Form):
    full_name = forms.CharField(max_length=100)
    school_name = forms.CharField(max_length=100)
    sender = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)