from .models import Regions, Pokemons, Sprites, Areas, Abilities, Moves, Types, PokemonsAbilities, PokemonsMoves
from .models import PokemonsTypes, Stats, Storage, Locations
from rest_framework import serializers

# ******* clase para serializar una relacion anidada de objeto  ******
class AbilitiesListingField(serializers.RelatedField):
    def to_representation(self, value):
        return { 'ability':value.id_abilities.ability }

class MovesListingField(serializers.RelatedField):
    def to_representation(self, value):
        return { 'move': value.id_moves.move }

class TypesListingField(serializers.RelatedField):
    def to_representation(self, value):
        return { 'type': value.id_types.type }

class StatsListingField(serializers.RelatedField):
    def to_representation(self, value):
        return { 'name': value.name, 'value': value.value }

class LocationsListingField(serializers.RelatedField):
    def to_representation(self, value):
        return { 'id': value.id, 'name': value.name }

class AreasListingField(serializers.RelatedField):
    def to_representation(self, value):
        return { 'id': value.id, 'name': value.name, 'pokemon_count': value.pokemon_count, 'location': value.location }

class PokemonsListingField(serializers.RelatedField):
    def to_representation(self, value):
        return PokemonsSerializer(value).data


# ****** Serializers ********
class AbilitiesSerializer(serializers.ModelSerializer):
    class Meta:
        Model = Abilities
        field = '__all__'

class MovesSerializer(serializers.ModelSerializer):
    class Meta:
        Model = Moves
        field = '__all__'

class TypesSerializer(serializers.ModelSerializer):
    class Meta:
        Model = Types
        field = '__all__'
    
class StatsSerializer(serializers.ModelSerializer):
    class Meta:
        Model = Stats
        field = '__all__'

class PokemonsAbilitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PokemonsAbilities
        field = ['id_abilities', 'id_pokemons']

class PokemonsMovesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PokemonsMoves
        fields = '__all__'

class PokemonsTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PokemonsTypes
        fields = '__all__'

class SpritesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sprites
        fields = '__all__'

class AreasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Areas
        fields = '__all__'

class PokemonsSerializer(serializers.ModelSerializer):
    id_sprites = SpritesSerializer(read_only =True)
    #id_areas = AreasSerializer(read_only =True)
    #abilities = serializers.StringRelatedField(many=True)
    abilities = AbilitiesListingField(many = True, read_only =True)
    moves = MovesListingField(many = True, read_only =True)
    types = TypesListingField(many = True, read_only =True)
    stats = StatsListingField(many = True, read_only =True)
    class Meta:
        model = Pokemons
        fields = ['id', 'id_sprites', 'name', 'capture_rate', 'color', 'flavor_text', 'height', 'weight', 'abilities', 'moves', 'types', 'stats']

class StorageSerializer(serializers.ModelSerializer):
    id_pokemons = PokemonsSerializer(read_only =True)
    class Meta:
        model = Storage
        fields = ['id', 'id_pokemons', 'nick_name', 'is_party_member', 'id_user']

class StoragePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Storage
        fields = ['id', 'id_pokemons', 'nick_name', 'is_party_member', 'id_user']

class RegionsSerializer(serializers.ModelSerializer):
    locations = LocationsListingField(many = True, read_only =True)
    class Meta:
        model = Regions
        fields = ['id','name', 'locations']

class RegionsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Regions
        fields = ['id','name']

class LocationsSerializer(serializers.ModelSerializer):
    areas = AreasListingField(many = True, read_only =True)
    class Meta:
        model = Locations
        fields = ['id', 'areas', 'name', 'id_regions']

class AreasSerializer(serializers.ModelSerializer):
    pokemons = PokemonsListingField(many = True, read_only =True)
    class Meta:
        model = Areas
        fields = ['id', 'name', 'location', 'pokemon_count', 'pokemons']