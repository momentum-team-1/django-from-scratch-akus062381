from django import forms
from .models import Tag
from .models import Snippet

class SnippetForm(forms.ModelForm):
    tag_names = forms.CharField(help_text="Enter tags separated by spaces.", label="Tags", widget=forms.TextInput(attrs={'class': 'f4 w-100'}))

    class Meta:
        model = Snippet
        fields = [
            'language',
            'title',
            'usage_description',
            'code_text',
            'tag_names',
        ]
        widgets = {
            'title' : forms.TextInput(attrs={'class': 'pa2 f4 w-100'}),
            'usage_description': forms.TextInput(attrs={'class': 'pa2 f4 w-100'}),
            'code_text': forms.Textarea(attrs={'class': 'f4 w-100'}),
            'tag_names': forms.TextInput(attrs={'class': 'pa2 f4 w-100'})
        }

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = [
            'tag',
        ]
        