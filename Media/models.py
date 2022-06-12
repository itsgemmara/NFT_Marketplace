from django.db import models


class File(models.Model):
    file = models.ImageField(upload_to='uploads/')
    FILE_CHOICES = [
        ('im', 'Image'),
        ('vd', 'Video'),
        ('3d', '3D Models'),
        ('ad', 'Audio'),
    ]
    type = models.CharField(max_length=2, choices=FILE_CHOICES)
    is_nft = models.BooleanField(default=False)

