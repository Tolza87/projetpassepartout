from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from appli.models import Archivage

class ArchivageCreateView(CreateView):
    model = Archivage
    fields = '__all__'
    template_name = "archivage/archivage_create.html"
    success_url = reverse_lazy('archivage_list')
