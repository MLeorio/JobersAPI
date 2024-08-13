from datetime import timedelta
from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone

# Create your models here.


class Metier(models.Model):
    label_metier = models.CharField(max_length=100, verbose_name="Nom du métier")
    description_metier = models.TextField(verbose_name="Description du métier")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.label_metier


class User(AbstractUser):
    is_client = models.BooleanField(default=False, verbose_name="Est un Client")
    is_artisan = models.BooleanField(default=False, verbose_name="Est un Artisan")
    phone = PhoneNumberField(
        unique=True, verbose_name="Numéro de téléphone", null=False
    )
    is_active = models.BooleanField(
        default=False
    )  # Non actif jusqu'à la verification par email
    otp = models.CharField(max_length=6, blank=True, null=True)
    otp_created_at = models.DateTimeField(blank=True, null=True)

    def is_otp_expired(self):
        if self.otp_created_at:
            return timezone.now() > self.otp_created_at + timedelta(
                minutes=10
            )  # OTP valide pendant 10 minutes
        return True


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)


class Artisan(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    workshop_name = models.CharField(
        max_length=255, unique=True, verbose_name="Nom de l'atelier"
    )
    quartier = models.CharField(max_length=255, verbose_name="Quartier")
    metier = models.ForeignKey(Metier, on_delete=models.SET_NULL, null=True)
