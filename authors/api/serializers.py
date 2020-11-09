from rest_framework import serializers

from authors.models import Author
from tags.models import Tag


class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'full_name', 'short_name', 'born')


class StatisticSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('title', 'timestamp', 'active', 'products')