from django.shortcuts import render
from core.models import LiderazgoFemenino, LiderazgoPublicaciones, ProyectosITT, FONDEF_categorias, FONDEF_financiamiento, Academicosdap_acreditados, Academicosdap_tipos
from django.contrib.humanize.templatetags.humanize import intcomma

def home(request):
    return render(request, 'home.html')
    
def repositorio(request):
    return render(request, 'repositorio.html')

def lineas_accion(request):
    return render(request, 'lineas_accion.html')

def la1(request):
    return render(request, 'lineas_accion_1.html')

def graficos_l2(request):

    # Datos para el gráfico de liderazgo femenino
    lf = LiderazgoFemenino.objects.all()

    # Filtrar los datos para el año 2022
    lf_2022 = lf.filter(año=2022)
    categorias_2022 = list(lf_2022.values_list('categoria', flat=True))
    total_mujeres_2022 = list(lf_2022.values_list('total_mujeres', flat=True))
    total_hombres_2022 = list(lf_2022.values_list('total_hombres', flat=True))

    # Filtrar los datos para el año 2023
    lf_2023 = lf.filter(año=2023)
    categorias_2023 = list(lf_2023.values_list('categoria', flat=True))
    total_mujeres_2023 = list(lf_2023.values_list('total_mujeres', flat=True))
    total_hombres_2023 = list(lf_2023.values_list('total_hombres', flat=True))

    lp= LiderazgoPublicaciones.objects.all()

    años = list(lp.values_list('año', flat=True))
    total_mujeres = list(lp.values_list('total_mujeres', flat=True))
    total_hombres = list(lp.values_list('total_hombres', flat=True))
    total_publicaciones = list(lp.values_list('total_publicaciones', flat=True))

    pitt = ProyectosITT.objects.all()
    
    años_itt = list(pitt.values_list('año', flat=True))
    total_itt_mujeres = list(pitt.values_list('total_mujeres', flat=True))
    total_itt_hombres = list(pitt.values_list('total_hombres', flat=True))

    context = {
        'años': años,
        'total_mujeres': total_mujeres,
        'total_hombres': total_hombres,
        'total_publicaciones': total_publicaciones,
        'años_itt': años_itt,
        'total_itt_mujeres': total_itt_mujeres,
        'total_itt_hombres': total_itt_hombres,
        'categorias_2022': categorias_2022,
        'total_mujeres_2022': total_mujeres_2022,
        'total_hombres_2022': total_hombres_2022,
        'categorias_2023': categorias_2023,
        'total_mujeres_2023': total_mujeres_2023,
        'total_hombres_2023': total_hombres_2023,
    }

    return render(request, 'lineas_accion_2.html', context)

def graficos_l3(request):

    fc = FONDEF_categorias.objects.all()

    fc_2022 = fc.filter(año=2022)
    categorias_2022 = list(fc_2022.values_list('categoria', flat=True))
    total_mujeres_2022 = list(fc_2022.values_list('total_mujeres', flat=True))
    total_hombres_2022 = list(fc_2022.values_list('total_hombres', flat=True))

    fc_2023 = fc.filter(año=2023)
    categorias_2023 = list(fc_2023.values_list('categoria', flat=True))
    total_mujeres_2023 = list(fc_2023.values_list('total_mujeres', flat=True))
    total_hombres_2023 = list(fc_2023.values_list('total_hombres', flat=True))

    años = list(fc.values_list('año', flat=True))

    ff = FONDEF_financiamiento.objects.all()

    ff_2020 = ff.filter(año=2020)
    financiamiento_mujeres_2020 = list(ff_2020.values_list('financiamiento_mujeres', flat=True))
    financiamiento_hombres_2020 = list(ff_2020.values_list('financiamiento_hombres', flat=True))
    financiamiento_total_2020 = list(ff_2020.values_list('financiamiento_total', flat=True))

    ff_2021 = ff.filter(año=2021)
    financiamiento_mujeres_2021 = list(ff_2021.values_list('financiamiento_mujeres', flat=True))
    financiamiento_hombres_2021 = list(ff_2021.values_list('financiamiento_hombres', flat=True))
    financiamiento_total_2021 = list(ff_2021.values_list('financiamiento_total', flat=True))
    
    ff_2022 = ff.filter(año=2022)
    financiamiento_mujeres_2022 = list(ff_2022.values_list('financiamiento_mujeres', flat=True))
    financiamiento_hombres_2022 = list(ff_2022.values_list('financiamiento_hombres', flat=True))
    financiamiento_total_2022 = list(ff_2022.values_list('financiamiento_total', flat=True))

    ff_2023 = ff.filter(año=2023)
    financiamiento_mujeres_2023 = list(ff_2023.values_list('financiamiento_mujeres', flat=True))
    financiamiento_hombres_2023 = list(ff_2023.values_list('financiamiento_hombres', flat=True))
    financiamiento_total_2023 = list(ff_2023.values_list('financiamiento_total', flat=True))

    años_ff = list(ff.values_list('año', flat=True))

    context = {
        'años': años,
        'años_ff': años_ff,
        'categorias_2022': categorias_2022,
        'total_mujeres_2022': total_mujeres_2022,
        'total_hombres_2022': total_hombres_2022,
        'categorias_2023': categorias_2023,
        'total_mujeres_2023': total_mujeres_2023,
        'total_hombres_2023': total_hombres_2023,
        'financiamiento_mujeres_2020': financiamiento_mujeres_2020,
        'financiamiento_hombres_2020': financiamiento_hombres_2020,
        'financiamiento_total_2020': financiamiento_total_2020,
        'financiamiento_mujeres_2021': financiamiento_mujeres_2021,
        'financiamiento_hombres_2021': financiamiento_hombres_2021,
        'financiamiento_total_2021': financiamiento_total_2021,
        'financiamiento_mujeres_2022': financiamiento_mujeres_2022,
        'financiamiento_hombres_2022': financiamiento_hombres_2022,
        'financiamiento_total_2022': financiamiento_total_2022,
        'financiamiento_mujeres_2023': financiamiento_mujeres_2023,
        'financiamiento_hombres_2023': financiamiento_hombres_2023,
        'financiamiento_total_2023': financiamiento_total_2023,
    }

    return render(request, 'lineas_accion_3.html', context)

def obtener_datos_programa():
    tdap = Academicosdap_tipos.objects.all()
    data = []
    for programa in tdap:
        data.append({
            'tipo_programa': programa.tipo_programa,
            'sexo': programa.sexo,
            'colaborador': programa.colaborador,
            'claustro': programa.claustro,
            'nucleo': programa.nucleo,
            'permanente': programa.permanente,
            'visitante': programa.visitante,
        })
    return data

def graficos_l4(request):

    # tdap = Academicosdap_tipos.objects.all()
    datos_programas = obtener_datos_programa()

    adap = Academicosdap_acreditados.objects.all()

    programas = []
    datos_mujeres = []
    datos_hombres = []

    for registro in adap:
        programas.append(registro.programa_postgrado)
        datos_mujeres.append(registro.total_mujeres)
        datos_hombres.append(registro.total_hombres)

    contexto = {
        'programas': programas,
        'datos_mujeres': datos_mujeres,
        'datos_hombres': datos_hombres,
        'datos_programas': datos_programas,
        
    }
    return render(request, 'lineas_accion_4.html', contexto)

