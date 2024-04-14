from django.urls import path
from bookmarks import views

urlpatterns = [
    path("bookmarks/", views.BookmarkList.as_view()),
    path("bookmarks/<int:pk>/", views.BookmarkDetails.as_view()),
]
