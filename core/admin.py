from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import AcademicosDAP, PIDitt, LiderazgoFemenino, LiderazgoPublicaciones, ProyectosITT
from .resource import AcademicosDAPResource, PIDittResource, LiderazgoFemeninoResource, LiderazgoPublicacionesResource, ProyectosITTResource

# Register your models here.
class AcademicosDAPAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = AcademicosDAPResource
    list_display = ('rut', 'nombre', 'area_acreditacion', 'tipo_programa', 'contrato', 'vigencia')

class PIDittAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = PIDittResource
    list_display = ('año', 'total_mujeres', 'total_hombres', 'total_pi')    

class LiderazgoFemeninoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = LiderazgoFemeninoResource
    list_display = ('año', 'categoria', 'total_mujeres', 'total_hombres')

class LiderazgoPublicacionesAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = LiderazgoPublicacionesResource
    list_display = ('año', 'total_mujeres', 'total_hombres', 'total_publicaciones')

class ProyectosITTAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = ProyectosITTResource
    list_display = ('año', 'total_mujeres', 'total_hombres', 'total_proyectos')

admin.site.register(AcademicosDAP, AcademicosDAPAdmin)
admin.site.register(PIDitt, PIDittAdmin)
admin.site.register(LiderazgoFemenino, LiderazgoFemeninoAdmin)
admin.site.register(LiderazgoPublicaciones, LiderazgoPublicacionesAdmin)
admin.site.register(ProyectosITT, ProyectosITTAdmin)