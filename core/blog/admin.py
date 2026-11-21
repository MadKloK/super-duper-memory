from django.contrib import admin
from blog.models import Post, Category

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'status', 'category', 'created_at', 'published_at']
    list_filter = ['status', 'category']
    search_fields = ['title', 'content']
    ordering = ['-created_at']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']