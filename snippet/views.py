from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Tag
from .models import Snippet

# Create your views here.

def show_snippets(request):
    snippets = Snippet.objects.all()
    return render(request, "snippet/show_snippets.html", {
        "snippets": snippets
    })

def index(request):
    
    return render(request, 'snippet/index.html')


def new_snippet(request):
    if request.method == 'GET':
        form = SnippetForm()
    else:
        form = SnippetForm()(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='show_snippets')
    
    return render(request, "snippet/new_snippet.html", {"form": form})





