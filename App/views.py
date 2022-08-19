from multiprocessing import context
from urllib import request
from django.shortcuts import render
from django.http import HttpResponse
from App.forms import FormDeveloppeur, FormProjet, FormResponsable, FormTache
from App.models import Projet, Relation_Projet_Tache, Tache
from django.shortcuts import redirect

def projets(request):
    projets = Projet.objects.all()
    return render(request, 'projets.html',
    {'projets':projets})

def supprimerUnProjet(request, projet_id):
    projet = Projet.objects.get(pk=projet_id)
    projet.delete()
    return redirect('projets')  
     
def ajouterUnProjet(request):
    if (request.method == "POST"):
        formProjet=FormProjet(request.POST)
        if formProjet.is_valid():
            formProjet.save()
            return redirect('projets')
    else:        
        formProjet = FormProjet
        return render (request, 'formProjet.html', {'formProjet':FormProjet})

def ajouterResponsable(request):
    if (request.method == "POST"):
        formResponsable=FormResponsable(request.POST)
        if formResponsable.is_valid():
            formResponsable.save()
            return redirect('projets')
    else: 
        formResponsable=FormResponsable
        return render (request, 'formResponsable.html', {'formResponsable':FormResponsable})

def ajouterDeveloppeur(request):
    if (request.method == "POST"):
        formDeveloppeur=FormDeveloppeur(request.POST)
        if formDeveloppeur.is_valid():
            formDeveloppeur.save()
            return redirect('projets')
    else: 
        formDeveloppeur=FormDeveloppeur
        return render (request, 'formDeveloppeur.html', {'formDeveloppeur':FormDeveloppeur})



def detailsProjet(request, projet_id):
    projet = Projet.objects.get(pk=projet_id)
    return render(request, 'detailsProjet.html', { "projet": projet })
    
def ajouterUneTache(request, projet_id):
    if(request.method == "POST"):
        formTache=FormTache(request.POST)
        if formTache.is_valid():
            formTache.save()
            relation_projet_tache = Relation_Projet_Tache()
            relation_projet_tache.id_projet = Projet.objects.get(pk=projet_id)
            relation_projet_tache.id_tache = formTache.instance
            relation_projet_tache.save()
            return redirect('detailsProjet', projet_id = projet_id)
    else:        
        formTache= FormTache
        return render(request,'formTache.html',{'formTache':FormTache})

def supprimerUneTache(request, tache_id, projet_id):
    tache = Tache.objects.get(pk=tache_id)
    tache.delete()
    return redirect('detailsProjet', projet_id=projet_id) 

def detailsTache(request, tache_id):
    tache = Tache.objects.get(pk=tache_id)
    return render(request, 'detailsTache.html', { "tache": tache })

def modifierProjet(request, projet_id):
    projet = Projet.objects.get(id = projet_id)
    if (request.method == "POST"): 
        formData= FormProjet(request.POST or None, instance=projet)
        if formData.is_valid():
            formData.save()
            return redirect('detailsProjet', projet_id = formData.instance.id)
    else:
        formData = FormProjet(instance=projet)
        return render(request,'formProjet.html',{'formProjet': formData})       