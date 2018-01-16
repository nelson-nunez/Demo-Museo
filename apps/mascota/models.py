from django.db import models
from apps.adopcion.models import Persona
# Create your models here.

class Vacuna(models.Model):
	nombre= models.CharField(max_length=50)
	def __str__(self):

		return self.nombre

class Mascota(models.Model):
	SEXO = (("macho","MACHO"),("hembra","HEMBRA"))
	ESPECIE = (("canino","CANINO"),("felino","FELINO"))
	especie = models.CharField(max_length = 10, choices = ESPECIE, null = True)
	sexo = models.CharField(max_length = 10, choices = SEXO, null = True)
	nombre = models.CharField(max_length = 50)
	direccion = models.CharField(max_length = 50)
	edad_aproximada = models.IntegerField()
	fecha_aproximada = models.DateField()
	persona = models.ForeignKey(Persona, null = True, blank= True, on_delete=models.CASCADE)
	vacuna = models.ManyToManyField(Vacuna, blank=True)

	def __str__(self):

		return self.nombre