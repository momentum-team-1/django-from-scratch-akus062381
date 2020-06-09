from django.db import models
from users.models import User

LANGUAGE_CHOICES = (
    ('HTML', 'HTML'),
    ('CSS', 'CSS'),
    ('JAVASCRIPT', 'JavaScript'),
    ('PYTHON', 'Python'),
)

# Create your models here.
# unique Tag means you can query it using "get"
class Tag(models.Model):
    tag = models.CharField(max_length=100, unique=True) 

    def __str__(self):
        return self.tag

class Snippet(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="snippets")
    language = models.CharField(max_length=255, choices=LANGUAGE_CHOICES, default='PYTHON')
    title = models.CharField(max_length=255, blank=True, null=True)
    date_of_creation = models.DateField(auto_now_add=True)
    usage_description = models.CharField(max_length=255)
    code_text = models.TextField(max_length=1000, blank=True, null=True, help_text="Type snippet here!")
    tags = models.ManyToManyField(to=Tag, related_name="snippets")
    # use models.ForeignKey('self', on_delete=models.CASCADE) if I want to use
    # smaller snippets of code that refer back to a parent snippet

    def tag_names(self):
        tag_names = []
        for tag in self.tags.all():
            tag_names.append(tag.tag)
        
        return " ".join(tag_names)

    def set_tag_names(self, tag_names):
        
        tag_names = tag_names.split()
        tags = []
        for tag_name in tag_names:
            tag = Tag.objects.filter(tag=tag_name).first()
            if tag is None:
                tag = Tag.objects.create(tag=tag_name)
            tags.append(tag)
        self.tags.set(tags)
    
    # def save(self, commit=True):
    #     snippet = super().save(commit=True)
    #     all_tag_names = self.cleaned_data['tag_names']
    #     snippet.set_tag_names(all_tag_names)
    #     return snippet

    def __str__(self):
        return self.title
        return self.language
        


