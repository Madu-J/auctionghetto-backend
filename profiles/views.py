from django.db.models import Count
from rest_framework import generics, filters, permissions
from django_filters.rest_framework import DjangoFilterBackend
from auctionghetto_api.permissions import IsOwnerOrReadOnly
from .models import Profile
from .serializers import ProfileSerializer


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user


class ProfileList(generics.ListAPIView):
    """
    Profile list for logged in user.

    """
    serializer_class = ProfileSerializer
    queryset = Profile.objects.annotate(
        auctions_count=Count("owner__auctions", distinct=True),
        followers_count=Count("owner__followed", distinct=True),
        following_count=Count("owner__following", distinct=True),
    ).order_by("-created_at")
    filter_backends = [
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        "owner__following__followed__profile",
        "owner__followed__owner__profile",
    ]
    ordering_fields = [
        "auctions_count",
        "followers_count",
        "following_count",
        "owner__following__created_at",
        "owner__followed__created_at",
    ]

class ProfileDetails(generics.RetrieveUpdateAPIView):
    """
    Profile details allows users to edit or delete their profiles.
    """
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.annotate(
        auctions_count=Count("owner__auction", distinct=True),
        followers_count=Count("owner__followed", distinct=True),
        following_count=Count("owner__following", distinct=True),
    ).order_by("-created_at")