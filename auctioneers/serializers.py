from rest_framework import serializers
from .models import Auctioneer
from followers.models import Follower


class AuctioneerSerializer(serializers.ModelSerializer):
    """
    Auctioneer serializer
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    following_id = serializers.SerializerMethodField()
    auctions_count = serializers.ReadOnlyField()
    followers_count = serializers.ReadOnlyField()
    following_count = serializers.ReadOnlyField()

    def get_is_owner(self, obj):
        request = self.context["request"]
        return request.user == obj.owner

    def get_following_id(self, obj):
        user = self.context["request"].user
        if user.is_authenticated:
            following = Follower.objects.filter(
                owner=user, followed=obj.owner
                ).first()
            return following.id if following else None
        return None

    class Meta:
        model = Auctioneer
        fields = "__all__"
