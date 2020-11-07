from rest_framework import serializers
from snippets.model import Snippet


class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Snippet
        fields = ('title', 'body', 'created')