#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Passepartout.settings") 
os.environ['DJANGO_SETTINGS_MODULE'] = 'Passepartout.settings' 
settings.configure()

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'passepartout.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

import django

if __name__ == '__main__':
    django.setup()
    # import AFTER setup
    from appli.models import Appartenir
    from appli.models import Archivage
    from appli.models import Barillet
    from appli.models import Batiment
    from appli.models import Exemplaire
    from appli.models import Ouvre
    from appli.models import Personne
    from appli.models import Porte
    from appli.models import PossesseurDeClef
    from appli.models import Pouvoir
    from appli.models import Roles
    from appli.models import Salle
    from appli.models import TypeExemplaire
    from appli.models import Utilisateur
    from appli.models import Variure
