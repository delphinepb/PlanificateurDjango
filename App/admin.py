from django.contrib import admin
from App.models import Projet
from App.models import *


admin.site.register(Projet)
admin.site.register(Tache)
admin.site.register(Relation_Projet_Tache)
admin.site.register(Responsable)
admin.site.register(Developpeur)
admin.site.register(Event)