from dataclasses import field
from urllib import request
from django.db import models
from datetime import datetime


class StatutProjetChoices(models.TextChoices):
    enPause = 'En pause', 
    planifie = 'Planifié',
    enCours = 'En cours',
    livre = 'Livré'

class StatutTacheChoices(models.TextChoices):
    enPause = 'En pause', 
    planifie = 'Planifiée',
    enCours = 'En cours',
    realisee = 'Réalisée',
    valide = 'Validée'


class Developpeur(models.Model):
    id = models.BigAutoField(primary_key=True)
    nom_developpeur = models.fields.CharField(max_length=50)
    prénom_developpeur = models.fields.CharField(max_length=50)
    def __str__(self):
        return self.nom_developpeur + ' ' + self.prénom_developpeur

class Tache(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.fields.CharField(max_length=100)
    developpeur = models.fields.CharField(max_length=50)
    description = models.fields.CharField(max_length=500)
    duree_tache = models.fields.CharField(max_length=20)
    statut_tache = models.CharField(
        choices = StatutTacheChoices.choices,
        default=StatutTacheChoices.planifie,
        max_length=50
    )
    etat_avancement_tache = models.fields.CharField(max_length=20)
    developpeur=models.ManyToManyField(Developpeur, through='Relation_Tache_Developpeur')

class Responsable(models.Model):
    id = models.BigAutoField(primary_key=True)
    nom_responsable = models.fields.CharField(max_length=50)
    prénom_responsable = models.fields.CharField(max_length=50)
    def __str__(self):
        return self.nom_responsable + ' ' + self.prénom_responsable


class Projet(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.fields.CharField(max_length=100)
    responsable = models.fields.CharField(max_length=50)
    statut_projet = models.CharField(
        choices = StatutProjetChoices.choices,
        default=StatutProjetChoices.planifie,
        max_length=50
    )
    etat_avancement_projet = models.fields.CharField(max_length=20)
    taches = models.ManyToManyField(Tache, through='Relation_Projet_Tache')
    responsable=models.ManyToManyField(Responsable, through='Relation_Projet_Responsable')
    
class Relation_Projet_Tache(models.Model):
    id_tache= models.ForeignKey(Tache, on_delete=models.CASCADE)
    id_projet=models.ForeignKey(Projet, on_delete=models.CASCADE)


class Relation_Projet_Responsable(models.Model):
    id_projet=models.ForeignKey(Projet, on_delete=models.CASCADE)
    id_responsable=models.ForeignKey(Responsable, on_delete=models.CASCADE)

class Relation_Tache_Developpeur(models.Model):
    id_tache= models.ForeignKey(Tache, on_delete=models.CASCADE)
    id_developpeur=models.ForeignKey(Developpeur, on_delete=models.CASCADE)