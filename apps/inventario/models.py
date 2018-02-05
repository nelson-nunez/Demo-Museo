from django.db import models
from apps.turnos.models import Persona
# Create your models here.



class Piezas(models.Model):
	nombre = models.CharField(max_length = 50)
	nombre_cientifico = models.CharField(max_length = 50)
	edad_aproximada = models.IntegerField()
	fecha_aproximada = models.DateField()
	persona = models.ForeignKey(Persona, null = True, blank= True, on_delete=models.CASCADE)

	def __str__(self):

		return self.nombre