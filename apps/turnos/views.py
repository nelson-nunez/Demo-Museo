from django.shortcuts import render, redirect
from django.db.models import Sum
from django.http import Http404
from django.contrib.auth.models import User
from .models import Persona
#-------------------------------------------------------
from django.conf import settings
from io import BytesIO
from reportlab.pdfgen import canvas
from django.views.generic import View
from django.http import HttpResponse
from django.views.generic import ListView
from reportlab.platypus import SimpleDocTemplate, Paragraph, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.platypus import Table
#-----------------------------------------------------

#from apps.adopcion.forms import PersonaForm
from .forms import PersonaForm
#-----------------------------------------------------

def index (request):
	return HttpResponse("Index")
#-----------------------------------------------------

def ver_persona(request):
    personas = Persona.objects.all().order_by('nombre')
    #campania = Campaing.objects.get(id=id)

    return render(request, 'ver_persona.html', {'personas':personas})

def persona_view(request):
	if request.method == 'POST':
		form = PersonaForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('/ver_persona')
	else: 
		form = PersonaForm()
	
	return render(request, 'persona_form.html',{'form':form})