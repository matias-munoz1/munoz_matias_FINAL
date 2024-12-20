from django.urls import path
from app_seminario.views import (
    index, 
    InscritoListView, 
    InscritoCreateView, 
    InscritoUpdateView, 
    InscritoDeleteView, 
    InstitucionListAPI, 
    instituciones_list,    
    institucion_detail,    
    autor_data,            
    custom_api_view,       
    InscritoListAPI,    
)


urlpatterns = [
    path('inscritos/', InscritoListView.as_view(), name='inscrito_list'),
    path('inscritos/nuevo/', InscritoCreateView.as_view(), name='inscrito_create'),
    path('inscritos/<int:pk>/editar/', InscritoUpdateView.as_view(), name='inscrito_update'),
    path('inscritos/<int:pk>/eliminar/', InscritoDeleteView.as_view(), name='inscrito_delete'),
    path('instituciones/', instituciones_list, name='instituciones_list'),
    path('instituciones/<int:pk>/', institucion_detail, name='institucion_detail'),
    path('seminario/api/inscritos/', InscritoListAPI.as_view(), name='api-inscritos'),
    path('api/autor/', autor_data, name='api-autor'),
    path('api/', custom_api_view, name='custom-api'),
    path('seminario/api/instituciones/', InstitucionListAPI.as_view(), name='api-instituciones'),
]
