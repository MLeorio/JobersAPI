from django.urls import path
from .views import (
    RegisterCustomerView,
    RegisterArtisanView,
    ActivateAccountView,
    LoginView,
    Home_Description,
    ValidateOTPView,
)

urlpatterns = [
    path("", Home_Description, name="Documentation"),
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
    path("activate/<uidb64>/<token>/", ActivateAccountView.as_view(), name="activate"),
    path("login/", LoginView.as_view(), name="login"),
    path("confirm-otp/", ValidateOTPView.as_view(), name="Confirm-OTP"),
]
