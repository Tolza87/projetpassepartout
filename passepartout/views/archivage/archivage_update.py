from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy

from appli.models import Archivage

class ArchivageUpdateView(UpdateView):
    model = Archivage
    fields = '__all__'
    template_name = "archivage/archivage_update.html"
    success_url = reverse_lazy('archivage_list')
