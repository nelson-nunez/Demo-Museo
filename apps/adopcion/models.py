from django.db import models

# Create your models here.
class Persona(models.Model):
	nombre = models.CharField(max_length = 50)
	sexo = models.CharField(max_length = 50)
	edad = models.IntegerField()
	email = models.EmailField()
	#fecha_rescate = models.DateField()
	domicilio = models.TextField()
	
	def __str__(self):

		return self.nombre

