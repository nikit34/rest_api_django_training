from snippets.models import Snippet
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializers import SnippetSerializer


# class SnippetViewSet(viewsets.ViewSet):
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer

#     def list(self, request):
#         serializer = SnippetSerializer(self.queryset, many=True)
#         return Response(serializer.data)


class SnippetViewSet(viewsets.ModelViewSet):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    @action(methods=['get'], detail=False)
    def newest(self, request):
        newest = self.get_queryset().order_by('created').last()
        serializer = self.get_serializer_class()(newest)
        return Response(serializer.data)