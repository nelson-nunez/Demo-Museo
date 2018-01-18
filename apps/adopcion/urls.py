

from django.conf.urls import url
from . import views

app_name = 'adopcion'
urlpatterns = [
   	url(r'^ver_persona/',views.ver_persona, name="ver_persona"),		
    #url(r'^ver_colaboradores/', views.ver_colaboradores, name="ver_colaboradores"),
    url(r'^persona_form/',views.persona_view, name="persona_form"),
]
