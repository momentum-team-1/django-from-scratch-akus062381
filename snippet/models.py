from django.db import models
from users.models import User

LANGUAGE_CHOICES = (
    ('HTML', 'html'),
    ('CSS', 'css'),
    ('JAVASCRIPT', 'javascript'),
    ('PYTHON', 'python'),
)

# Create your models here.

class Tag(models.Model):
    label = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.label

class Snippet(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="snippets")
    language = models.CharField(max_length=255, choices=LANGUAGE_CHOICES, default='PYTHON')
    title = models.CharField(max_length=255, blank=True, null=True)
    date_of_creation = models.DateField(auto_now_add=True)
    usage_description = models.CharField(max_length=255)
    code_text = models.TextField(max_length=1000, blank=True, null=True)
    labels = models.ManyToManyField(to=Tag, related_name="snippets")
    # use models.ForeignKey('self', on_delete=models.CASCADE) if I want to use
    # smaller snippets of code that refer back to a parent snippet

    def __str__(self):
        return self.title


