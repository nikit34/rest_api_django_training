from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django_filters import rest_framework as filters

from .serializers import TagSerializer
from tags.models import Tag


class TagFilter(filters.FilterSet):
    class Meta:
        model = Tag
        fields = {
            'title': ['icontains'],
            'timestamp': ['iexact', 'lte', 'gte']
        }


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    filterset_class = TagFilter

    @action(methods=['get'], detail=False)
    def newest(self, request):
        newest = self.get_queryset().order_by('timestamp').last()
        serializer = self.get_serializer_class()(newest)
        return Response(serializer.data)

    def get_queryset(self):
        return Tag.objects.filter(title__icontains='h1')