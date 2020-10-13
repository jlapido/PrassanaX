from django.shortcuts import render
from django.views import generic
from .models import Usuario, Clase, ClaseAlumno
from django.contrib.auth.mixins import LoginRequiredMixin


def index(request):
    # Función vista para la página inicio del sitio.

    # Genera contadores de algunos de los objetos principales

    # Renderiza la plantilla HTML index.html con los datos en la variable contexto
    return render(
        request,
        'index.html',
    )


# Create your views here.


class AvailableClassesListView(LoginRequiredMixin, generic.ListView):
    """
    Generic class-based view listing all available classes to the user.
    """
    model = Clase
    template_name = 'reserva/available_class_list.html'
    paginate_by = 10

    def get_queryset(self):
        return Clase.objects.all().order_by('DiaHora')

    """
    def get_querysets(self):
        return Clase.objects.filter(alumnoID=self.request.user).order_by('DiaHora')
    """


