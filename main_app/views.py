from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Pokemon

# pokemon = [
#   {'name': 'Venusaur-EX', 'types': 'Grass', 'rarity': 'Rare Holo EX', 'artist': 'Eske Yoshinob', 'img': 'https://images.pokemontcg.io/xy1/1_hires.png'},
#   {'name': 'Xerneas-EX', 'types': 'Fairy', 'rarity': 'Rare Ultra', 'artist': '5ban Graphics', 'img': 'https://images.pokemontcg.io/xy1/146_hires.png'},
#   {'name': 'Charizard-EX', 'types': 'Fire', 'rarity': 'Rare Ultra', 'artist': 'Ryo Ueda', 'img': 'https://images.pokemontcg.io/xy2/100_hires.png'},
#   {'name': 'M Lucario-EX', 'types': 'Fighting', 'rarity': 'Rare Holo EX', 'artist': '5ban Graphics', 'img': 'https://images.pokemontcg.io/xy3/55_hires.png'},
#   {'name': 'Magnezone-EX', 'types': 'Lightning', 'rarity': 'Rare Ultra', 'artist': 'Ryo Ueda', 'img': 'https://images.pokemontcg.io/xy2/101_hires.png'},
#   {'name': 'Toxicroak-EX', 'types': 'Psychic', 'rarity': 'Rare Ultra', 'artist': 'Ryo Ueda', 'img': 'https://images.pokemontcg.io/xy2/102_hires.png'},
# ]


# Create your views here.
def home(request):
    pokemon = Pokemon.objects.all()
    return render(request, "home.html", {"pokemon": pokemon})


def about(request):
    return render(request, "about.html")


def pokemon_index(request):
    pokemon = Pokemon.objects.all()
    return render(request, "pokemon/index.html", {"pokemon": pokemon})


def pokemon_detail(request, cat_id):
    pokemon = Pokemon.objects.get(id=cat_id)
    return render(request, "pokemon/detail.html", {"pokemon": pokemon})


class PokemonCreate(CreateView):
    model = Pokemon
    fields = "__all__"
    # success_url = "/pokemon/"


class PokemonUpdate(UpdateView):
    model = Pokemon
    fields = "__all__"
    # success_url = "/pokemon/"


class PokemonDelete(DeleteView):
    model = Pokemon
    fields = "__all__"
    success_url = "/pokemon/"
