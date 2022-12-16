#django import
from django.urls import path

#Views
from apps.notas.api.views import (NotasApiView,
                          CreateNotasApiView,
                          NotasDetailApiView,
                        )

#urls
urlpatterns = [
    path('notas-list/', NotasApiView.as_view(), name='notas_list'),
    path('create-notas/', CreateNotasApiView.as_view(), name='create'),
    path('detail-notas/<int:pk>/', NotasDetailApiView.as_view(), name='detail'),
]