from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Pokemon
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
    attack_form = AttackForm()

    return render(
        request, "pokemon/detail.html", {"pokemon": pokemon, "attack_form": attack_form}
    )


def add_attack(request, pokemon_id):
    form = AttackForm(request.POST)
    if form.is_valid():
        new_attack = form.save(commit=False)
        new_attack.cat_id = pokemon_id
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
