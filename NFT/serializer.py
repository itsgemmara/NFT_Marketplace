from rest_framework import serializers
from django.core.exceptions import ValidationError

from .models import NFT


class NFTSerializer(serializers.ModelSerializer):

    class Meta:
        model = NFT
        fields = ("name", "description", "image", "video", "audio",
                  "treeD_models", "link", "blockchain_name", "sensitive", "supply")


class NFTListSerializer(serializers.ModelSerializer):

    class Meta:
        model = NFT
        fields = ("name", "image", "video", "audio", "treeD_models")

