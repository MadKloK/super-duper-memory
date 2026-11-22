from django.urls import path
from blog.views import *

urlpatterns = [
    path('', indexView, name='fbv-test'),
]