# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Appartenir(models.Model):
    id_barillet = models.OneToOneField('Barillet', models.DO_NOTHING, db_column='id_barillet', primary_key=True)
    id_exemplaire = models.ForeignKey('Exemplaire', models.DO_NOTHING, db_column='id_exemplaire')

    class Meta:
        managed = False
        db_table = 'appartenir'
        unique_together = (('id_barillet', 'id_exemplaire'),)


class Archivage(models.Model):
    id_archive = models.IntegerField(primary_key=True)
    rendu = models.CharField(max_length=50)
    acquisition = models.CharField(max_length=50)
    id_exemplaire = models.ForeignKey('Exemplaire', models.DO_NOTHING, db_column='id_exemplaire')
    id_personne = models.ForeignKey('PossesseurDeClef', models.DO_NOTHING, db_column='id_personne')

    class Meta:
        managed = False
        db_table = 'archivage'


class Barillet(models.Model):
    id_barillet = models.IntegerField(primary_key=True)
    code_clef = models.CharField(max_length=50)
    stock_cle = models.IntegerField()
    type_clÚ = models.CharField(max_length=50)
    id_variure = models.ForeignKey('Variure', models.DO_NOTHING, db_column='id_Variure')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'barillet'


class Batiment(models.Model):
    id_batiment = models.IntegerField(primary_key=True)
    nom_batiment = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'batiment'


class Exemplaire(models.Model):
    id_exemplaire = models.IntegerField(primary_key=True)
    date_posseder = models.CharField(max_length=50)
    code_type = models.ForeignKey('TypeExemplaire', models.DO_NOTHING, db_column='code_type')
    id_personne = models.ForeignKey('PossesseurDeClef', models.DO_NOTHING, db_column='id_personne', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'exemplaire'


class Ouvre(models.Model):
    id_salle = models.OneToOneField('Salle', models.DO_NOTHING, db_column='id_salle', primary_key=True)
    id_porte = models.ForeignKey('Porte', models.DO_NOTHING, db_column='id_porte')

    class Meta:
        managed = False
        db_table = 'ouvre'
        unique_together = (('id_salle', 'id_porte'),)


class Personne(models.Model):
    id_personne = models.IntegerField(primary_key=True)
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    numtelephone = models.IntegerField(db_column='numTelephone')  # Field name made lowercase.
    email = models.CharField(max_length=50)
    adresse = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'personne'


class Porte(models.Model):
    id_porte = models.CharField(primary_key=True, max_length=50)
    id_barillet = models.ForeignKey(Barillet, models.DO_NOTHING, db_column='id_barillet')

    class Meta:
        managed = False
        db_table = 'porte'


class PossesseurDeClef(models.Model):
    id_personne = models.OneToOneField(Personne, models.DO_NOTHING, db_column='id_personne', primary_key=True)
    date_sortie_etablissement = models.DateField(db_column='Date_Sortie_Etablissement')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'possesseur_de_clef'


class Pouvoir(models.Model):
    id_barillet = models.OneToOneField(Barillet, models.DO_NOTHING, db_column='id_barillet', primary_key=True)
    id_personne = models.ForeignKey(Personne, models.DO_NOTHING, db_column='id_personne')

    class Meta:
        managed = False
        db_table = 'pouvoir'
        unique_together = (('id_barillet', 'id_personne'),)


class Roles(models.Model):
    id_role = models.CharField(primary_key=True, max_length=50)
    libelle = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'roles'


class Salle(models.Model):
    id_salle = models.IntegerField(primary_key=True)
    nom_salle = models.CharField(max_length=50)
    id_batiment = models.ForeignKey(Batiment, models.DO_NOTHING, db_column='id_batiment')

    class Meta:
        managed = False
        db_table = 'salle'


class TypeExemplaire(models.Model):
    code_type = models.CharField(primary_key=True, max_length=50)
    type_libelle = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'type_exemplaire'


class Utilisateur(models.Model):
    id_personne = models.OneToOneField(Personne, models.DO_NOTHING, db_column='id_personne', primary_key=True)
    login_hash = models.CharField(max_length=50)
    mdp_hash = models.CharField(max_length=50)
    id_role = models.ForeignKey(Roles, models.DO_NOTHING, db_column='id_role')

    class Meta:
        managed = False
        db_table = 'utilisateur'


class Variure(models.Model):
    id_variure = models.IntegerField(db_column='id_Variure', primary_key=True)  # Field name made lowercase.
    libelle_variure = models.CharField(db_column='Libelle_Variure', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'variure'
