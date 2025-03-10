from django.urls import path
from . import views

app_name = 'pokedex'

urlpatterns = [
    path("", views.index, name="index"),
    path("pokemon/<int:pokemon_id>/", views.pokemon, name="pokemon"),
    path("add_pokemon/", views.add_pokemon, name="add_pokemon"),
    path("edit_pokemon/<int:pokemon_id>/", views.edit_pokemon, name="edit_pokemon"),
    path("delete_pokemon/<int:pokemon_id>/", views.delete_pokemon, name="delete_pokemon"),
    path("trainers/", views.trainers, name="trainers"),
    path("trainers/trainer/<int:trainer_id>", views.trainer, name="trainer"),
    path("add_trainer/", views.add_trainer, name="add_trainer"),
    path("trainers/edit_trainer/<int:trainer_id>/", views.edit_trainer, name="edit_trainer"),
    path("trainers/delete_trainer/<int:trainer_id>/", views.delete_trainer, name="delete_trainer"),
    path("login/", views.CustomLoginView.as_view(), name="login"),
]
