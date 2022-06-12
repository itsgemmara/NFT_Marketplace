from django.db import models

from Media.models import File
from User.models import Profile


class Properties(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    prop_is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class NFT(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    File = models.ManyToManyField(File)
    link = models.CharField(max_length=2048, null=True, blank=True)
    blockchain_name = models.CharField(max_length=50)  # choices?
    sensitive = models.BooleanField(default=False)
    supply = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now=True)
    listed_at = models.DateTimeField(null=True, blank=True)
    nft_is_deleted = models.BooleanField(default=False)
    prop = models.ManyToManyField(Properties)
    creator = models.ForeignKey(Profile, on_delete=models.DO_NOTHING, related_name='nft_creator_profile')
    owner = models.ForeignKey(Profile, on_delete=models.DO_NOTHING, related_name='nft_owner_profile')

    def __str__(self):
        return self.name


class NFTHistory(models.Model):
    nft_id = models.TextField()
    date = models.DateTimeField(auto_created=True)
    nft_history_is_deleted = models.BooleanField(default=False)
    TYPE_CHOICES = [
        ('b', 'buy'),
        ('s', 'sell'),
    ]
    type = models.CharField(max_length=1, choices=TYPE_CHOICES)
    price = models.CharField(max_length=255)
    taker = models.ForeignKey(Profile, on_delete=models.DO_NOTHING, related_name='nft_taker_profile')
    seller = models.ForeignKey(Profile, on_delete=models.DO_NOTHING, related_name='nft_seller_profile')

    def __str__(self):
        return self.nft_id


class Collection(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    File = models.ManyToManyField(File)
    NFTies = models.ManyToManyField(NFT)
    collection_is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name
