# forms.py
from django import forms
from .models import Post, Contact

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['Name']

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter your message (max 200 characters)', 'rows': 4, 'maxlength': 200}),
        }

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
