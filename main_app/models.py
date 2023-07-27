from django.db import models
from django.urls import reverse


class Pokemon(models.Model):
    name = models.CharField(max_length=100)
    types = models.CharField(max_length=100)
    rarity = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    img = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f"{self.name} ({self.id})"

    def get_absolute_url(self):
        return reverse("detail", kwargs={"cat_id": self.id})


# pokemon = [
#   {'name': 'Venusaur-EX', 'types': 'Grass', 'rarity': 'Rare Holo EX', 'artist': 'Eske Yoshinob', 'img': 'https://images.pokemontcg.io/xy1/1_hires.png'},
#   {'name': 'Xerneas-EX', 'types': 'Fairy', 'rarity': 'Rare Ultra', 'artist': '5ban Graphics', 'img': 'https://images.pokemontcg.io/xy1/146_hires.png'},
#   {'name': 'Charizard-EX', 'types': 'Fire', 'rarity': 'Rare Ultra', 'artist': 'Ryo Ueda', 'img': 'https://images.pokemontcg.io/xy2/100_hires.png'},
#   {'name': 'M Lucario-EX', 'types': 'Fighting', 'rarity': 'Rare Holo EX', 'artist': '5ban Graphics', 'img': 'https://images.pokemontcg.io/xy3/55_hires.png'},
#   {'name': 'Magnezone-EX', 'types': 'Lightning', 'rarity': 'Rare Ultra', 'artist': 'Ryo Ueda', 'img': 'https://images.pokemontcg.io/xy2/101_hires.png'},
#   {'name': 'Toxicroak-EX', 'types': 'Psychic', 'rarity': 'Rare Ultra', 'artist': 'Ryo Ueda', 'img': 'https://images.pokemontcg.io/xy2/102_hires.png'},
# ]
