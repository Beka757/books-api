from django.urls import path
from api.views.books_view import BookListApiView, BookDetailApiView


urlpatterns = [
    path('', BookListApiView.as_view(), name='book-list'),
    path('books/<int:id>/', BookDetailApiView.as_view(), name='book-detail')
]
