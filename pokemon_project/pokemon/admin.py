from django.contrib import admin
from .models import Regions, Pokemons, Abilities, Areas, Locations, Moves, PokemonsAbilities, PokemonsMoves, PokemonsTypes
from .models import Sprites, Stats, Storage, Types

# Register your models here.
admin.site.register(Regions)
admin.site.register(Pokemons)
admin.site.register(Abilities)
admin.site.register(Areas)
admin.site.register(Locations)
admin.site.register(Moves)
admin.site.register(PokemonsAbilities)
admin.site.register(PokemonsMoves)
admin.site.register(PokemonsTypes)
admin.site.register(Sprites)
admin.site.register(Stats)
admin.site.register(Storage)
admin.site.register(Types)