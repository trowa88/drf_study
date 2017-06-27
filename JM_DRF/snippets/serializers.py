from rest_framework import serializers

from snippets.models import LANGUAGE_CHOICE, STYLE_CHOICE, Snippet


class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ('id', 'title', 'code', 'linenos', 'language', 'style')
