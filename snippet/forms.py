from django import forms
from .models import Tag
from .models import Snippet

class SnippetForm(forms.ModelForm):
    class Meta:
        model = Snippet
        fields = [
            'user',
            'language',
            'title',
            'usage_description',
            'code_text',
            'labels',
        ]

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = [
            'label',
        ]