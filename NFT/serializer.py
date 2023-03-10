from rest_framework import serializers
from django.core.exceptions import ValidationError


from .models import NFT


class NFTSerializer(serializers.ModelSerializer):

    def validate(self, validated_data):
        count = 0
        for file in validated_data['File']:
            if not file.is_nft:
                count += 1
            if count == len(validated_data['File']):
                raise ValidationError('Specify the NFT file.')
        return validated_data

    def create(self, validated_data):
        request = self.context.get('request', None)
        if request:
            validated_data['owner'] = request.user
            validated_data['creator'] = request.user
        return super().create(validated_data)

    class Meta:
        model = NFT
        fields = ("name", "description", "File", "link", "blockchain_name", "sensitive", "supply")


class ShowNFTSerializer(serializers.ModelSerializer):

    class Meta:
        model = NFT
        fields = ("name", "File", "description", 'creator', 'owner', "supply", 'sensitive', "link", "blockchain_name",
                  'created_at', 'listed_at', 'pk', )



