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

# **** Vistas ****
# Create your views here.
class PokemonsDetails(APIView):
    #Get Pokemon
    permission_classes = [AllowAny]
    def get_object(self, pk):
        try:
            return Pokemons.objects.get(pk=pk)
        except Pokemons.DoesNotExist:
            raise Http404
    def get(self, request, pk):
        pokemon = self.get_object(pk)
        serializer = PokemonsSerializer(pokemon)
        
        return Response(serializer.data)

class StorageList(APIView):
    #Get and post Storage
    
    def get(self, request):
        token = request.headers['Authorization'][6:]
        token_obj = Token.objects.get(key = token)
        
        storage = Storage.objects.filter(id_user = token_obj.user_id)
        serializer = StorageSerializer(storage, many = True)
        return Response(serializer.data)
    
    def post(self, request):
        token = request.headers['Authorization'][6:]
        token_obj = Token.objects.get(key = token)
        request.data['id_user'] = token_obj.user_id
        
        serializer = StoragePostSerializer(data = request.data)
        if serializer.is_valid():
            if request.data['is_party_member'] == True or (request.data['is_party_member']).lower() == "true":
                is_party = Storage.objects.filter(is_party_member = True, id_user = token_obj.user_id)
                if len(is_party) <6:
                    serializer.save()
                    return Response(serializer.data, status.HTTP_201_CREATED)
                else:
                    return Response({'mensaje: ': 'Party llena, solo puedes tener un maximo de 6 pokemon en tu party'}, status=status.HTTP_400_BAD_REQUEST)
            else:
                 serializer.save()
                 return Response(serializer.data, status.HTTP_201_CREATED)
        else:
           return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StorageDetails(APIView):
#Get, update, or delete Storage  
    def get_object(self, pk):
        try:
            return Storage.objects.get(pk=pk)
        except Storage.DoesNotExist:
            raise Http404
    def put(self, request, pk):
        storage = self.get_object(pk)
        request.data['is_party_member'] = storage.is_party_member
        request.data['id_pokemons'] = storage.id_pokemons.id
        request.data['id_user'] = storage.id_user.id
        serializer = StoragePostSerializer(storage, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        storage = self.get_object(pk)
        storage.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

class StorageParty(APIView):
    #Get pokemon from your party
    def get(self, request):
        token = request.headers['Authorization'][6:]
        token_obj = Token.objects.get(key = token)
        
        storage = Storage.objects.filter(id_user = token_obj.user_id, is_party_member = True)
        serializer = StorageSerializer(storage, many = True)
        return Response(serializer.data)



class RegionsList(APIView):
#Get all Regions
    permission_classes = [AllowAny]
    #permission_classes = [IsAuthenticated|ReadOnlyPost]  

    def get(self, request):
        region = Regions.objects.all()
        serializer = RegionsListSerializer(region, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

class RegionsDetails(APIView):
#Get a specifc region
    permission_classes = [AllowAny]
    def get_object(self, pk):
        try:
            return Regions.objects.get(pk=pk)
        except Regions.DoesNotExist:
            raise Http404
    def get(self, request, pk):
        region = self.get_object(pk)
        serializer = RegionsSerializer(region)
        return Response(serializer.data) 

class LocationsDetails(APIView):
#Get specifc region
    permission_classes = [AllowAny]
    def get_object(self, pk):
        try:
            return Locations.objects.get(pk=pk)
        except Locations.DoesNotExist:
            raise Http404
    def get(self, request, pk):
        locations = self.get_object(pk)
        serializer = LocationsSerializer(locations)
        return Response(serializer.data) 

class AreasDetails(APIView):
#Get a specifc region
    permission_classes = [AllowAny]
    def get_object(self, pk):
        try:
            return Areas.objects.get(pk=pk)
        except Areas.DoesNotExist:
            raise Http404
    def get(self, request, pk):
        areas = self.get_object(pk)
        serializer = AreasSerializer(areas)
        return Response(serializer.data) 