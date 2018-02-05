
from django import forms
from .models import Piezas
from .models import Persona
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
import apps.inventario
import apps.turnos

class BuscarPiezas(forms.Form):
	query = forms.CharField(label="Ingrese el Nombre la pieza")

class PersonaForm(forms.ModelForm):
	class Meta:
		model = Persona
		fields =   ("nombre",
					"sexo", 
					"edad",  
					"email", 
					"domicilio")
		labels =   {"nombre": "Nombre",
					"sexo": "setso", 
					"edad": "edad",  
					"email": "mail", 
					"domicilio": "domicilio"}
		widget =   {"nombre":forms.TextInput(), 
				    "sexo":forms.TextInput(),
				    "edad":forms.TextInput(), 
				    "email":forms.TextInput(),
				    "domicilio":forms.TextInput()}
	def __init__(self, *args, **kwargs):
		super(PersonaForm, self).__init__(*args, **kwargs)

class PiezasForm(forms.ModelForm):
	class Meta:
		model = Piezas
		fields = ("nombre",				  
				  "nombre_cientifico",
				  "edad_aproximada",
				  "fecha_aproximada")

		labels = {"nombre":"Nombre de la Piezas",
				  "nombre_cientifico":"Nombre cientifico",
				  "edad_aproximada":"Edad aproximada",
				  "fecha_aproximada":"fecha_aproximada",
				  }

		widget = {"nombre":forms.TextInput(), 
				  "nombre_cientifico":forms.TextInput(),
				  "edad_aproximada":forms.DateInput(), 
				  "fecha_aproximada":forms.DateInput(),
				  }		  

	def __init__(self, *args, **kwargs):
		super(PiezasForm, self).__init__(*args, **kwargs)
