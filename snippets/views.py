from django.views.generic import ListView, DetailView
from .models import Snippet


class SnippetListView(ListView):
    model = Snippet
    template_name = 'snippets/snippet_list.html'


class SnippetDetailView(DetailView):
    model = Snippet
    template_name = 'snippets/snippet_detail.html'