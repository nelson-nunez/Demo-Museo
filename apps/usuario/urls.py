
from django.conf.urls import url
#from apps.usuario.views import RegistroUsuario
from . import views

app_name = 'usuario'
urlpatterns = [
   #url(r'^registrar/', RegistroUsuario.as_view(), name="registrar")
  # url(r'^registrar/',views.RegistroUsuario, name="registrar"),		

]
