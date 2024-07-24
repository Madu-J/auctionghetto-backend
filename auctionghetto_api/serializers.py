from dj_rest_auth.serializers import UserDetailsSerializer
from rest_framework import serializers


class CurrentUserSerializer(UserDetailsSerializer):
    auctioneer_id = serializers.ReadOnlyField(source='auctioneer.id')
    auctioneer_image = serializers.ReadOnlyField(source='auctioneer.image.url')

    class Meta(UserDetailsSerializer.Meta):
        fields = UserDetailsSerializer.Meta.fields + (
            'auctioneer_id', 'auctioneer_image'
        )

