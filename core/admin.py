from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import AcademicosDAP, PIDitt, LiderazgoFemenino, LiderazgoPublicaciones, ProyectosITT, FONDEF_categorias, FONDEF_financiamiento, Academicosdap_acreditados, Academicosdap_tipos

from .resource import AcademicosDAPResource, PIDittResource, LiderazgoFemeninoResource, LiderazgoPublicacionesResource, ProyectosITTResource, FONDEF_categoriasResource, FONDEF_financiamientoResource, Academicosdap_acreditadosResource, Academicosdap_tiposResource

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

class FONDEF_categoriasAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = FONDEF_categoriasResource
    list_display = ('año', 'categoria', 'total_mujeres', 'total_hombres')

class FONDEF_financiamientoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = FONDEF_financiamientoResource
    list_display = ('año', 'financiamiento_mujeres', 'financiamiento_hombres', 'financiamiento_total')

class Academicosdap_acreditadosAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = Academicosdap_acreditadosResource
    list_display = ('año', 'total_mujeres', 'total_hombres', 'programa_postgrado')

class Academicosdap_tiposAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = Academicosdap_tiposResource
    list_display = ('tipo_programa', 'sexo', 'colaborador', 'claustro', 'nucleo', 'permanente', 'visitante')


admin.site.register(AcademicosDAP, AcademicosDAPAdmin)
admin.site.register(PIDitt, PIDittAdmin)
admin.site.register(LiderazgoFemenino, LiderazgoFemeninoAdmin)
admin.site.register(LiderazgoPublicaciones, LiderazgoPublicacionesAdmin)
admin.site.register(ProyectosITT, ProyectosITTAdmin)
admin.site.register(FONDEF_categorias, FONDEF_categoriasAdmin )
admin.site.register(FONDEF_financiamiento, FONDEF_financiamientoAdmin)
admin.site.register(Academicosdap_acreditados, Academicosdap_acreditadosAdmin)
admin.site.register(Academicosdap_tipos, Academicosdap_tiposAdmin)
admin.site.site_header = 'Observatorio Género y Ciencia'