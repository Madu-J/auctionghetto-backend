from django.urls import path
from auctions import views

urlpatterns = [
    path('auctions/', views.AuctionList.as_view()),
]