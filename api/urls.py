from django.urls import path, re_path
from .views import (
    CurrentUserView,
    LogoutView,
    MetierListCreateView,
    RegisterCustomerView,
    RegisterArtisanView,
    LoginView,
    ValidateOTPView,
)

urlpatterns = [
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
