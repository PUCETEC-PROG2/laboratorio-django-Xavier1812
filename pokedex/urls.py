from django.urls import path
from . import views

app_name = 'pokedex'

urlpatterns = [
    path("", views.index, name="index"),
    path("pokemon/<int:pokemon_id>/", views.pokemon, name="pokemon"),
    path("trainer/<int:trainer_id>", views.trainer, name="trainer"),
    path("add_pokemon/", views.add_pokemon, name="add_pokemon"),
    path("edit_pokemon/<int:pokemon_id>/", views.edit_pokemon, name="edit_pokemon"),
    path("trainers", views.trainers, name="trainers"),
]