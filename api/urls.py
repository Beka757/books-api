from django.urls import path, include


urlpatterns = [
    path('schema/', include('api.routes.swagger')),
    path('auth/', include('api.routes.auth')),
    path('', include('api.routes.book'))
]
