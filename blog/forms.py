from django import forms
from .models import Comment, Contact


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("name", "email", "content")
        widgets = {
            'name': forms.TextInput(attrs={'class': "col-sm-12"}),
            'email': forms.TextInput(attrs={'class': "col-sm-12"}),
            'content': forms.Textarea(attrs={'class': "form-control"})
        }


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email', 'subject', 'message')
        widgets = {
            'name': forms.TextInput(attrs={'class': "col-sm-12"}),
            'email': forms.TextInput(attrs={'class': "col-sm-12"}),
            'subject': forms.TextInput(attrs={'class': "col-sm-12"}),
            'message': forms.Textarea(attrs={'class': "form-control"})
        }