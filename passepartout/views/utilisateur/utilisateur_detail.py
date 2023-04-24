from django.views.generic import DetailView

from appli.models import Utilisateur


class UtilisateurDetailView(DetailView):
    model = Utilisateur
    template_name = "utilisateur/utilisateur_detail.html"
