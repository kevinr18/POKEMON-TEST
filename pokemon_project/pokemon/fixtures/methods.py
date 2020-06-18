from django.shortcuts import render
from django.http import Http404
import json
import string

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token

from .models import Pokemons, Storage, Regions, Locations, Areas
from .serializer import PokemonsSerializer, StorageSerializer, StoragePostSerializer, RegionsSerializer, AreasSerializer
from .serializer import LocationsSerializer , RegionsListSerializer


class chargeDataRegions():
    with open('pokemon/fixtures/regions.json') as file:
        data = json.load(file)
        elemento = []
        norepetido = True
        for region in data['data']:
            print('name:', region['name'])
            region_obj = Regions()
            region_obj.name = region['name']
            ser = RegionsListSerializer(region_obj)
            serializer = RegionsListSerializer(region_obj, data = ser.data)
            if serializer.is_valid():
                serializer.save()
            else:
                print(serializer.errors)
        

class chargeDataLocations():
    with open('pokemon/fixtures/regions.json') as file:
        data = json.load(file)
        elemento = []
        norepetido = True
        i=0;
        for region in data['data']:
            print('name:', region['name'])
            i = i+1
            for a in region['locations']:
                locations = Locations()
                locations.name = a
                region = Regions()
                region.id = i;
                locations.id_regions = region
                ser = LocationsListSerializer(locations)
                
                serializer = LocationsListSerializer(locations, data = ser.data)
                if serializer.is_valid():
                    serializer.save()
                else:
                    print(serializer.errors)
                
                #print(LocationsListSerializer(locations).data)
            print('')

class chargeDataAreas():
    with open('pokemon/fixtures/areas.json') as file:
        data = json.load(file)
        for area in data['data']:
            location_obj = Locations.objects.get(name = area['location'])
            areas = Areas()
            areas.name = area['name']
            areas.id_locations = location_obj
            ser = AreasListSerializer(areas)
            serializer = AreasListSerializer(areas, data = ser.data)
            if serializer.is_valid():
                serializer.save()
            else:
                print(serializer.errors)
               
                
                #print(LocationsListSerializer(locations).data)
            print('')


class chargeDataMoves():
    with open('pokemon/fixtures/pokemons.json') as file:
        data = json.load(file)
        elemento = []
        norepetido = True
        for pokemon in data['data']:
            for a in pokemon['moves']:
                if elemento:
                    for b in elemento:
                        if(a == b):
                            norepetido = False
                            break
                        else:
                            norepetido = True
                    if norepetido:
                        elemento.append(a)
                else:
                    elemento = [a]
               
            #print('')

        MovesList = [];
        for c in elemento:
            moves_obj = Moves()
            moves_obj.move = c
            MovesList.append(moves_obj)
            #print(c)
        for d in MovesList:
            ser = MovesSerializer(d)
            print(ser.data)
            serializer = MovesSerializer(d, data = ser.data)
            if serializer.is_valid():
                serializer.save()
            else:
                print(serializer.errors)

class chargeDataAbilities():
    with open('pokemon/fixtures/pokemons.json') as file:
        data = json.load(file)
        elemento = []
        norepetido = True
        for pokemon in data['data']:
            for a in pokemon['abilities']:
                if elemento:
                    for b in elemento:
                        if(a == b):
                            norepetido = False
                            break
                        else:
                            norepetido = True
                    if norepetido:
                        elemento.append(a)
                else:
                    elemento = [a]
               
            #print('')

        AbilitiesList = [];
        for c in elemento:
            abilities_obj = Abilities()
            abilities_obj.ability = c
            AbilitiesList.append(abilities_obj)
            #print(c)
        for d in AbilitiesList:
            ser = AbilitiesSerializer(d)
            print(ser.data)
            serializer = AbilitiesSerializer(d, data = ser.data)
            if serializer.is_valid():
                serializer.save()
            else:
                print(serializer.errors)

class chargeDataTypes():
    with open('pokemon/fixtures/pokemons.json') as file:
        data = json.load(file)
        elemento = []
        norepetido = True
        for pokemon in data['data']:
            for a in pokemon['types']:
                if elemento:
                    for b in elemento:
                        if(a == b):
                            norepetido = False
                            break
                        else:
                            norepetido = True
                    if norepetido:
                        elemento.append(a)
                else:
                    elemento = [a]
               
            #print('')

        TypeList = [];
        for c in elemento:
            type_obj = Types()
            type_obj.type = c
            TypeList.append(type_obj)
            #print(c)
        for d in TypeList:
            ser = TypesSerializer(d)
            print(ser.data)
            serializer = TypesSerializer(d, data = ser.data)
            if serializer.is_valid():
                serializer.save()
            else:
                print(serializer.errors)


class chargeDataSprites():
    with open('pokemon/fixtures/pokemons.json') as file:
        data = json.load(file)
        elemento = []
        norepetido = True
        for pokemon in data['data']:
           # print(pokemon['sprites']['back_default'])
            sprite_obj = Sprites()
            sprite_obj.back_default = pokemon['sprites']['back_default']
            sprite_obj.back_female = pokemon['sprites']['back_female']
            sprite_obj.back_shiny = pokemon['sprites']['back_shiny']
            sprite_obj.back_shiny_female = pokemon['sprites']['back_shiny_female']
            sprite_obj.front_default = pokemon['sprites']['front_default']
            sprite_obj.front_female = pokemon['sprites']['front_female']
            sprite_obj.front_shiny = pokemon['sprites']['front_shiny']
            sprite_obj.front_shiny_female = pokemon['sprites']['front_shiny_female']

            print(SpritesSerializer(sprite_obj).data)
            print('')

            ser = SpritesSerializer(sprite_obj)
            serializer = SpritesSerializer(sprite_obj, data = ser.data)
            if serializer.is_valid():
                serializer.save()
            else:
                print(serializer.errors)

class chargeDataPokemons():
    with open('pokemon/fixtures/pokemons.json') as file:
        data = json.load(file)
        i = 0;
        for pokemon in data['data']:
           # print(pokemon['sprites']['back_default'])
            pokemon_obj = Pokemons()
            pokemon_obj.name = pokemon['name']
            pokemon_obj.capture_rate = pokemon['capture_rate']
            pokemon_obj.color = pokemon['color']
            pokemon_obj.flavor_text = pokemon['flavor_text']
            pokemon_obj.height = pokemon['height']
            pokemon_obj.weight = pokemon['weight']

            sprite_obj = Sprites()
            sprite_obj.back_default = pokemon['sprites']['back_default']
            sprite_obj.front_default = pokemon['sprites']['front_default']

            try:
                sprites_objs = Sprites.objects.get(back_default = sprite_obj.back_default, front_default = sprite_obj.front_default) 
                #print(SpritesSerializer(sprites_objs).data)
                
                pokemon_obj.id_sprites = sprites_objs

                print(PokemonsSerializer(pokemon_obj).data)
                ser = PokemonsSerializer(pokemon_obj)
                serializer = PokemonsSerializer(pokemon_obj, data = ser.data)
                if serializer.is_valid():
                    serializer.save()
                else:
                    print(serializer.errors)
            except Sprites.DoesNotExist:
                ser = PokemonsSerializer(pokemon_obj)
                serializer = PokemonsSerializer(pokemon_obj, data = ser.data)
                if serializer.is_valid():
                    serializer.save()
                else:
                    print(serializer.errors)

class chargeDataStats():
    with open('pokemon/fixtures/pokemons.json') as file:
        data = json.load(file)
        elemento = []
        norepetido = True
        for pokemon in data['data']:
            try:
                pokemon_obj = Pokemons.objects.get(name = pokemon['name'])
                #print(PokemonsSerializer(pokemon_obj).data)
                for a in pokemon['stats']:
                    stats_obj = Stats()
                    stats_obj.id_pokemons = pokemon_obj
                    stats_obj.name = a['name']
                    stats_obj.value = a['value']
                    ser = StatsSerializer(stats_obj)
                    serializer = StatsSerializer(stats_obj, data = ser.data)
                    if serializer.is_valid():
                        serializer.save()
                    else:
                        print(serializer.errors)
                    print(StatsSerializer(stats_obj).data)
                    print('')
            except Pokemons.DoesNotExist:
                print('error') 


class chargeDataPokemonsMove():
    with open('pokemon/fixtures/pokemons.json') as file:
        data = json.load(file)
        elemento = []
        norepetido = True
        for pokemon in data['data']:
            try:
                pokemon_obj = Pokemons.objects.get(name = pokemon['name'])
                #print(PokemonsSerializer(pokemon_obj).data)
                for a in pokemon['moves']:
                    pokemonsMoves_obj = PokemonsMoves()
                    move_obj = Moves.objects.get(move = a)

                    pokemonsMoves_obj.id_pokemons = pokemon_obj
                    pokemonsMoves_obj.id_moves = move_obj

                    print(PokemonsMovesSerializer(pokemonsMoves_obj).data)
                    ser = PokemonsMovesSerializer(pokemonsMoves_obj)
                    serializer = PokemonsMovesSerializer(pokemonsMoves_obj, data = ser.data)
                    if serializer.is_valid():
                        serializer.save()
                    else:
                        print(serializer.errors)
            except Pokemons.DoesNotExist:
                print('error') 

class chargeDataPokemonsAbilities():
    with open('pokemon/fixtures/pokemons.json') as file:
        data = json.load(file)
        elemento = []
        norepetido = True
        for pokemon in data['data']:
            try:
                pokemon_obj = Pokemons.objects.get(name = pokemon['name'])
                #print(PokemonsSerializer(pokemon_obj).data)
                for a in pokemon['abilities']:
                    pokemonsabilities_obj = PokemonsAbilities()
                    abilities_obj = Abilities.objects.get(ability = a)

                    pokemonsabilities_obj.id_pokemons = pokemon_obj
                    pokemonsabilities_obj.id_abilities = abilities_obj

                    print(PokemonsAbilitiesSerializer(pokemonsabilities_obj).data)
                    ser = PokemonsAbilitiesSerializer(pokemonsabilities_obj)
                    serializer = PokemonsAbilitiesSerializer(pokemonsabilities_obj, data = ser.data)
                    if serializer.is_valid():
                        serializer.save()
                    else:
                        print(serializer.errors)
            except Pokemons.DoesNotExist:
                print('error') 

class chargeDataPokemonsTypes():
    with open('pokemon/fixtures/pokemons.json') as file:
        data = json.load(file)
        elemento = []
        norepetido = True
        for pokemon in data['data']:
            try:
                pokemon_obj = Pokemons.objects.get(name = pokemon['name'])
                #print(PokemonsSerializer(pokemon_obj).data)
                for a in pokemon['types']:
                    pokemonsType_obj = PokemonsTypes()
                    types_obj = Types.objects.get(type = a)

                    pokemonsType_obj.id_pokemons = pokemon_obj
                    pokemonsType_obj.id_types = types_obj
                    
                    print(PokemonsTypesSerializer(pokemonsType_obj).data)
                    ser = PokemonsTypesSerializer(pokemonsType_obj)
                    serializer = PokemonsTypesSerializer(pokemonsType_obj, data = ser.data)
                    if serializer.is_valid():
                        serializer.save()
                    else:
                        print(serializer.errors)
                    
                    
            except Pokemons.DoesNotExist:
                print('error') 


class chargeDataPokemonsAreas():
    with open('pokemon/fixtures/areas.json') as file:
        data = json.load(file)
        for area in data['data']:


            
                area_obj = Areas.objects.get(name = area['name'])
                #print(PokemonsSerializer(pokemon_obj).data)
                for a in area['pokemons']:
                    pokemonsAreas_obj = PokemonsAreas()
                    try:
                        
                        pokemon_obj = Pokemons.objects.get(name = a.capitalize())
                        pokemonsAreas_obj.id_pokemons = pokemon_obj
                        pokemonsAreas_obj.id_areas = area_obj
                        ser = PokemonsAreasSerializer(pokemonsAreas_obj)
                        serializer = PokemonsAreasSerializer(pokemonsAreas_obj, data = ser.data)
                        if serializer.is_valid():
                            serializer.save()
                        else:
                            print(serializer.errors)
                        print(PokemonsAreasSerializer(pokemonsAreas_obj).data)
                    except Pokemons.DoesNotExist:
                        print('no existe: ', a.capitalize())