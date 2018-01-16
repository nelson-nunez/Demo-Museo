

from django.conf.urls import url
from . import views

app_name = 'mascota'
urlpatterns = [
   # url(r'^$', index),
   	url(r'^reporte_personas_pdf2/$',views.ReportePersonasPDF2.as_view(), name="reporte_personas_pdf2"),		

]
