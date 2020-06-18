# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = True` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import User

# **** Modelos de BD ****
class Abilities(models.Model):
    id = models.BigAutoField(primary_key=True)
    ability = models.CharField(max_length=200)

    class Meta:
        managed = True
        db_table = 'abilities'


class Areas(models.Model):
    id = models.BigAutoField(primary_key=True)
    id_locations = models.ForeignKey('Locations', models.DO_NOTHING, db_column='id_locations', related_name='areas')
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200, blank=True, null=True)
    pokemon_count = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'areas'

class Locations(models.Model):
    id = models.BigAutoField(primary_key=True)
    id_regions = models.ForeignKey('Regions', models.DO_NOTHING, db_column='id_regions', related_name='locations')
    name = models.CharField(max_length=200)

    class Meta:
        managed = True
        db_table = 'locations'


class Moves(models.Model):
    id = models.BigAutoField(primary_key=True)
    move = models.CharField(max_length=200)

    class Meta:
        managed = True
        db_table = 'moves'


class Pokemons(models.Model):
    id = models.BigAutoField(primary_key=True)
    id_sprites = models.ForeignKey('Sprites', models.DO_NOTHING, db_column='id_sprites', blank=True, null=True)
    name = models.CharField(max_length=200)
    capture_rate = models.FloatField()
    color = models.CharField(max_length=200)
    flavor_text = models.CharField(max_length=200)
    height = models.FloatField()
    weight = models.FloatField()

    class Meta:
        managed = True
        db_table = 'pokemons'


class PokemonsAbilities(models.Model):
    id = models.BigAutoField(primary_key=True)
    id_abilities = models.ForeignKey(Abilities, models.DO_NOTHING, db_column='id_abilities')
    id_pokemons = models.ForeignKey(Pokemons, models.DO_NOTHING, db_column='id_pokemons', related_name='abilities')

    class Meta:
        managed = True
        db_table = 'pokemons_abilities'

class PokemonsAreas(models.Model):
    id = models.BigAutoField(primary_key=True)
    id_areas = models.ForeignKey(Areas, models.DO_NOTHING, db_column='id_areas', related_name = 'pokemons')
    id_pokemons = models.ForeignKey(Pokemons, models.DO_NOTHING, db_column='id_pokemons')

    class Meta:
        managed = True
        db_table = 'pokemons_areas'


class PokemonsMoves(models.Model):
    id = models.BigAutoField(primary_key=True)
    id_pokemons = models.ForeignKey(Pokemons, models.DO_NOTHING, db_column='id_pokemons', related_name='moves')
    id_moves = models.ForeignKey(Moves, models.DO_NOTHING, db_column='id_moves')

    class Meta:
        managed = True
        db_table = 'pokemons_moves'


class PokemonsTypes(models.Model):
    id = models.BigAutoField(primary_key=True)
    id_types = models.ForeignKey('Types', models.DO_NOTHING, db_column='id_types')
    id_pokemons = models.ForeignKey(Pokemons, models.DO_NOTHING, db_column='id_pokemons', related_name='types')

    class Meta:
        managed = True
        db_table = 'pokemons_types'


class Regions(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=200)

    class Meta:
        managed = True
        db_table = 'regions'


class Sprites(models.Model):
    id = models.BigAutoField(primary_key=True)
    back_default = models.CharField(max_length=200, blank=True, null=True)
    front_default = models.CharField(max_length=200)
    back_shiny = models.CharField(max_length=200, blank=True, null=True)
    back_shiny_female = models.CharField(max_length=200, blank=True, null=True)
    back_female = models.CharField(max_length=200, blank=True, null=True)
    front_shiny = models.CharField(max_length=200, blank=True, null=True)
    front_shiny_female = models.CharField(max_length=200, blank=True, null=True)
    front_female = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'sprites'


class Stats(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=200)
    value = models.BigIntegerField()
    id_pokemons = models.ForeignKey(Pokemons, models.DO_NOTHING, db_column='id_pokemons', related_name='stats')

    class Meta:
        managed = True
        db_table = 'stats'


class Storage(models.Model):
    id = models.BigAutoField(primary_key=True)
    id_pokemons = models.ForeignKey(Pokemons, models.DO_NOTHING, db_column='id_pokemons')
    nick_name = models.CharField(max_length=200, blank=True, null=True)
    is_party_member = models.BooleanField()
    id_user = models.ForeignKey(User, models.DO_NOTHING, db_column='id_user')

    class Meta:
        managed = True
        db_table = 'storage'


class Types(models.Model):
    id = models.BigAutoField(primary_key=True)
    type = models.CharField(max_length=200)

    class Meta:
        managed = True
        db_table = 'types'
