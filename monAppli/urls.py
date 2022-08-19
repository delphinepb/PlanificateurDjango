"""monAppli URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from unicodedata import name
from django.contrib import admin
from django.urls import path
from App import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('projets/', views.projets, name='projets'),
    path('projets/supprimer/<int:projet_id>', views.supprimerUnProjet,name='supprimerUnProjet'),
    path('projets/detailsProjet/<int:projet_id>', views.detailsProjet, name='detailsProjet'),
    path('projets/ajouterProjet', views.ajouterUnProjet, name='ajouterUnProjet'),
    path('projets/ajouterResponsable', views.ajouterResponsable, name='ajouterResponsable'),
    path('projet/ajouterDeveloppeur', views.ajouterDeveloppeur, name='ajouterDeveloppeur'),
    path('projets/<int:projet_id>/ajouterTache', views.ajouterUneTache,name='ajouterUneTache'),
    path('projets/<int:projet_id>/supprimer/<int:tache_id>', views.supprimerUneTache,name='supprimerUneTache'),
    path('projets/detailsTache/<int:tache_id>', views.detailsTache, name='detailsTache'),
    path('projets/<int:projet_id>/modifier', views.modifierProjet, name='modifierProjet')

]
