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
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer

def index(request):
    return render(request, 'index.html')


def custom_api_view(request):
    return JsonResponse({"message": "Esta es la API REST del Seminario"})


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


class InscritoListAPI(APIView):
    """
    API que lista y permite crear inscritos.
    """
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'api_list.html'

    def get(self, request):
        inscritos = Inscrito.objects.all()
        serializer = InscritoSerializer(inscritos, many=True)
        form = InscritoForm()
        return Response({'inscritos': serializer.data, 'form': form})

    def post(self, request):
        form = InscritoForm(request.POST)
        if form.is_valid():
            form.save()
            return self.get(request)  
        inscritos = Inscrito.objects.all()
        serializer = InscritoSerializer(inscritos, many=True)
        return Response({'inscritos': serializer.data, 'form': form}, status=400)


class InscritoDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Inscrito.objects.all()
    serializer_class = InscritoSerializer



class InstitucionListAPI(APIView):
    renderer_classes = [TemplateHTMLRenderer, JSONRenderer]  
    template_name = 'api_list.html'

    def get(self, request):
        instituciones = Institucion.objects.all()
        serializer = InstitucionSerializer(instituciones, many=True)
        form = InstitucionForm()
        return Response({'instituciones': serializer.data, 'form': form})

    def post(self, request):
        form = InstitucionForm(request.POST)
        if form.is_valid():
            form.save()
            instituciones = Institucion.objects.all()
            serializer = InstitucionSerializer(instituciones, many=True)
            return Response({'instituciones': serializer.data, 'form': form, 'message': 'Institución creada exitosamente'})
        instituciones = Institucion.objects.all()
        serializer = InstitucionSerializer(instituciones, many=True)
        return Response({'instituciones': serializer.data, 'form': form, 'errors': form.errors})

@api_view(['GET', 'POST'])
def institucion_list_api(request):
    if request.method == 'GET':
        instituciones = Institucion.objects.all()
        serializer = InstitucionSerializer(instituciones, many=True)
        return Response({'instituciones': serializer.data})

    elif request.method == 'POST':
        serializer = InstitucionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Institución creada exitosamente!', 'institucion': serializer.data})
        return Response(serializer.errors, status=400)
