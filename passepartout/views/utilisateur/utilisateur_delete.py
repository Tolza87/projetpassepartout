from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy

from appli.models import Utilisateur

class UtilisateurDeleteView(DeleteView):
    model = Utilisateur
    template_name = "utilisateur/utilisateur_delete.html"
    success_url = reverse_lazy('utilisateur_list')