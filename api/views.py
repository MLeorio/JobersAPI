from django.urls import reverse
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from django.contrib.auth import get_user_model
from rest_framework.response import Response

from .services import generate_otp, send_otp
from .models import User
from .serializers import (
    CustomerRegisterSerializer,
    ArtisanRegisterSerializer,
    LoginSerializer,
)
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.utils import timezone
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import api_view


User = get_user_model()

# Create your views here.

@api_view(['GET'])
def Home_Description(request):
    api_urls = {
        "Page de documentation temporaire": "/",
        "Login" : "login/",
        "Confirmation du code OTP" : "confirm-otp/",
        "Inscription Client": "register/client/",
        "Inscription Artisan": "register/artisan/",
    }

    return Response(api_urls)





class RegisterCustomerView(generics.CreateAPIView):
    serializer_class = CustomerRegisterSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        # user = serializer.save()
        
        # Envoie de l'email d'activation
        # self.send_activation_email(user, request)
        
        # return Response(
        #     {"message": "Un email de confirmation a été envoyé."},
        #     status=status.HTTP_201_CREATED,
        # )
        
        return Response({"message": "Inscription réussie."}, status=status.HTTP_201_CREATED)

    # def send_activation_email(self, user, request):
    #     token = default_token_generator.make_token(user)
    #     uid = urlsafe_base64_encode(force_bytes(user.pk))
    #     current_site = get_current_site(request)
    #     domain = current_site.domain
    #     relative_link = reverse("activate", kwargs={"uidb64": uid, "token": token})
    #     activate_url = f"http://{domain}{relative_link}"
    #     email_subject = "Activation de votre compte"
    #     email_body = render_to_string(
    #         "account_activation_email.html",
    #         {"user": user, "activate_url": activate_url},
    #     )
    #     send_mail(
    #         email_subject,
    #         email_body,
    #         "noreply@jobers.com",
    #         [user.email],
    #         fail_silently=False,
    #     )


class RegisterArtisanView(RegisterCustomerView):
    serializer_class = ArtisanRegisterSerializer


class ActivateAccountView(generics.GenericAPIView):
    permission_classes = [AllowAny]

    def get(self, request, uidb64, token, *args, **kwargs):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user is not None and default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            return Response(
                {"message": "Compte activé avec succès."}, status=status.HTTP_200_OK
            )
        else:
            return Response(
                {"error": "Le lien d'activation est invalide."},
                status=status.HTTP_400_BAD_REQUEST,
            )


class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data["user"]
            if user.is_otp_expired():
                otp = generate_otp()
                user.otp = otp
                user.otp_created_at = timezone.now()
                user.save()
                
                print(str(user.phone), otp)
                send_otp(str(user.phone), otp)

            return Response(
                {
                    "message": "Un OTP vous a été envoyé. Veuillez valider pour acceéder à votre compte"
                }
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class ValidateOTPView(APIView):
    def post(self, request, *args, **kwargs):
        phone = request.data.get("phone")
        otp = request.data.get("otp")
        
        try:
            user = User.objects.get(phone=phone, otp= otp)
            if user.is_otp_expired():
                return Response({"error": "Code OTP expiré"}, status=status.HTTP_400_BAD_REQUEST)
            
            user.otp = None
            user.otp_created_at = None
            
            if not user.is_active:
                user.is_active = True
            
            user.save()
            
            jwt_token = RefreshToken.for_user(user)
            return Response({
                'message': "Connexion réussie",
                'refresh': str(jwt_token),
                'access': str(jwt_token.access_token),
            })
        except User.DoesNotExist:
            return Response({"error": "Code OTP invalide"}, status=status.HTTP_400_BAD_REQUEST)
            
