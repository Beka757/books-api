from django.urls import path
from api.views.favorite_view import BooksFavoriteView


urlpatterns = [
    path('favorite/', BooksFavoriteView.as_view(), name='favorite'),
]
