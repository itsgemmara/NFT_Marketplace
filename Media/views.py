from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.test import APITestCase, APITransactionTestCase, APIClient
from rest_framework import status
from django.core.files.uploadedfile import SimpleUploadedFile

from Media.models import File
from User.models import Profile
from NFT.models import NFT, NFTHistory, Collection, Properties
from NFT.serializer import NFTSerializer, ShowNFTSerializer
from NFT.api import NFTViewSet
from django.core.files.uploadedfile import SimpleUploadedFile
# Create your views here.
from .models import F, File
from NFT.models import NFT
from User.models import Profile


class Create(APITestCase):

    def create(self):
        person = Profile.objects.get(pk=1)
        photo = open('uploads/c704a9ba-c6c1-4275-a929-a85cef6d453b.jpg', 'rb')
        vid = open('uploads/Friends.S1.E1.480p.mp4', 'rb')
        video = SimpleUploadedFile(vid.name, photo.read())
        photo = SimpleUploadedFile(photo.name, photo.read())
        file = File.objects.create(file=photo, type='im', is_nft=False)
        file_nft = File.objects.create(file=photo, type='im', is_nft=True)
        vid = File.objects.create(file=video, type='im', is_nft=False)
        nft = NFT.objects.create(name="name", description="description", link="link",
                                 blockchain_name="blockchain_name", sensitive=True, supply=2, creator=person, owner=person)
        nft.File.set([file, file_nft, vid])
        print(type(photo))

        # _photo = open('uploads/c704a9ba-c6c1-4275-a929-a85cef6d453b.jpg', 'rb')
        # self.photo = SimpleUploadedFile(_photo.name, _photo.read())
        # _video = open('uploads/Friends.S1.E1.480p.mp4', 'rb')
        # self.video = SimpleUploadedFile(_video.name, _video.read())
        # file_nft = File.objects.create(file=self.photo, type='im', is_nft=True)
        # extra_img = File.objects.create(file=self.photo, type='im', is_nft=False)
        # self.video = File.objects.create(file=self.video, type='vd', is_nft=False)
        # person = Profile.objects.create(phone_number="048481", password='mmmmm1234')
        # self.client = CustomAPIClient
        #
        # self.data = {
        #     "name": "name",
        #     "File": [file_nft, ],
        #     "description": "s",
        #     "creator": person,
        #     "owner": person,
        #     "supply": 1,
        #     "sensitive": True,
        #     "link": "link",
        #     "blockchain_name": "blockchain_name",
        # }
        #
        # response = self.client.post("/nft/nfts/nft-viewset//", self.data)
        # self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        return HttpResponse('done')
        #
        #

