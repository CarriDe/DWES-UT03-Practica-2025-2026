from django.views.generic.detail import DetailView
from .models import Tarea

# Create your views here.
class TareaView(DetailView):
    model = Tarea
    template_name = "tareas/detalle_tarea.html"
    context_object_name = "tarea"