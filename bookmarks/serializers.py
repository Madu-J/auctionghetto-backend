from django.db import IntegrityError
from rest_framework import serializers
from .models import Bookmark


class BookmarkSerializer(serializers.ModelSerializer):
    """
    Bookmark Serializer
    """
    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = Bookmark
        fields = ['id', 'owner', 'auction', 'created_at']

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({"detail: possible duplicate"})
