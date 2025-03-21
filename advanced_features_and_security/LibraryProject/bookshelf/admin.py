from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group, Permission
from .models import Book, CustomUser

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Display these fields in the list view
    search_fields = ('title', 'author')  # Enable search by title and author
    list_filter = ('publication_year',)  # Add a filter for publication year

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ["email", "date_of_birth", "is_staff", "is_superuser"]
    
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal Info", {"fields": ("date_of_birth", "profile_photo")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "is_superuser", "groups", "user_permissions")}),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "date_of_birth", "profile_photo", "password1", "password2", "is_staff", "is_superuser"),
        }),
    )

    ordering = ["email"]  # Fix: Set ordering to "email" instead of "username"

# Register the CustomUser model
admin.site.register(CustomUser, CustomUserAdmin)

# Manage Groups and Permissions in Admin
admin.site.unregister(Group)  # Unregister default Group model
admin.site.register(Group)  # Re-register to allow custom management
admin.site.register(Permission)  # Register Permission model for fine-grained access control
