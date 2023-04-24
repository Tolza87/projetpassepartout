from django.views.generic import DetailView

from appli.models import Archivage


class ArchivageDetailView(DetailView):
    model = Archivage
    template_name = "archivage/archivage_detail.html"
