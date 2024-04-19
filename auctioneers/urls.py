from django.urls import path
from auctioneers import views

urlpatterns = [
    path('auctioneers/', views.AuctioneerList.as_view()),
     path("auctioneers/<int:pk>/", views.AuctioneerDetails.as_view()),
]