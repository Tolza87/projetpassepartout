from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy

from appli.models import Utilisateur

class UtilisateurUpdateView(UpdateView):
    model = Utilisateur
    fields = '__all__'
    template_name = "utilisateur/utilisateur_update.html"
    success_url = reverse_lazy('utilisateur_list')
