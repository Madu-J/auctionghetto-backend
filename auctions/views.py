from django.db.models import Count
from rest_framework import generics, filters, permissions
from django_filters.rest_framework import DjangoFilterBackend
from auctionghetto_api.permissions import IsOwnerOrReadOnly
from .models import Auction
from .serializers import AuctionSerializer


class AuctionList(generics.ListCreateAPIView):
    """
    Auction list for logged in users.
    """
    serializer_class = AuctionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Auction.objects.all()

    filter_backends = [
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        "owner__followed__owner__auctioneer",
        "bookmarks__owner__auctioneer",
        "owner__auctioneer",
    ]
    search_fields = [
         "title",
        "owner__username",
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class AuctionDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    Detail view for user post, update or delete item.
    """
    serializer_class = AuctionSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Auction.objects.all()
