# Django imports
from django.urls import path


# Views imports
from apps.usuarios.api.views import (
    user_api_view,
    user_detail_view
)


# Urls
urlpatterns = [
    
    path('usuarios-list/', user_api_view, name='usuarios_list'),
    path('create-usuarios/', user_api_view, name='create'),
    path('detail-usuarios/<int:pk>/', user_detail_view, name='detail'),
]