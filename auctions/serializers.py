from rest_framework import serializers
from .models import Auctions


class AuctionsSerializer(serializers.models):
    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = Auctions
        field = __all__