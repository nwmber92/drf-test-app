from django.urls import path

from .views import AlbumAPIView

urlpatterns = [
    path('', AlbumAPIView.as_view())
]