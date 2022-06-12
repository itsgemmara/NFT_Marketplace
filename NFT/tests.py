from rest_framework.test import APITestCase, APITransactionTestCase, APIClient
from rest_framework import status
from django.core.files.uploadedfile import SimpleUploadedFile

from Media.models import File
from User.models import Profile
from .models import NFT, NFTHistory, Collection, Properties
from .serializer import NFTSerializer, ShowNFTSerializer
from .api import NFTViewSet


class NFTTestCase(APITestCase):

    def setUp(self):
        _photo = open('uploads/c704a9ba-c6c1-4275-a929-a85cef6d453b.jpg', 'rb')
        self.photo = SimpleUploadedFile(_photo.name, _photo.read())
        _video = open('uploads/Friends.S1.E1.480p.mp4', 'rb')
        self.video = SimpleUploadedFile(_video.name, _video.read())
        self.file_nft = File.objects.create(file=self.photo, type='im', is_nft=True)
        self.extra_img = File.objects.create(file=self.photo, type='im', is_nft=False)
        self.video = File.objects.create(file=self.video, type='vd', is_nft=False)
        person = Profile.objects.create(phone_number="0913", password='mmmmm1234')

        self.data = {
    "name": "y",
    "File": [],
    "description": "s",
    "creator": person,
    "owner": person,
    "supply": 1,
    "sensitive": True,
    "link": "f",
    "blockchain_name": "d",
}

    def test_create_nft(self):
        # with only nft file
        self.data['File'] = [self.file_nft]
        response = self.client.post("/nft/nfts/nft-viewset//", self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
