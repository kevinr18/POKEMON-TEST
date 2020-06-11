from django.urls import path

from .views import RegionsList, RegionsDetails
from pokemon import views

urlpatterns = [
    path('pokemons/<int:pk>/', views.PokemonsDetails.as_view()),
    path('pokemons/own/', views.StorageList.as_view()),
    path('pokemons/own/<int:pk>/', views.StorageDetails.as_view()),
    path('pokemons/own/party/', views.StorageParty.as_view()),
    path('regions/', views.RegionsList.as_view()),
    path('regions/<int:pk>/', views.RegionsDetails.as_view()),
    path('location/<int:pk>/', views.LocationsDetails.as_view()),
    path('areas/<int:pk>/', views.AreasDetails.as_view()),

    
]
