from django.http import HttpResponse
from django.shortcuts import render
from django.core.files.uploadedfile import SimpleUploadedFile
# Create your views here.
from .models import F, File
from NFT.models import NFT
from User.models import Profile


def create(request):
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
    return HttpResponse('done')