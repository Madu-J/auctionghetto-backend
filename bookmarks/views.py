from rest_framework import generics, permissions
from bookmarks.models import Bookmark
from .serializers import BookmarkSerializer
from auctionghetto_api.permissions import IsOwnerOrReadOnly


class BookmarkList(generics.ListCreateAPIView):
    """
    Bookmark list for logged in user.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = BookmarkSerializer
    queryset = Bookmark.objects.all()

    def get_or_create(self, serializer):
        serializer.bookmark(owner=self.request.user)


class BookmarkDetails(generics.RetrieveDestroyAPIView):
    """
    Retrieve bookmarked by its owners id.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = BookmarkSerializer
    queryset = Bookmark.objects.all()