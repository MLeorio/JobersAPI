from rest_framework import serializers
from .models import Metier, Prestation, Artisan, Coordonnees, Customer, Service
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = User
        fields = ["id", "username", "password", "email"]


class MetierSerializers(serializers.ModelSerializer):
    class Meta:
        model = Metier
        fields = ["id", "label_metier", "description_metier", "created_at", "updated_at"]


class CoordonneesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Coordonnees
        fields = ["id", "longitude", "latitude", "created_at", "updated_at"]
        
    
class ArtisanSerializers(serializers.ModelSerializer):
    class Meta:
        model = Artisan
        fields = ["id", "label_atelier", "quartier", "tel", "created_at", "updated_at"]

class ServiceSerializers(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ["id", "label_service", "description_service", "created_at", "updated_at"]

class CustomerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ["id", "username", "prestation_service", "created_at", "updated_at"]
