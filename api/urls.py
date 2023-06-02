from django.urls import path
from .views.books_view import BookListApiView

books_url = [
    path('', BookListApiView.as_view()),
]

urlpatterns = []

urlpatterns += books_url
