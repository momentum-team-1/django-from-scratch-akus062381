from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Tag
from .models import Snippet
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
    snippet = get_object_or_404(request.user.snippet, pk=snippet_pk)
    return render(request, "snippet/snippet_detail.html", {"snippet": snippet})

@login_required
def new_snippet(request):
    if request.method == 'POST':
        form = SnippetForm(data=request.POST)
        if form.is_valid():
            snip = form.save(commit=False)
            snip.user = request.user
            snip.save()
            return redirect(to='show_snippets', snippet_pk=snippet.pk)
    else:
        form = SnippetForm()
    
    return render(request, 'snippet/new_snippet.html', {
        'snip_form': form,
    })







