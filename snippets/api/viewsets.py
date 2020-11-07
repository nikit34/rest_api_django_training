from snippets.models import Snippets
from .serializers import SnippetSerializer
from rest_framework import viewsets


class SnippetViewSet(viewsets.ModelViewSet):
    queryset = Snippets.objects.all()
    serializer_class = SnippetSerializer