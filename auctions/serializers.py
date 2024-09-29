from rest_framework import serializers
from .models import Auction
from bookmarks.models import Bookmark


class AuctionSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")
    is_owner = serializers.SerializerMethodField()
    auctioneer_id = serializers.ReadOnlyField(source="owner.auctioneer.id")
    auctioneer_image = serializers.ReadOnlyField(
        source="owner.auctioneer.image.url"
        )
    bookmark_id = serializers.SerializerMethodField()

    def validate_image(self, value):
        print(f"Received image size: {value.size}")
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
                owner=user, auction=obj
            ).first()
            return bookmark.id if bookmark else None
        return None

    def save(self, **kwargs):
        image = self.validated_data.get('image', None)
        if image:
            print(f"Image is being saved: {image}")  
        super().save(**kwargs)

    class Meta:
        model = Auction
        # fields = "__all__"
        fields = [
            'id',
            'owner',
            'is_owner',
            'image',
            'updated_at',
            'title',
            'categories',
            'products',
            'auctionday',
            'description',
            'year',
            'price',
            'auctioneer_id',
            'auctioneer_image',
            'bookmark_id'
        ]
