from django.urls import path
from .views import ImageList

urlpatterns = [
    path('images/', ImageList.as_view(), name='image-list'),
]