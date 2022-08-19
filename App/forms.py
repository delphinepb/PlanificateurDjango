from dataclasses import fields
from django.forms import ModelForm

from App.models import Developpeur, Projet, Responsable, Tache

class FormProjet(ModelForm):
    class Meta:
        model = Projet 
        fields =["title", "responsable", "statut_projet", "etat_avancement_projet"]

class FormTache(ModelForm):
    class Meta:
        model = Tache
        fields = ["name","developpeur","description","duree_tache","statut_tache","etat_avancement_tache"]

class FormResponsable(ModelForm):
    class Meta:
        model = Responsable
        fields = ["nom_responsable","prénom_responsable"]

class FormDeveloppeur(ModelForm):
    class Meta:
        model = Developpeur
        fields = ["nom_developpeur","prénom_developpeur"]