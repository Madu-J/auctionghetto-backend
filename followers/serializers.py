from rest_framework import serializers
from .models import Follower


class FollowerSerializer(serializers.ModelSerializer):
    """
    Follower Serializer
    """

    owner = serializers.ReadOnlyField(source="owner.user")
    followed_name = serializers.ReadOnlyField(source="followed.user")

    class Meta:
        model = Follower
        fields = "__all__"
