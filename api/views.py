from rest_framework import generics
from .models import Artisan, Customer, Metier, Coordonnees, Service
from .serializers import ArtisanSerializers, CustomerSerializers, MetierSerializers, CoordonneesSerializers, ServiceSerializers



# Create your views here.


########################################################################
######################        Metier Views        ######################
########################################################################

class MetierListCreate(generics.ListCreateAPIView):
    queryset = Metier.objects.all()
    serializer_class = MetierSerializers
    
class MetierRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Metier.objects.all()
    serializer_class = MetierSerializers
    lookup_field = "pk"


########################################################################
######################        Coords Views        ######################
########################################################################

class CoordonneeListCreate(generics.ListCreateAPIView):
    queryset = Coordonnees.objects.all()
    serializer_class = CoordonneesSerializers

class CoordonneeRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Coordonnees.objects.all()
    serializer_class = CoordonneesSerializers
    lookup_field = "pk"



########################################################################
######################       Artisan Views        ######################
########################################################################

class ArtisanListCreate(generics.ListCreateAPIView):
    queryset = Artisan.objects.all()
    serializer_class = ArtisanSerializers
    
    
class ArtisanRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Artisan.objects.all()
    serializer_class = ArtisanSerializers
    lookup_field = "pk"
    

########################################################################
######################       Service Views        ######################
########################################################################

class ServiceListCreate(generics.ListCreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializers
    
    
class ServiceRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializers
    lookup_field = "pk"


########################################################################
######################       Customer Views       ######################
########################################################################

class CustomerListCreate(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializers
    
    
class CustomerRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializers
    lookup_field = "pk"


########################################################################
######################       Artisan Views        ######################
########################################################################

class ArtisanListCreate(generics.ListCreateAPIView):
    queryset = Artisan.objects.all()
    serializer_class = ArtisanSerializers
    
    
class ArtisanRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Artisan.objects.all()
    serializer_class = ArtisanSerializers
    lookup_field = "pk"