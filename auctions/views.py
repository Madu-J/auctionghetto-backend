from rest_framework.views import APIView, filters, permissions
from django_filters.rest_framework import DjangoFilterBackend
from auctionghetto_api.permissions import IsOwnerOrReadOnly
from .models import Auctions
from .serializers import AuctionsSerializer


class AuctionList(APIView):
    """
    Auction list for logged in users.
    """
    serializer_class = AuctionsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Actions.objects.all()

    filter_backends = [
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        "owner__followed__owner__profile",
        "owner__profile",
    ]
    search_fields = [
        "owner__username",
        "title",
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class AuctionDetails(APIView):
    """
    Detail view for user post, update or delete item.
    """
    serializer_class = AuctionsSerializer
    permission_classes = [IsOwnerReadOnly]
    queryset = Auctions.objects.all()
