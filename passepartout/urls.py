"""passepartout URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from passepartout.views import VariureDeleteView
from passepartout.views import VariureUpdateView
from passepartout.views import VariureDetailView
from passepartout.views import VariureCreateView
from passepartout.views import VariureListView
from passepartout.views import UtilisateurDeleteView
from passepartout.views import UtilisateurUpdateView
from passepartout.views import UtilisateurDetailView
from passepartout.views import UtilisateurCreateView
from passepartout.views import UtilisateurListView
from passepartout.views import TypeExemplaireDeleteView
from passepartout.views import TypeExemplaireUpdateView
from passepartout.views import TypeExemplaireDetailView
from passepartout.views import TypeExemplaireCreateView
from passepartout.views import TypeExemplaireListView
from passepartout.views import SalleDeleteView
from passepartout.views import SalleUpdateView
from passepartout.views import SalleDetailView
from passepartout.views import SalleCreateView
from passepartout.views import SalleListView
from passepartout.views import RolesDeleteView
from passepartout.views import RolesUpdateView
from passepartout.views import RolesDetailView
from passepartout.views import RolesCreateView
from passepartout.views import RolesListView
from passepartout.views import PouvoirDeleteView
from passepartout.views import PouvoirUpdateView
from passepartout.views import PouvoirDetailView
from passepartout.views import PouvoirCreateView
from passepartout.views import PouvoirListView
from passepartout.views import PosseseurDeCLefDeleteView
from passepartout.views import PosseseurDeCLefUpdateView
from passepartout.views import PosseseurDeCLefDetailView
from passepartout.views import PosseseurDeCLefCreateView
from passepartout.views import PosseseurDeCLefListView
from passepartout.views import PorteDeleteView
from passepartout.views import PorteUpdateView
from passepartout.views import PorteDetailView
from passepartout.views import PorteCreateView
from passepartout.views import PorteListView
from passepartout.views import PersonneDeleteView
from passepartout.views import PersonneUpdateView
from passepartout.views import PersonneDetailView
from passepartout.views import PersonneCreateView
from passepartout.views import PersonneListView
from passepartout.views import OuvreDeleteView
from passepartout.views import OuvreUpdateView
from passepartout.views import OuvreDetailView
from passepartout.views import OuvreCreateView
from passepartout.views import OuvreListView
from passepartout.views import ExemplaireDeleteView
from passepartout.views import ExemplaireUpdateView
from passepartout.views import ExemplaireDetailView
from passepartout.views import ExemplaireCreateView
from passepartout.views import ExemplaireListView
from passepartout.views import BatimentDeleteView
from passepartout.views import BatimentUpdateView
from passepartout.views import BatimentDetailView
from passepartout.views import BatimentCreateView
from passepartout.views import BatimentListView
from passepartout.views import BarilletDeleteView
from passepartout.views import BarilletUpdateView
from passepartout.views import BarilletDetailView
from passepartout.views import BarilletCreateView
from passepartout.views import BarilletListView
from passepartout.views import ArchivageDeleteView
from passepartout.views import ArchivageUpdateView
from passepartout.views import ArchivageDetailView
from passepartout.views import ArchivageCreateView
from passepartout.views import ArchivageListView
from passepartout.views import AppartenirDeleteView
from passepartout.views import AppartenirUpdateView
from passepartout.views import AppartenirDetailView
from passepartout.views import AppartenirCreateView
from passepartout.views import AppartenirListView

urlpatterns = [
    path("", include("appli.urls")),
    path("admin/", admin.site.urls),
    path('appartenir/list/', AppartenirListView.as_view(), name='appartenir_list'),
    path('appartenir/create/', AppartenirCreateView.as_view(), name='appartenir_create'),
    path('appartenir/detail/<int:pk>/', AppartenirDetailView.as_view(), name='appartenir_detail'),
    path('appartenir/update/<int:pk>/', AppartenirUpdateView.as_view(), name='appartenir_update'),
    path('appartenir/delete/<int:pk>/', AppartenirDeleteView.as_view(), name='appartenir_delete'),
    path('archivage/list/', ArchivageListView.as_view(), name='archivage_list'),
    path('archivage/create/', ArchivageCreateView.as_view(), name='archivage_create'),
    path('archivage/detail/<int:pk>/', ArchivageDetailView.as_view(), name='archivage_detail'),
    path('archivage/update/<int:pk>/', ArchivageUpdateView.as_view(), name='archivage_update'),
    path('archivage/delete/<int:pk>/', ArchivageDeleteView.as_view(), name='archivage_delete'),
    path('barillet/list/', BarilletListView.as_view(), name='barillet_list'),
    path('barillet/create/', BarilletCreateView.as_view(), name='barillet_create'),
    path('barillet/detail/<int:pk>/', BarilletDetailView.as_view(), name='barillet_detail'),
    path('barillet/update/<int:pk>/', BarilletUpdateView.as_view(), name='barillet_update'),
    path('barillet/delete/<int:pk>/', BarilletDeleteView.as_view(), name='barillet_delete'),
    path('batiment/list/', BatimentListView.as_view(), name='batiment_list'),
    path('batiment/create/', BatimentCreateView.as_view(), name='batiment_create'),
    path('batiment/detail/<int:pk>/', BatimentDetailView.as_view(), name='batiment_detail'),
    path('batiment/update/<int:pk>/', BatimentUpdateView.as_view(), name='batiment_update'),
    path('batiment/delete/<int:pk>/', BatimentDeleteView.as_view(), name='batiment_delete'),
    path('exemplaire/list/', ExemplaireListView.as_view(), name='exemplaire_list'),
    path('exemplaire/create/', ExemplaireCreateView.as_view(), name='exemplaire_create'),
    path('exemplaire/detail/<int:pk>/', ExemplaireDetailView.as_view(), name='exemplaire_detail'),
    path('exemplaire/update/<int:pk>/', ExemplaireUpdateView.as_view(), name='exemplaire_update'),
    path('exemplaire/delete/<int:pk>/', ExemplaireDeleteView.as_view(), name='exemplaire_delete'),
    path('ouvre/list/', OuvreListView.as_view(), name='ouvre_list'),
    path('ouvre/create/', OuvreCreateView.as_view(), name='ouvre_create'),
    path('ouvre/detail/<int:pk>/', OuvreDetailView.as_view(), name='ouvre_detail'),
    path('ouvre/update/<int:pk>/', OuvreUpdateView.as_view(), name='ouvre_update'),
    path('ouvre/delete/<int:pk>/', OuvreDeleteView.as_view(), name='ouvre_delete'),
    path('personne/list/', PersonneListView.as_view(), name='personne_list'),
    path('personne/create/', PersonneCreateView.as_view(), name='personne_create'),
    path('personne/detail/<int:pk>/', PersonneDetailView.as_view(), name='personne_detail'),
    path('personne/update/<int:pk>/', PersonneUpdateView.as_view(), name='personne_update'),
    path('personne/delete/<int:pk>/', PersonneDeleteView.as_view(), name='personne_delete'),
    path('porte/list/', PorteListView.as_view(), name='porte_list'),
    path('porte/create/', PorteCreateView.as_view(), name='porte_create'),
    path('porte/detail/<int:pk>/', PorteDetailView.as_view(), name='porte_detail'),
    path('porte/update/<int:pk>/', PorteUpdateView.as_view(), name='porte_update'),
    path('porte/delete/<int:pk>/', PorteDeleteView.as_view(), name='porte_delete'),
    path('posseseur_de_c_lef/list/', PosseseurDeCLefListView.as_view(), name='posseseur_de_c_lef_list'),
    path('posseseur_de_c_lef/create/', PosseseurDeCLefCreateView.as_view(), name='posseseur_de_c_lef_create'),
    path('posseseur_de_c_lef/detail/<int:pk>/', PosseseurDeCLefDetailView.as_view(), name='posseseur_de_c_lef_detail'),
    path('posseseur_de_c_lef/update/<int:pk>/', PosseseurDeCLefUpdateView.as_view(), name='posseseur_de_c_lef_update'),
    path('posseseur_de_c_lef/delete/<int:pk>/', PosseseurDeCLefDeleteView.as_view(), name='posseseur_de_c_lef_delete'),
    path('pouvoir/list/', PouvoirListView.as_view(), name='pouvoir_list'),
    path('pouvoir/create/', PouvoirCreateView.as_view(), name='pouvoir_create'),
    path('pouvoir/detail/<int:pk>/', PouvoirDetailView.as_view(), name='pouvoir_detail'),
    path('pouvoir/update/<int:pk>/', PouvoirUpdateView.as_view(), name='pouvoir_update'),
    path('pouvoir/delete/<int:pk>/', PouvoirDeleteView.as_view(), name='pouvoir_delete'),
    path('roles/list/', RolesListView.as_view(), name='roles_list'),
    path('roles/create/', RolesCreateView.as_view(), name='roles_create'),
    path('roles/detail/<int:pk>/', RolesDetailView.as_view(), name='roles_detail'),
    path('roles/update/<int:pk>/', RolesUpdateView.as_view(), name='roles_update'),
    path('roles/delete/<int:pk>/', RolesDeleteView.as_view(), name='roles_delete'),
    path('salle/list/', SalleListView.as_view(), name='salle_list'),
    path('salle/create/', SalleCreateView.as_view(), name='salle_create'),
    path('salle/detail/<int:pk>/', SalleDetailView.as_view(), name='salle_detail'),
    path('salle/update/<int:pk>/', SalleUpdateView.as_view(), name='salle_update'),
    path('salle/delete/<int:pk>/', SalleDeleteView.as_view(), name='salle_delete'),
    path('type_exemplaire/list/', TypeExemplaireListView.as_view(), name='type_exemplaire_list'),
    path('type_exemplaire/create/', TypeExemplaireCreateView.as_view(), name='type_exemplaire_create'),
    path('type_exemplaire/detail/<int:pk>/', TypeExemplaireDetailView.as_view(), name='type_exemplaire_detail'),
    path('type_exemplaire/update/<int:pk>/', TypeExemplaireUpdateView.as_view(), name='type_exemplaire_update'),
    path('type_exemplaire/delete/<int:pk>/', TypeExemplaireDeleteView.as_view(), name='type_exemplaire_delete'),
    path('utilisateur/list/', UtilisateurListView.as_view(), name='utilisateur_list'),
    path('utilisateur/create/', UtilisateurCreateView.as_view(), name='utilisateur_create'),
    path('utilisateur/detail/<int:pk>/', UtilisateurDetailView.as_view(), name='utilisateur_detail'),
    path('utilisateur/update/<int:pk>/', UtilisateurUpdateView.as_view(), name='utilisateur_update'),
    path('utilisateur/delete/<int:pk>/', UtilisateurDeleteView.as_view(), name='utilisateur_delete'),
    path('variure/list/', VariureListView.as_view(), name='variure_list'),
    path('variure/create/', VariureCreateView.as_view(), name='variure_create'),
    path('variure/detail/<int:pk>/', VariureDetailView.as_view(), name='variure_detail'),
    path('variure/update/<int:pk>/', VariureUpdateView.as_view(), name='variure_update'),
    path('variure/delete/<int:pk>/', VariureDeleteView.as_view(), name='variure_delete'),
]
