from django.urls import path, include


urlpatterns = [
    path('schema/', include('api.routes.swagger')),
    path('auth/', include('api.routes.auth')),
    path('', include('api.routes.book')),
    path('books/<int:pk>/', include('api.routes.review')),
    path('books/<int:pk>/', include('api.routes.favorite')),
]
