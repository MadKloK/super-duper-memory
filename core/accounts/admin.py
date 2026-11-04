from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import User

# Register your models here.


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ['email', 'is_superuser', 'is_active']
    list_filter = ['is_superuser', 'is_active']
    search_fields = ['email']
    ordering = ['created_date']
    
    fieldsets = [
        ('Authentication', {
            'fields': ('email', 'password'),
        }),
        ('Permissions', {
            'fields': ('is_superuser', 'is_staff', 'is_active'),
        }),
    ]

    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["email", "password1", "password2", "is_superuser", "is_staff"],
            },
        ),
    ]
