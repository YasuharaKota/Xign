from django.contrib import admin
from cms.models import *

# Register your models here.

admin.site.register(ArtistAlias)
admin.site.register(Artist)
admin.site.register(AliasToArtist)
admin.site.register(Music)

admin.site.register(Game)
admin.site.register(Difficulty)
admin.site.register(Level)
admin.site.register(ChartConstantToLevel)

admin.site.register(ChartCreatorAlias)
admin.site.register(ChartCreator)
admin.site.register(ChartAliasToCreator)
admin.site.register(Chart)