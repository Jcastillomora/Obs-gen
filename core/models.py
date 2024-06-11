from django.db import models

# Create your models here.
class AcademicosDAP(models.Model):
    rut = models.CharField(max_length=10)
    nombre = models.CharField(max_length=100)
    area_acreditacion = models.CharField(max_length=100)
    tipo_programa = models.CharField(max_length=100)
    contrato = models.CharField(max_length=100)
    vigencia = models.CharField(max_length=100)

class PIDitt(models.Model):
    año = models.IntegerField()
    total_mujeres = models.IntegerField()
    total_hombres = models.IntegerField()
    total_pi = models.IntegerField()

class LiderazgoFemenino(models.Model):
    año = models.IntegerField()
    categoria = models.CharField(max_length=200)
    total_mujeres = models.IntegerField()
    total_hombres = models.IntegerField()

class LiderazgoPublicaciones(models.Model):
    año = models.IntegerField()
    total_mujeres = models.IntegerField()
    total_hombres = models.IntegerField()
    total_publicaciones = models.IntegerField()

class ProyectosITT(models.Model):
    año = models.IntegerField()
    total_mujeres = models.IntegerField()
    total_hombres = models.IntegerField()
    total_proyectos = models.IntegerField()

class FONDEF_categorias(models.Model):
    año = models.IntegerField()
    categoria = models.CharField(max_length=200)
    total_mujeres = models.IntegerField()
    total_hombres = models.IntegerField()

# pendiente
class FONDEF_financiamiento(models.Model):
    año = models.IntegerField()
    financiamiento_mujeres = models.FloatField()
    financiamiento_hombres = models.FloatField()
    financiamiento_total = models.FloatField()

class Academicosdap_acreditados(models.Model):
    año = models.IntegerField()
    total_mujeres = models.IntegerField()
    total_hombres = models.IntegerField()
    programa_postgrado = models.CharField(max_length=200)