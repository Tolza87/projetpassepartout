from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from appli.models import Utilisateur

class UtilisateurCreateView(CreateView):
    model = Utilisateur
    fields = '__all__'
    template_name = "utilisateur/utilisateur_create.html"
    success_url = reverse_lazy('utilisateur_list')
