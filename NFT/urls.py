from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .api import *

nft_router = DefaultRouter()
nft_router.register(r'nft-view-set', NFTViewSet, basename='nft')

urlpatterns = [
    path('nfties/', include(nft_router.urls)),

]