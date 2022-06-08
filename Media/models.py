from django.db import models


class Audio(models.Model):
    audio = models.FileField(upload_to='uploads/')


class Image(models.Model):
    image = models.ImageField(upload_to='uploads/')


class Video(models.Model):
    video = models.FileField(upload_to='uploads/')


class TreeDModels (models.Model):
    treeD_models = models.FileField(upload_to='uploads/')

