from django import forms

from .models import Post
from .models import CV

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text',)

class CVForm(forms.ModelForm):
    class Meta:
        model = CV
        fields = ('title', 'date', 'location', 'text', 'l1', 'l2', 'l3',)