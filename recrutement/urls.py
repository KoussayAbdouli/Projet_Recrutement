from django.urls import path
from . import views
urlpatterns = [
    path('', views.ProgrammeList, name = 'programme'),
    path('ajout_programme', views.AjouterProgramme, name = 'ajouter_prog')

]