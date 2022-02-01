from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, FormView, TemplateView
from core.erp.models import Auxiliar, Accion

from django.http import JsonResponse

from core.erp.forms import IngresoRelatoUsuarioForm, AccionForm

import speech_recognition as sr

from core.erp.pre_procesar import procesar


class PantallaHola(FormView):
    model = Auxiliar
    form_class = IngresoRelatoUsuarioForm
    template_name = 'dashboard.html'
    success_url = reverse_lazy('#')

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Bienvenido todo tipo de pensamiento'
        context['acciones'] = reverse_lazy('#')
        return context


class Prueba(FormView):
    model = Auxiliar
    template_name = 'pantallas/historia.html'
    form_class = IngresoRelatoUsuarioForm
    success_url = reverse_lazy('prueba')

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            print(action)
            if action == 'tx':
                print('Subir Textofff')
                form1 = self.get_form()
                relatoTxt = form1.FILES['subirTxt']
                leer1 = open(relatoTxt, 'r')
                mensaje1 = leer1.read()
                print(mensaje1)
                leer1.close()
                print('QUe paso cdfds')
            elif action == 'subir_aud':
                print("Subir Audio sdfd")
                form1 = self.get_form()
                audio = request.FILES['subirAudio']

                r = sr.Recognizer()
                r.energy_threshold = 300
                with sr.AudioFile(audio) as source:
                    r.adjust_for_ambient_noise(source, duration=1)
                    # sonido = r.listen(source)
                    sonido = r.record(source)
                    try:
                        print('Reading the audio')
                        text = r.recognize_google(sonido, language='es-ES')
                        print(text)
                    except:
                        print('Losiento no se puede entender...')
                data['audio'] = text
            elif action == 'voz':
                r = sr.Recognizer()
                # r.pause_threshold = 0.8;
                r.dynamic_energy_threshold = True;
                # r.energy_threshold = 300;
                r.operation_timeout = 5;

                with sr.Microphone() as source:
                    print('Habla .....')
                    r.adjust_for_ambient_noise(source, duration=1)
                    audio = r.listen(source, timeout=5)
                    try:
                        text = r.recognize_google(audio, language='es-ES')
                        print(text)
                    except:
                        print("Perdon, pero no entiendo")
                        data['error'] = 'No se entiende'
                data['voz'] = text
            elif action == 'pre_procesar':

                usuario = request.POST['nombreUsuario']
                texto = request.POST['relatoUsuario']
                acciones = procesar(usuario, texto)
                auxiliar = Auxiliar(relatoUsuario=texto)
                auxiliar.save()

                for index, frase in enumerate(acciones):
                    nuevo = Accion(actor=frase['usuario'], que=frase['que'], para_que=frase['para_que'],
                                   posicion=index + 1, aux_id=auxiliar.id)
                    nuevo.save()

                data['url'] = reverse_lazy('accion')

            else:
                data['error'] = "No ha ingresado a ninguna opcion"
        except Exception as e:
            print('Ingreso a la excepcion')
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Historia de Usuario'
        context['acciones'] = reverse_lazy('prueba')
        context['mensaje'] = 'Bienvenido'
        return context


class IndexView(TemplateView):
    template_name = 'index.html'


class Accion_1(ListView):
    template_name = 'pantallas/acciones_1.html'
    model = Auxiliar
    success_url = reverse_lazy('prueba')

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                print('Entro aqui sfdsfd dfd')
                variable = Auxiliar.objects.all().last()

                acciones = Accion.objects.filter(aux_id=variable.id)

                data = []
                for frase in acciones:
                    item = {}
                    item['usuario'] = frase.actor
                    item['que'] = frase.que
                    item['para_que'] = frase.para_que
                    item['posicion'] = frase.posicion
                    data.append(item)
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)

        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Lista de Acciones'
        context['sub_title'] = 'Lista de Historias de Usuario Encontradas'
        context['ingreso_url'] = reverse_lazy('prueba')
        context['entity'] = 'Categorias'
        context['mensaje'] = 'Historias de Usuario'
        context['backlog'] = reverse_lazy('backlog')
        return context


class Backlog(ListView):
    template_name = 'pantallas/backlog.html'
    model = Auxiliar
    success_url = reverse_lazy('prueba')

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                print('Entro aqui sfdsfd dfd')
                variable = Auxiliar.objects.all().last()

                acciones = Accion.objects.filter(aux_id=variable.id)

                data = []
                for frase in acciones:
                    item = {}
                    item['id'] = frase.id
                    item['usuario'] = frase.actor
                    item['que'] = frase.que
                    item['para_que'] = frase.para_que
                    item['posicion'] = frase.posicion
                    data.append(item)

            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)

        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Product Backlog'
        context['sub_title'] = 'Product Backlog'
        context['acciones_url'] = reverse_lazy('accion')
        context['entity'] = 'Categorias'
        context['mensaje'] = 'Historias de Usuario'
        return context

class Grafico(ListView):
    model = Accion
    form_class = AccionForm
    template_name = 'pantallas/grafico.html'
    model = Auxiliar
    success_url = reverse_lazy('prueba')

    @method_decorator(csrf_exempt)
    def dispath(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                print('Entro aqui sfdsfd dfd')
                variable = Auxiliar.objects.all().last()

                acciones = Accion.objects.filter(aux_id=variable.id)

                data = []
                for frase in acciones:
                    item = {}
                    item['id'] = frase.id
                    item['usuario'] = frase.actor
                    item['que'] = frase.que
                    item['para_que'] = frase.para_que
                    item['posicion'] = frase.posicion
                    data.append(item)

            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)

        return JsonResponse(data, safe=False)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Microservicios'
        context['sub_title'] = 'Grafico de los Microservicios'
        context['ingreso_url'] = reverse_lazy('prueba')
        context['entity'] = 'Microservicios'
        context['formAccion'] = AccionForm()
        return context





class Acciones(ListView):
    template_name = 'pantallas/Acciones.html'
    model = Auxiliar
    success_url = reverse_lazy('prueba')

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                print("Hola entro a la accion")

            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)

        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Lista de Acciones'
        context['sub_title'] = 'Lista de Historias de Usuario Encontradas'
        context['ingreso_url'] = reverse_lazy('prueba')
        context['entity'] = 'Categorias'
        return context


