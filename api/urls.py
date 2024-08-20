from django.urls import include, path
from .views import (
    CurrentUserView,
    LogoutView,
    MetierListCreateView,
    RegisterCustomerView,
    RegisterArtisanView,
    LoginView,
    ValidateOTPView,
    # CustomerViewSet
)
from rest_framework import routers

# router = routers.DefaultRouter()
# # router.register(r"Register for Artisan", RegisterArtisanView)
# router.register(r"Client", CustomerViewSet)


urlpatterns = [
    
    # path("", include(router.urls)),
    
    path(
        "register/client/",
        RegisterCustomerView.as_view(),
        name="Inscription d'un client",
    ),
    path(
        "register/artisan/",
        RegisterArtisanView.as_view(),
        name="Inscription d'un artisan",
    ),
    path("login/", LoginView.as_view(), name="login"),
    path("confirm-otp/", ValidateOTPView.as_view(), name="Confirm-OTP"),
    path("liste-metiers/", MetierListCreateView.as_view(), name="Liste des metiers"),
    path("current-user/", CurrentUserView.as_view(), name="current-user"),
    path("logout/", LogoutView.as_view(), name="logout"),
]
