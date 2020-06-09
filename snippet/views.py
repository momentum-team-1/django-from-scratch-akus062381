  
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Tag
from .models import Snippet
from django.db.models import Q
from .forms import SnippetForm
from .forms import TagForm
from users.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def show_snippets(request):
    snippets = request.user.snippets.all()
    form = SnippetForm(data=request.POST)
    return render(request, 'snippet/show_snippets.html', {
        "snip_form": form,
        "snippets": snippets,
    })

@login_required
def home(request):
    return render(request, 'snippet/home.html')

@login_required
def snippet_detail(request, snippet_pk):
    snippet = get_object_or_404(request.user.snippets, pk=snippet_pk)
    return render(request, "snippet/snippet_detail.html", {"snippet": snippet})

@login_required
def new_snippet(request):
    if request.method == 'POST':
        form = SnippetForm(data=request.POST)
        if form.is_valid():
            snip = form.save(commit=False)
            snip.user = request.user
            snip.save()
            snip.set_tag_names(form.cleaned_data['tag_names'])
            return redirect(to='show_snippets')
    else:
        form = SnippetForm()
    
    return render(request, 'snippet/new_snippet.html', {
        'snip_form': form,
    })

@login_required
def edit_snippet(request, snippet_pk):
    snippet = get_object_or_404(request.user.snippets, pk=snippet_pk)

    if request.method == 'POST':
        form = SnippetForm(instance=snippet, data=request.POST)
        if form.is_valid():
            snippet = form.save()
            snippet.set_tag_names(form.cleaned_data['tag_names'])
            return redirect(to='snippet_detail', snippet_pk=snippet.pk)
    else:
        form = SnippetForm(instance=snippet, initial={"tag_names": snippet.tag_names()})
        
    return render(request, 'snippet/edit_snippet.html', { 'snip_form': form, 'snippet': snippet,})

@login_required
def delete_snippet(request, snippet_pk):
    snippet = get_object_or_404(request.user.snippets, pk=snippet_pk)

    if request.method == 'POST':
        snippet.delete()
        return redirect(to='show_snippets')
    
    return render(request, 'snippet/delete_snippet.html', { 'snippet': snippet })

@login_required
def view_tag(request, tag_name):
    tag = get_object_or_404(Tag, tag=tag_name)
    snippets = tag.snippets.filter(user=request.user)
    return render(request, 'snippet/tag_detail.html', {'tag': tag, 'snippets': snippets})

@login_required
def list_tags(request, tag_names):
    tags = request.user.tags.all()
    snippets = request.user.snippets.all()
    return render(request, 'snippet/list_tags.html', {'tags': tags, 'snippets': snippets})

@login_required
def search_snippets(request):
    
    query = request.GET.get('q')

    if query is not None:
        # change the below and add the piece to models.py
        snippets = Snippet.objects.filter(Q(title__icontains=query))
    else:
        snippets = []

    return render(request, "snippet/search_snippets.html", {
        "snippets": snippets, 
        "query": query
    })



