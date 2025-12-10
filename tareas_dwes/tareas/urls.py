from django.urls import path
from .views import TareaView

urlpatterns = [
    path('tarea/<uuid:pk>/', TareaView.as_view(), name='detalle_tarea'),
]