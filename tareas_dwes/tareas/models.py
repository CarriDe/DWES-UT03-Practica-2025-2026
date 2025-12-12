import uuid
from django.db import models

# Create your models here.
class Tarea(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) #689dc8d8-537d-478a-965f-a61a1c7899b2
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True, null=True)
    completada = models.BooleanField(default=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_recordatorio = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.titulo