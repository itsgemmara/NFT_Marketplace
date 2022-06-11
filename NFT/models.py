from django.db import models

from Media.models import Video, Audio, TreeDModels, Image
from User.models import Profile


class Properties(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    prop_is_deleted = models.BooleanField(default=False)


class NFT(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.OneToOneField(Image, on_delete=models.DO_NOTHING, null=True, blank=True)
    video = models.OneToOneField(Video, on_delete=models.DO_NOTHING, null=True, blank=True)
    audio = models.OneToOneField(Audio, on_delete=models.DO_NOTHING, null=True, blank=True)
    treeD_models = models.OneToOneField(TreeDModels, on_delete=models.DO_NOTHING, null=True, blank=True)
    link = models.CharField(max_length=2048, null=True, blank=True)
    blockchain_name = models.CharField(max_length=50)  # choices?
    sensitive = models.BooleanField(default=False)
    supply = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_created=True)
    listed_at = models.DateTimeField(null=True, blank=True)
    nft_is_deleted = models.BooleanField(default=False)
    # creator = models.ForeignKey(Profile, on_delete=models.DO_NOTHING)
    # owner = models.ForeignKey(Profile, on_delete=models.DO_NOTHING)


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
    # taker = models.ManyToOneRel(Profile)
    # seller = models.ManyToOneRel(Profile)


class Collection(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.OneToOneField(Image, on_delete=models.DO_NOTHING, null=True, blank=True)
    video = models.OneToOneField(Video, on_delete=models.DO_NOTHING, null=True, blank=True)
    audio = models.OneToOneField(Audio, on_delete=models.DO_NOTHING, null=True, blank=True)
    NFTies = models.ForeignKey(NFT, on_delete=models.DO_NOTHING, related_name='collection_nft')
    collection_is_deleted = models.BooleanField(default=False)
