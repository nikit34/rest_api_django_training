from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from django_filters import rest_framework as filters

from .serializers import AuthorSerializer, StatisticSerializer
from authors.models import Author
from tags.models import Tag
from tags.api.viewsets import TagFilter


class AuthorFilter(filters.FilterSet):
    class Meta:
        model = Author
        fields = {
            'full_name': ['icontains'],
            'born': ['iexact', 'lte', 'gte'],
        }


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.filter(id='1')
    serializer_class = AuthorSerializer
    authentication_classes = (TokenAuthentication,)
    filterset_class = AuthorFilter

    @action(methods=['get'], detail=False)
    def newest(self):
        newest = self.get_queryset().order_by('timestamp').last()
        serializer = self.get_serializer_class()(newest)
        return Response(serializer.data)

    def get_queryset(self):
        return Author.objects.all()


class StatisticViewSet(ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = StatisticSerializer
    authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    filterset_class = TagFilter
    lookup_field = 'title'

    @action(methods=['get'], detail=False)
    def stat(self, request, *args, **kwargs):
        stat = self.queryset.order_by('title')
        serializer = StatisticSerializer(stat, many=True)
        return Response(serializer.data)
