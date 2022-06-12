from django.contrib import admin

from .models import NFT, Collection, NFTHistory, Properties

admin.site.register(NFT)
admin.site.register(Collection)
admin.site.register(NFTHistory)
admin.site.register(Properties)