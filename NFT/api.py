from rest_framework import mixins
from rest_framework import viewsets
from rest_framework import permissions

from .serializer import *
from .models import NFT
from .permissions import NFTIsOwner


class NFTViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet,
                   ):
    """
    General ViewSet description
    list: List NFT
    retrieve: Retrieve NFT
    update: Update NFT
    create: Create NFT
    partial_update: Patch NFT
    """
    queryset = NFT.objects.all()
    serializer_class = NFTSerializer

    def get_serializer_class(self):
        if self.action == 'create' or self.action == 'update' or self.action == 'partial_update':
            return NFTSerializer
        elif self.action == 'list' or self.action == 'retrieve':
            return ShowNFTSerializer
        return NFTSerializer

    def get_queryset(self):
        return self.queryset.filter(nft_is_deleted=False)

    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [permissions.IsAuthenticated(), ]
            return permission_classes
        elif self.action == 'update' or self.action == 'partial_update':
            permission_classes = [permissions.IsAuthenticated(), NFTIsOwner()]
            return permission_classes
        return [permissions.AllowAny()]


