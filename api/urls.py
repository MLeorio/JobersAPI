from django.urls import path
from .views import CustomerListCreate, CustomerRetrieveUpdateDestroy, MetierListCreate, MetierRetrieveUpdateDestroy, CoordonneeListCreate, CoordonneeRetrieveUpdateDestroy, ArtisanListCreate, ArtisanRetrieveUpdateDestroy, ServiceListCreate, ServiceRetrieveUpdateDestroy

urlpatterns = [
    path("metier/", MetierListCreate.as_view(), name="metier-view-create"),
    path("metier/<int:pk>/", MetierRetrieveUpdateDestroy.as_view(), name="metier-update"),
    
    path("coords/", CoordonneeListCreate.as_view(), name="coords-view-create"),
    path("coords/<int:pk>/", CoordonneeRetrieveUpdateDestroy.as_view(), name="coords-update"),
    
    path("artisan/", ArtisanListCreate.as_view(), name="artisan-view-create"),
    path("artisan/<int:pk>/", ArtisanRetrieveUpdateDestroy.as_view(), name="artisan-update"),
    
    path("service/", ServiceListCreate.as_view(), name="service-view-create"),
    path("service/<int:pk>/", ServiceRetrieveUpdateDestroy.as_view(), name="service-update"),
    
    path("customer/", CustomerListCreate.as_view(), name="customer-view-create"),
    path("customer/<int:pk>/", CustomerRetrieveUpdateDestroy.as_view(), name="customer-update"),
]
