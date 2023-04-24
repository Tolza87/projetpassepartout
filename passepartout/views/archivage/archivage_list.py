from django.views.generic import ListView

from appli.models import Archivage

class ArchivageListView(ListView):
    model = Archivage
    template_name = "archivage/archivage_list.html"
