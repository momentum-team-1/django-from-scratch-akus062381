from django import forms
from .models import Tag
from .models import Snippet

class SnippetForm(forms.ModelForm):
    class Meta:
        model = Snippet
        fields = [
            'title',
            'usage_description',
            'language',
            'code_text',
            'labels',
        ]

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = [
            'label',
        ]