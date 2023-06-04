from django.urls import path
from api.views.reviews_view import ReviewCreateApiView


urlpatterns = [
    path('reviews/create/', ReviewCreateApiView.as_view(), name='review-create'),
]
