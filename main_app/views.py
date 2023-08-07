from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Pokemon, BoosterPack
from .forms import AttackForm


# Create your views here.
def home(request):
    pokemon = Pokemon.objects.all()
    return render(request, "home.html", {"pokemon": pokemon})


def about(request):
    return render(request, "about.html")


def pokemon_index(request):
    pokemon = Pokemon.objects.all()
    return render(request, "pokemon/index.html", {"pokemon": pokemon})


def pokemon_detail(request, pokemon_id):
    pokemon = Pokemon.objects.get(id=pokemon_id)

    id_list = pokemon.boosterpacks.all().values_list("id")

    booster_pokemon_doesnt_have = BoosterPack.objects.exclude(id__in=id_list)
    attack_form = AttackForm()

    return render(
        request,
        "pokemon/detail.html",
        {
            "pokemon": pokemon,
            "attack_form": attack_form,
            "boosterpacks": booster_pokemon_doesnt_have,
        },
    )


def add_attack(request, pokemon_id):
    form = AttackForm(request.POST)
    if form.is_valid():
        new_attack = form.save(commit=False)
        new_attack.pokemon_id = pokemon_id
        new_attack.save()
    return redirect("detail", pokemon_id=pokemon_id)


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


class BoosterList(ListView):
    model = BoosterPack


class BoosterDetail(DetailView):
    model = BoosterPack


class BoosterCreate(CreateView):
    model = BoosterPack
    fields = "__all__"
    success_url = "/boosterPacks/"


class BoosterUpdate(UpdateView):
    model = BoosterPack
    fields = ["name", "year"]


class BoosterDelete(DeleteView):
    model = BoosterPack
    success_url = "/boosterPacks"


def assoc_booster(request, pokemon_id, booster_pack_id):
    Pokemon.objects.get(id=pokemon_id).boosterPack.add(booster_pack_id)
    return redirect("detail", pokemon_id=pokemon_id)


def unassoc_booster(request, pokemon_id, booster_pack_id):
    Pokemon.objects.get(id=pokemon_id).boosterPack.remove(booster_pack_id)
    return redirect("detail", pokemon_id=pokemon_id)
