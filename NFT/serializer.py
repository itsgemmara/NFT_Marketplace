from rest_framework import serializers
from django.core.exceptions import ValidationError

from .models import NFT


class NFTSerializer(serializers.ModelSerializer):

    class Meta:
        model = NFT
        fields = ("name", "description", "File", "link", "blockchain_name", "sensitive", "supply")


class ShowNFTSerializer(serializers.ModelSerializer):

    class Meta:
        model = NFT
        fields = ("name", "File", "description", 'creator', 'owner', "supply", 'sensitive', "link", "blockchain_name",
                  'created_at', 'listed_at', )

