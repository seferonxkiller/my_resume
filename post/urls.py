from django.urls import path
from .views import *

app_name = 'post'

urlpatterns = [
    path('<int:pk>/', blog_single, name='blog-single'),
]
