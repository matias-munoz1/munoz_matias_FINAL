from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Inscrito, Institucion
from .forms import InscritoForm, InstitucionForm
from django.http import JsonResponse
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import InscritoSerializer, InstitucionSerializer, AutorSerializer

def index(request):
   return render(request, 'index.html')

class InscritoListView(ListView):
    model = Inscrito
    template_name = 'inscritos/inscritos_list.html'
    context_object_name = 'inscritos'

class InscritoCreateView(CreateView):
    model = Inscrito
    form_class = InscritoForm
    template_name = 'inscritos/inscritos_form.html'
    success_url = reverse_lazy('inscrito_list')

class InscritoUpdateView(UpdateView):
    model = Inscrito
    form_class = InscritoForm
    template_name = 'inscritos/inscritos_form.html'
    success_url = reverse_lazy('inscrito_list')

class InscritoDeleteView(DeleteView):
    model = Inscrito
    template_name = 'inscritos/inscritos_confirm_delete.html'
    success_url = reverse_lazy('inscrito_list')

def instituciones_list(request):
    instituciones = Institucion.objects.all()
    return render(request, 'instituciones/instituciones_list.html', {'instituciones': instituciones})

def institucion_detail(request, pk):
    institucion = get_object_or_404(Institucion, pk=pk)
    return JsonResponse({'id': institucion.id, 'nombre': institucion.nombre})


@api_view(['GET'])
def autor_data(request):
    data = {
        'nombre': 'Matias Munoz',
        'proyecto': 'munoz_matias_FINAL'
    }
    serializer = AutorSerializer(data)
    return Response(serializer.data)

class InscritoListAPI(generics.ListCreateAPIView):
    queryset = Inscrito.objects.all()
    serializer_class = InscritoSerializer

class InscritoDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Inscrito.objects.all()
    serializer_class = InscritoSerializer

@api_view(['GET'])
def institucion_list_api(request):
    instituciones = Institucion.objects.all()
    serializer = InstitucionSerializer(instituciones, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def institucion_detail_api(request, pk):
    institucion = get_object_or_404(Institucion, pk=pk)
    serializer = InstitucionSerializer(institucion)
    return Response(serializer.data)
