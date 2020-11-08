from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django_filters import rest_framework as filters

from .serializers import AuthorSerializer
from authors.models import Author


class AuthorFilter(filters.FilterSet):
    class Meta:
        model = Author
        fields = {
            'full_name': ['icontains'],
            'born': ['iexact', 'lte', 'gte'],
        }


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    filterset_class = AuthorFilter

    @action(methods=['get'], detail=False)
    def newest(self, request):
        newest = self.get_queryset().order_by('timestamp').last()
        serializer = self.get_serializer_class()(newest)
        return Response(serializer.data)

    def get_queryset(self):
        return Author.objects.filter(full_name__icontains='h1')