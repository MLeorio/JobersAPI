from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Artisan, Customer, Metier


admin.site.site_header = "Administration de AllPro"
admin.site.site_title = "Admin AllPro"
admin.site.index_title = "Bienvenu dans l'interface d'administration"


# Register your models here.


class ArtisanMetierInline(admin.TabularInline):
    model = Artisan
    extra = 1


class ArtianUserInline(admin.TabularInline):
    model = Artisan
    extra = 1

class CustomerUserInline(admin.StackedInline):
    model = Customer
    extra = 1


class MetierAdmin(admin.ModelAdmin):
    inlines = [ArtisanMetierInline]
    list_display = ("label_metier", "description_metier", "created_at", "updated_at")
    list_filter = ("label_metier", "description_metier")
    search_fields = ("label_metier",)
    ordering = ("label_metier",)
    fieldsets = ((None, {"fields": ("label_metier", "description_metier")}),)


class UserAdmin(BaseUserAdmin):
    inlines = [ArtianUserInline, CustomerUserInline]
    list_display = ("username", "phone", "is_active", "date_joined")
    list_filter = ("is_active", "date_joined")
    search_fields = ("username", "phone", "email")
    ordering = ("date_joined",)
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (
            ("Infos personnelles"),
            {"fields": ("phone", "email", "last_name", "first_name")},
        ),
        (
            ("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_client",
                    "is_artisan",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        (("Dates importantes"), {"fields": ("last_login", "date_joined")}),
    )



class ArtisanAdmin(admin.ModelAdmin):
    list_display = ("workshop_name", "quartier", 'get_phone', 'user')
    search_fields = ('get_phone', 'quartier')
    list_filter = ('user__is_active', 'user__is_artisan')
    fieldsets = (
        (('Compte Utilisateur'), {'fields': ("user",)}),
        (('Atelier'), {'fields': ("workshop_name", "quartier")}),
        (('Service Metier'), {'fields': ("metier",)})
    )
    
    def get_phone(sself, obj):
        return obj.user.phone
    get_phone.short_description = "Numéro de téléphone"


admin.site.register(Metier, MetierAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Artisan, ArtisanAdmin)

admin.site.register(Customer)
