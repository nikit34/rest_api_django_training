from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django_filters import rest_framework as filters

from .serializers import BookSerializer
from books.models import Book


class BookFilter(filters.FilterSet):
    class Meta:
        model = Book
        fields = {
            'title': ['icontains'],
            'created': ['iexact', 'lte', 'gte']
        }


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    filterset_class = BookFilter

    @action(methods=['get'], detail=False)
    def newest(self, request):
        newest = self.get_queryset().order_by('created').last()
        serializer = self.get_serializer_class()(newest)
        return Response(serializer.data)

    def get_queryset(self):
        return Book.objects.filter(title__icontains='h1')