from django.contrib import admin
from .models import User, Artisan, Customer, Metier

# Register your models here.
admin.site.register([User, Artisan, Customer, Metier])