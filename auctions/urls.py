from django.urls import path
from auctions import views

urlpatterns = [
    path('auctions/', views.AuctionList.as_view()),
    path("auctions/<int:pk>/", views.AuctionDetails.as_view()),
]