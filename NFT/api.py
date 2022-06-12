from rest_framework import mixins
from rest_framework import viewsets

from .serializer import *
from .models import NFT


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
        if self.action == 'create' or self.action == 'update' or self.action == 'partial_update' or\
                self.action == 'retrieve':
            return NFTSerializer
        elif self.action == 'list':
            return NFTListSerializer
        return NFTSerializer


