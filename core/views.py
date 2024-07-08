from django.shortcuts import render
from core.models import LiderazgoFemenino, LiderazgoPublicaciones, ProyectosITT, FONDEF_categorias, FONDEF_financiamiento, Academicosdap_acreditados, Academicosdap_tipos
from django.db.models import Sum

def home(request):
    return render(request, 'home.html')
    
def repositorio(request):
    return render(request, 'repositorio.html')

def lineas_accion(request):
    return render(request, 'lineas_accion.html')

def la1(request):
    return render(request, 'lineas_accion_1.html')

def preparar_datos_anidados(tdap, campo):
    outer_data = {}
    inner_data = []

    for entry in tdap:
        tipo = entry.tipo_programa
        sexo = entry.sexo
        valor = getattr(entry, campo)

        # Solo agregar datos que no sean 0
        if valor != 0:
            # Preparar los datos exteriores
            if tipo not in outer_data:
                outer_data[tipo] = 0
            outer_data[tipo] += valor

            # Preparar los datos interiores
            inner_data.append({
                'name': f'{tipo} ({sexo})',
                'value': valor
            })

    outer_series = [{'name': key, 'value': value} for key, value in outer_data.items()]

    return outer_series, inner_data

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

def graficos_l4(request):

    tdap = Academicosdap_tipos.objects.all()

    data_colaborador, inner_colaborador = preparar_datos_anidados(tdap, 'colaborador')
    data_claustro, inner_claustro = preparar_datos_anidados(tdap, 'claustro')
    data_nucleo, inner_nucleo = preparar_datos_anidados(tdap, 'nucleo')
    data_permanente, inner_permanente = preparar_datos_anidados(tdap, 'permanente')
    data_visitante, inner_visitante = preparar_datos_anidados(tdap, 'visitante')

    adap = Academicosdap_acreditados.objects.all()

    programas = []
    datos_mujeres = []
    datos_hombres = []

    for registro in adap:
        programas.append(registro.programa_postgrado)
        datos_mujeres.append(registro.total_mujeres)
        datos_hombres.append(registro.total_hombres)

    contexto = {
        'data_colaborador': data_colaborador,
        'inner_colaborador': inner_colaborador,
        'data_claustro': data_claustro,
        'inner_claustro': inner_claustro,
        'data_nucleo': data_nucleo,
        'inner_nucleo': inner_nucleo,
        'data_permanente': data_permanente,
        'inner_permanente': inner_permanente,
        'data_visitante': data_visitante,
        'inner_visitante': inner_visitante,
        'programas': programas,
        'datos_mujeres': datos_mujeres,
        'datos_hombres': datos_hombres,
        
    }
    return render(request, 'lineas_accion_4.html', contexto)

