from django.db.models import Count
from rest_framework import generics, filters, permissions
from django_filters.rest_framework import DjangoFilterBackend
from auctionghetto_api.permissions import IsOwnerOrReadOnly
from .models import Auctioneer
from .serializers import AuctioneerSerializer


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user


class AuctioneerList(generics.ListAPIView):
    """
    Auctioneer list for logged in.

    """
    serializer_class = AuctioneerSerializer
    queryset = Auctioneer.objects.annotate(
        auctions_count=Count("owner__auction", distinct=True),
        followers_count=Count("owner__followed", distinct=True),
        following_count=Count("owner__following", distinct=True),
    ).order_by("-created_at")
    filter_backends = [
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        "owner__following__followed__auctioneer",
        "owner__followed__owner__auctioneer",
    ]
    ordering_fields = [
        "auctions_count",
        "followers_count",
        "following_count",
        "owner__following__created_at",
        "owner__followed__created_at",
    ]


class AuctioneerDetails(generics.RetrieveUpdateAPIView):
    """
    Auctioneer details is used for editing or deleting profiles.
    """
    serializer_class = AuctioneerSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Auctioneer.objects.annotate(
        auctions_count=Count("owner__auction", distinct=True),
        followers_count=Count("owner__followed", distinct=True),
        following_count=Count("owner__following", distinct=True),
    ).order_by("-created_at")
