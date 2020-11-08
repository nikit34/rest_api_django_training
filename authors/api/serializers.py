from rest_framework import serializers

from authors.models import Author


class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'full_name', 'short_name', 'born')