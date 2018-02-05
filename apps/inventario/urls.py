

from django.conf.urls import url
from . import views

app_name = 'inventario'
urlpatterns = [
   # url(r'^$', index),
   	url(r'^reporte_personas_pdf2/$',views.ReportePersonasPDF2.as_view(), name="reporte_personas_pdf2"),		
	#url(r'^agregar_piezas/', views.inscribir_piezas, name="agregar_piezas"),
	url(r'^buscar_piezas/', views.buscar_piezas, name="buscar_piezas"),
	url(r'^ver_piezas/', views.ver_piezas, name="ver_piezas"),
	url(r'^agregar_piezas/', views.agregar_piezas, name="agregar_piezas"),

]
