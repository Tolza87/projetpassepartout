from django.views.generic import ListView

from appli.models import Utilisateur

class UtilisateurListView(ListView):
    model = Utilisateur
    template_name = "utilisateur/utilisateur_list.html"
