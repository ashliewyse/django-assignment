from django import forms
from .models import Comment

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label="Your name")
    email = forms.EmailField(label="Your email")
    message = forms.CharField(widget=forms.Textarea, label="Message")

    from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["name", "email", "message"]