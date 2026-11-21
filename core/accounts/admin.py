from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import User, Profile
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

# Register your models here.


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ("email",)


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    model = User
    add_form = CustomUserCreationForm
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
        ('Group Permissions', {
            'fields': ('groups', 'user_permissions')
        }),
        ('Important Dates', {
            'fields': ('last_login',)
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


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass