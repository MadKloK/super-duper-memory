from django.db import models

# Create your models here.

class Post(models.Model):
    '''
    Model representing a blog post.
    '''

    title = models.CharField(max_length=200)
    author = models.ForeignKey('User', on_delete=models.CASCADE)
    content = models.TextField()
    image = models.ImageField(null=True, blank=True)
    status = models.BooleanField(default=False)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, blank=False)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField()

    def __str__(self):
        return self.title


class Category(models.Model):
    '''
    Model representing a blog post category.
    '''
    
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name