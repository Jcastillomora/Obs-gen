from django.shortcuts import render
from core.models import LiderazgoFemenino, LiderazgoPublicaciones, ProyectosITT, FONDEF_categorias, FONDEF_financiamiento, Academicosdap_acreditados, Academicosdap_tipos
import plotly.graph_objs as go

def home(request):
    return render(request, 'home.html')
    
def repositorio(request):
    return render(request, 'repositorio.html')

def lineas_accion(request):
    return render(request, 'lineas_accion.html')

def la1(request):
    return render(request, 'lineas_accion_1.html')

def plot3(request):

    def add_percentage_symbol(values):
        return [f'{value:.0f}%' for value in values]

    # Usar datos de FONDEF_categorias
    fc = FONDEF_categorias.objects.all()

    # Usar datos de FONDEF_financiamiento
    ff = FONDEF_financiamiento.objects.all()

    # Filtrar los datos de FONDEF_financiamiento
    años_ff = list(ff.values_list('año', flat=True))
    financiamiento_mujeres = list(ff.values_list('financiamiento_mujeres', flat=True))
    financiamiento_hombres = list(ff.values_list('financiamiento_hombres', flat=True))
    financiamiento_total = list(ff.values_list('financiamiento_total', flat=True))

    # Filtrar los datos de FONDEF_categorias
    años = list(fc.values_list('año', flat=True))
    categorias = list(fc.values_list('categoria', flat=True))
    total_mujeres = list(fc.values_list('total_mujeres', flat=True))
    total_hombres = list(fc.values_list('total_hombres', flat=True))

    total_mujeres = add_percentage_symbol(total_mujeres)
    total_hombres = add_percentage_symbol(total_hombres)

    fig = go.Figure()
    
    # Crear gráfico de barras para FONDEF_categorias por cada año
    años_unicos = sorted(set(años))

    for año in años_unicos:
        categorias_año = [categorias[i] for i in range(len(años)) if años[i] == año]
        total_mujeres_año = [total_mujeres[i] for i in range(len(años)) if años[i] == año]
        total_hombres_año = [total_hombres[i] for i in range(len(años)) if años[i] == año]

        fig.add_trace(
            go.Bar(name=f'Mujeres {año}', 
                   x=categorias_año, 
                   y=total_mujeres_año, 
                   marker=dict(color='rgba(255,174,255,0.5)', 
                               line=dict(color='rgb(0,0,0)', width=1)),
                   text=total_mujeres_año,
                   hovertemplate='Mujeres: %{y}%<extra></extra>',
                   textposition='auto', 
                   textangle=0,
                   visible=(año == años_unicos[0])),
        )

        fig.add_trace(
            go.Bar(name=f'Hombres {año}', 
                   x=categorias_año, 
                   y=total_hombres_año, 
                   marker=dict(color='rgba(3,187,133,0.3)',
                               line=dict(color='rgb(0,0,0)', width=1)), 
                   text=total_hombres_año,
                   hovertemplate='Hombres: %{y}%<extra></extra>',  
                   textposition='auto', 
                   textangle=0,
                   visible=(año == años_unicos[0])),
        )

   

    fig.update_layout(
        # title='Evolución de FONDEF por Categorías (2020-2023)',
        template='none',
        yaxis=dict(title='Porcentaje'),
        barmode='stack',   
        bargap=0.2,
        font_family='Roboto',
        font=dict(size=14, color='#4d4d4d', family='Roboto'),
        yaxis2=dict(showticklabels=False),
        xaxis=dict(type='category'),
        xaxis_tickangle=-90,
        autosize=True,
        margin=dict(l=100, r=100, t=50, b=200, autoexpand=True),
        legend=dict(font=dict(size=12)),
        hovermode='x',
    )


    # agregar un dropdown para seleccionar el año
    botones = []
    for i, año in enumerate(años_unicos):
        visibilidad = [False] * len(fig.data)
        visibilidad[2*i] = True
        visibilidad[2*i + 1] = True
        botones.append(
            dict(
                label=str(año),
                method="update",
                args=[{"visible": visibilidad},
                      {"title": f"Datos del año {año}"}],
            )
        )

    # agregar un dropdwon para seleccionar el año
    fig.update_layout(
        updatemenus=[
            dict(
                buttons=botones,
                direction="right",
                showactive=True,
                pad={"r": 10, "t": 10},
                x=0,
                xanchor="left",
                y=1.38,
                yanchor="top",
            ),
        ],
    )

    # Crear gráfico de barras para FONDEF_financiamiento
    fig2 = go.Figure()
    # años_unicos_ff = sorted(set(años_ff))
    años_unicos_ff = sorted(set(años_ff))

    for año in años_unicos_ff:
        
        total_mujeres_año_ff = [financiamiento_mujeres[i] for i in range(len(años_ff)) if años_ff[i] == año]
        total_hombres_año_ff = [financiamiento_hombres[i] for i in range(len(años_ff)) if años_ff[i] == año]

        fig2.add_trace(
            go.Bar(name=f'Financiamiento Mujeres {año}', 
                   x=['Mujeres'], 
                   y=total_mujeres_año_ff, 
                   marker=dict(color='rgba(255,174,255,0.5)', 
                               line=dict(color='rgb(0,0,0)', width=1)),
                   text=total_mujeres_año_ff,
                   hovertemplate='Financiamiento Mujeres: $%{y} M<extra></extra>',
                   textposition='auto', 
                   textangle=0,
                   visible=(año == años_unicos_ff[0])),
        )

        fig2.add_trace(
            go.Bar(name=f'Financiamiento Hombres {año}', 
                   x=['Hombres'],
                   y=total_hombres_año_ff, 
                   marker=dict(color='rgba(3,187,133,0.3)',
                               line=dict(color='rgb(0,0,0)', width=1)), 
                   text=total_hombres_año_ff,
                   hovertemplate='Financiamiento Hombres: $ %{y} M<extra></extra>',  
                   textposition='auto', 
                   textangle=0,
                   visible=(año == años_unicos_ff[0])),
        )

    fig2.update_layout(
        template='none',
        yaxis=dict(title='Total Financiamiento ($ M)'),
        barmode='group',   
        bargap=0.2,
        font_family='Roboto',
        font=dict(size=14, color='#4d4d4d', family='Roboto'),
        yaxis2=dict(showticklabels=False),
        # xaxis=dict(type='category'),
        autosize=True,
        margin=dict(l=100, r=100, t=80, b=100, autoexpand=True),
        legend=dict(font=dict(size=12)),
        hovermode='x',
    )

    # Agregar un dropdown para seleccionar el año en FONDEF_financiamiento
    botones_ff = []
    for i, año in enumerate(años_unicos_ff):
        visibilidad = [False] * len(fig2.data)
        visibilidad[2*i] = True
        visibilidad[2*i + 1] = True
        botones_ff.append(
            dict(
                label=str(años_ff[i]),
                method="update",
                args=[
                      {"visible": visibilidad},
                      {"title": f"Financiamiento ($ M) del año {año}"}
                      ],
            )
        )

    fig2.update_layout(
        updatemenus=[
            dict(
                buttons=botones_ff,
                direction="right",
                showactive=True,
                pad={"r": 10, "t": 10},
                x=0,
                xanchor="left",
                y=1.38,
                yanchor="top",
            ),
        ],
    )

    config = {
        'modeBarButtonsToAdd': ['drawline',
                                'drawopenpath',
                                'drawcircle',
                                'drawrect',
                                'eraseshape'],
        'modeBarButtonsToRemove': ['zoom', 'pan', 'select', 'autoScale', 'lasso']
    }

    fig.update_yaxes(tickformat=".1f%")
    fig2.update_yaxes(tickformat=".1f%")

    html = fig.to_html(full_html=False, config=config)
    html2 = fig2.to_html(full_html=False, config=config)

    context = {
        'chart': html,
        'chart_id': 'chart',
        'chart2': html2,
        'chart2_id': 'chart2'
    }

    return render(request, 'lineas_accion_3.html', context)

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
