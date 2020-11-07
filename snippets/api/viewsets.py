from snippets.models import Snippet
from .serializers import SnippetSerializer
from rest_framework import viewsets
from rest_framework.response import Response


# class SnippetViewSet(viewsets.ViewSet):
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer

#     def list(self, request):
#         serializer = SnippetSerializer(self.queryset, many=True)
#         return Response(serializer.data)


class SnippetViewSet(viewsets.ModelViewSet):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer