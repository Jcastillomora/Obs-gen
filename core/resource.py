from import_export import resources, fields
from .models import AcademicosDAP, PIDitt, LiderazgoFemenino, LiderazgoPublicaciones, ProyectosITT

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
