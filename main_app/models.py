from django.db import models
from django.urls import reverse

TYPES = (
    ("F", "Fire"),
    ("G", "Grass"),
    ("W", "Water"),
    ("L", "Lightning"),
    ("P", "Psychic"),
    ("C", "Colorless"),
    ("D", "Darkness"),
    ("M", "Metal"),
    ("DR", "Dragon"),
    ("F", "Fairy"),
    ("FG", "Fighting"),
)


class BoosterPack(models.Model):
    name = models.CharField(max_length=100)
    year = models.IntegerField()

    def __str__(self):
        return f"{self.name} ({self.year})"

    def get_absolute_url(self):
        return reverse("boosterpacks_detail", kwargs={"pk": self.id})


class Pokemon(models.Model):
    names = models.CharField(max_length=100)
    types = models.CharField(max_length=100)
    rarity = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    img = models.CharField(max_length=100)

    BoosterPacks = models.ManyToManyField(BoosterPack)

    def __str__(self) -> str:
        return f"{self.names} ({self.id})"

    def get_absolute_url(self):
        return reverse("detail", kwargs={"cat_id": self.id})


class Attack(models.Model):
    names = models.CharField(max_length=100, default="Nameless")
    types = models.CharField(max_length=2, choices=TYPES, default=TYPES[0][0])
    description = models.TextField(max_length=250, default="None")
    cost = models.IntegerField(default=1)
    damage = models.IntegerField(default=20)

    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)

    def __str__(self):
        return (
            f"{self.names} is {self.get_types_display()} type with {self.damage} attack"
        )
