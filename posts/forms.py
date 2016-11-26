from django import forms
from .models import Post
from django_summernote.widgets import SummernoteWidget


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        widgets = {
            'text': SummernoteWidget(),
        }
        fields = [
            "title",
            "text",
            "category",
            "published",
            "image",
        ]