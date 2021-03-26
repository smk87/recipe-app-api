from rest_framework import serializers

from core.models import Tag


class TagSerializer(serializers.ModelSerializer):
    # Setializer for Tag object
    class Meta:
        model = Tag
        fields = ('id', 'name',)
        read_only_field = ('id',)
