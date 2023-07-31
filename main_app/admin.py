from django.contrib import admin
from .models import Pokemon, Attack, BoosterPack

# Register your models here.

admin.site.register(Pokemon)
admin.site.register(Attack)
admin.site.register(BoosterPack)
