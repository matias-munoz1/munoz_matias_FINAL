from django.urls import path
from .views import (
    InscritoListView, InscritoCreateView, InscritoUpdateView, InscritoDeleteView,
    instituciones_list, institucion_detail,
    InscritoListAPI, InscritoDetailAPI,
    institucion_list_api, institucion_detail_api
)

urlpatterns = [
    # Web
    path('inscritos/', InscritoListView.as_view(), name='inscrito_list'),
    path('inscritos/nuevo/', InscritoCreateView.as_view(), name='inscrito_create'),
    path('inscritos/<int:pk>/editar/', InscritoUpdateView.as_view(), name='inscrito_update'),
    path('inscritos/<int:pk>/eliminar/', InscritoDeleteView.as_view(), name='inscrito_delete'),
    path('instituciones/', instituciones_list, name='instituciones_list'),
    path('instituciones/<int:pk>/', institucion_detail, name='institucion_detail'),

    # API
    path('api/inscritos/', InscritoListAPI.as_view(), name='api_inscritos_list'),
    path('api/inscritos/<int:pk>/', InscritoDetailAPI.as_view(), name='api_inscritos_detail'),
    path('api/instituciones/', institucion_list_api, name='api_instituciones_list'),
    path('api/instituciones/<int:pk>/', institucion_detail_api, name='api_institucion_detail'),
]
