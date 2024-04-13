from rest_framework.views import APIView
from rest_framework.response import Response
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
        "saved__owner__profile",
        "owner__profile",
    ]
    search_fields = [
        "owner__username",
        "title",
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

