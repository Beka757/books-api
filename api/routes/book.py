from django.urls import path
from api.views.books_view import BookListApiView


urlpatterns = [
    path('', BookListApiView.as_view()),
]
