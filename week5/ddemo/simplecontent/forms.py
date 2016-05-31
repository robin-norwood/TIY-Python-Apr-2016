from django import forms
from .models import Article

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'article_text', 'current', 'authors', 'cover_photo' ]
