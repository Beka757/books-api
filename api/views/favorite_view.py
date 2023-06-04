from rest_framework.generics import get_object_or_404
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from api.serializers.favorite_serializer import FavoriteSerializer
from app.models import Book
from app.models.favorite import Favorite
from rest_framework.response import Response


class BooksFavoriteView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = FavoriteSerializer

    def post(self, request, *args, **kwargs):
        book = get_object_or_404(Book, pk=self.kwargs['pk'])
        user = self.request.user
        existing_favorite = Favorite.objects.filter(book=book, user=user).first()
        if existing_favorite:
            existing_favorite.delete()
            return Response({'status': 'Книга удалена из избранных'})
        else:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(book=book, user=user)
            return Response({'status': 'Книга добавлена в избранные'})
