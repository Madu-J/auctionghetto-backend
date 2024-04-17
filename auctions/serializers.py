from rest_framework import serializers
from .models import Auctions
from bookmarks.models import Bookmark

class AuctionsSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source="owner.profile.id")
    profile_image = serializers.ReadOnlyField(
        source="owner.profile.image.url"
        )
    bookmark_id = serializers.SerializerMethodField()

    def validate_image(self, value):
        if value.size > 4096 * 4096 * 2:
            raise serializers.ValidationError(
                "Image size larger than 2mb"
                )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                "Image width too large"
                )
        if value.image.height > 4096:
            raise serializers.ValidationError(
                "Image height too large"
                )
            return value

    def get_is_owner(self, obj):
        request = self.context["request"]
        return request.user == obj.owner

    def get_bookmark_id(self, obj):
        user = self.context["request"].user
        if user.is_authenticated:
            bookmark = Bookmark.objects.filter(
                owner=user, auctions=obj
            ).first()
            return bookmark.id if bookmark else None
        return None

    class Meta:
        model = Auctions
        fields = "__all__"