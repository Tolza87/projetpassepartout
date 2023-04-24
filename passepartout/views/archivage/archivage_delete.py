from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy

from appli.models import Archivage

class ArchivageDeleteView(DeleteView):
    model = Archivage
    template_name = "archivage/archivage_delete.html"
    success_url = reverse_lazy('archivage_list')