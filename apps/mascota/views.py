from django.shortcuts import render, redirect
from django.db.models import Sum
from django.http import Http404
from django.contrib.auth.models import User
from .models import Mascota
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



#-----------------------------------------------------

def index (request):
	return HttpResponse("Index")
#-----------------------------------------------------

#-----------------------------------------------------

class ReportePersonasPDF2(View):

    def cabecera(self,pdf):
        #Establecemos el tamaño de letra en 16 y el tipo de letra Helvetica
        pdf.setFont("Helvetica", 16)
        #Dibujamos una cadena en la ubicación X,Y especificada
        pdf.drawString(230, 790, u" Reporte Personalizado")
        pdf.setFont("Helvetica", 14)
        pdf.drawString(200, 770, u"        ---------   Estadísticas   ------- ")
        #Utilizamos el archivo logo_django.png que está guardado en la carpeta media/imagenes
        archivo_imagen = settings.MEDIA_ROOT+'/logo.png'
        #Definimos el tamaño de la imagen a cargar y las coordenadas correspondientes
        pdf.drawImage(archivo_imagen, 70, 730, 120, 80,preserveAspectRatio=True)

    def get(self, request, *args, **kwargs):
        #Indicamos el tipo de contenido a devolver, en este caso un pdf
        response = HttpResponse(content_type='application/pdf')
        #La clase io.BytesIO permite tratar un array de bytes como un fichero binario, se utiliza como almacenamiento temporal
        buffer = BytesIO()
        #Canvas nos permite hacer el reporte con coordenadas X y Y
        pdf = canvas.Canvas(buffer)
        #Llamo al método cabecera donde están definidos los datos que aparecen en la cabecera del reporte.
        self.cabecera(pdf)
        #Con show page hacemos un corte de página para pasar a la siguiente
        pdf.showPage()
        pdf.save()
        pdf = buffer.getvalue()
        buffer.close()
        response.write(pdf)
        return response


    def tabla(self,pdf,y):
        #Creamos una tupla de encabezados para neustra tabla
        
        encabezados = ('Pieza','Nombre Cientifico','Antiguedad','Donada por:')
        #Creamos una lista de tuplas que van a contener a las personas
        detalles2 = [('Museo de la ciudad', ':')]
        detalles = [(mascota.nombre,) for mascota in Mascota.objects.all()]
        #Establecemos el tamaño de cada una de las columnas de la tabla
        # print detalles
        detalle_orden = Table(detalles2 + [encabezados] +  detalles)
        #Aplicamos estilos a las celdas de la tabla
        detalle_orden.setStyle(TableStyle(
        [
            
            ('GRID', (0, 0), (5, -1), 1, colors.black),
            ('LINEBELOW', (0, 0), (-1, 1), 2, colors.black),
            ('BACKGROUND', (0, 0), (-1, 1), colors.grey)
        ]
        ))
        #Establecemos el tamaño de la hoja que ocupará la tabla
        detalle_orden.wrapOn(pdf, 800, 600)
        #Definimos la coordenada donde se dibujará la tabla
        detalle_orden.drawOn(pdf, 90,y)

    def get(self, request, *args, **kwargs):
        
        #Indicamos el tipo de contenido a devolver, en este caso un pdf
        response = HttpResponse(content_type='application/pdf')
        #La clase io.BytesIO permite tratar un array de bytes como un fichero binario, se utiliza como almacenamiento temporal
        buffer = BytesIO()
        #Canvas nos permite hacer el reporte con coordenadas X y Y
        pdf = canvas.Canvas(buffer)
        #Llamo al método cabecera donde están definidos los datos que aparecen en la cabecera del reporte.
        self.cabecera(pdf)
        y= 670
        for mascota in Mascota.objects.all(): 
            y=y-16 
        self.tabla(pdf, y)
        #Con show page hacemos un corte de página para pasar a la siguiente
        #pdf.showPage()
        pdf.save()
        pdf = buffer.getvalue()
        buffer.close()
        response.write(pdf)
        return response

#-----------------------------------------------------
