from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Persona
class PersonaForm(forms.ModelForm):
	class Meta:
		model = Persona
		fields = [
			'nombre',
			'sexo', 
			'edad',  
			'email', 
			'domicilio',
		]
		labels = {'nombre': 'Nombre',
					'sexo': 'setso', 
					'edad': 'edad',  
					'email': 'mail', 
					'domicilio': 'domicilio'}
		widget = {"nombre":forms.TextInput(), 
				  "sexo":forms.TextInput(),
				  "edad":forms.TextInput(), 
				  "email":forms.TextInput(),
				  "domicilio":forms.TextInput()}
	def __init__(self, *args, **kwargs):

		super(PersonaForm, self).__init__(*args, **kwargs)
		self.fields['edad'].widget.attrs.update({'type' : 'number'})
	#	self.fields['telefono'].widget.attrs.update({'type' : 'number'})
