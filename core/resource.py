from import_export import resources, fields
from .models import AcademicosDAP, PIDitt, LiderazgoFemenino, LiderazgoPublicaciones, ProyectosITT, FONDEF_categorias, FONDEF_financiamiento, Academicosdap_acreditados

class AcademicosDAPResource(resources.ModelResource):
    class Meta:
        model = AcademicosDAP
        import_id_fields = ['rut']

class PIDittResource(resources.ModelResource):
    class Meta:
        model = PIDitt
        import_id_fields = ['año']

class LiderazgoFemeninoResource(resources.ModelResource):
    class Meta:
        model = LiderazgoFemenino
        import_id_fields = ['año', 'categoria']

class LiderazgoPublicacionesResource(resources.ModelResource):
    class Meta:
        model = LiderazgoPublicaciones
        import_id_fields = ['año']

class ProyectosITTResource(resources.ModelResource):
    class Meta:
        model = ProyectosITT
        import_id_fields = ['año']

class FONDEF_categoriasResource(resources.ModelResource):
    class Meta:
        model = FONDEF_categorias
        import_id_fields = ['año']

class FONDEF_financiamientoResource(resources.ModelResource):
    class Meta:
        model = FONDEF_financiamiento
        import_id_fields = ['año']


class Academicosdap_acreditadosResource(resources.ModelResource):
    class Meta:
        model = Academicosdap_acreditados
        import_id_fields = ['año']