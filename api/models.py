from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Metier(models.Model):
    label_metier = models.CharField(max_length=100, verbose_name="Nom du métier")
    description_metier = models.TextField(verbose_name="Description du métier")
    
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
        
    def __str__(self) -> str:
        return self.label_metier
    
    class Meta:
        verbose_name = "Métier ou Activité"
        verbose_name_plural = "Métiers ou Activités"
        ordering = ['label_metier']
    
class Coordonnees(models.Model):
    longitude = models.FloatField(verbose_name="Longitude")
    latitude = models.FloatField(verbose_name="Latitude")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> tuple:
        return (self.longitude, self.latitude)
    
    
class Artisan(models.Model):
    label_atelier = models.CharField(max_length=100, verbose_name="Nom de l'atelier")
    quartier = models.CharField(max_length=100, verbose_name="Quartier de l'atelier")
    tel = models.CharField(max_length=80, verbose_name="Telephone de l'atelier", null=True)
    
    coords = models.ForeignKey(Coordonnees, on_delete=models.CASCADE, related_name='coordonnees')
    metier = models.ForeignKey(Metier, on_delete=models.CASCADE, related_name="metier")
    
    user = models.ForeignKey(User, related_name="artisan", on_delete=models.CASCADE)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.label_workshop


class Service(models.Model):
    label_service = models.CharField(verbose_name="Libelle service", max_length=100)
    description_service = models.TextField(verbose_name="Description du service", null=True)
    
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.label_service

class Customer(models.Model):
    username = models.CharField(verbose_name="Nom d'utilisateur", max_length=100)
    prestation_service = models.ManyToManyField(Service, related_name="prestation")
    
    user = models.ForeignKey(User, related_name="client", on_delete=models.CASCADE)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.username


class Prestation(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="Client")
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name="Service")
    