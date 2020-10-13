from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from datetime import date


class Usuario(AbstractUser):
    usuario_id = models.AutoField(primary_key=True)


class Clase(models.Model):
    """
    Modelo de la clase Clase, donde guardamos fecha, hora, profesor y plazas libres de cada clase.
    """

    # Campos
    claseID = models.AutoField(primary_key=True, help_text="Identificador de la clase")
    Dia = models.DateField(help_text='Fecha en que se imparte la clase')
    Hora = models.CharField(max_length=6)
    profesor = models.CharField(max_length=20, blank=True)
    PlazasLibres = models.SmallIntegerField(blank=True)
    ...

    # Metadata

    class Meta:
        ordering = ["Dia"]

    """

    # Métodos
    def get_absolute_url(self):

        Devuelve la url para acceder a una instancia particular de MyModelName.

        return reverse('model-detail-view', args=[str(self.id)])
    """

    def __str__(self):
        # Cadena para representar el objeto Clase (en el sitio de Admin, etc.)

        return "Clase {}. Fecha {}. Profesor {}.".format(self.claseID, self.DiaHora, self.profesor)

    @property
    def is_past(self):
        if self.Dia and date.today() > self.DiaHora:
            return True
        return False


class ClaseAlumno(models.Model):
    """
    Modelo de la clase ClaseAlumno, derivado desde la clase Model.
    """
    Referencia = models.AutoField(primary_key=True)
    claseID = models.ForeignKey('Clase', on_delete=models.SET_NULL, null=True, blank=True)
    alumnoID = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        # Cadena para representar el objeto ClaseAlumno (en el sitio de Admin, etc.)

        return "Referencia {}. Id de la clase {}. Id del alumno {}.".format(self.Referencia, self.claseID,
                                                                            self.alumnoID)

