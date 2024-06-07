from django.shortcuts import render
from core.models import AcademicosDAP, PIDitt, LiderazgoFemenino, LiderazgoPublicaciones, ProyectosITT, FONDEF_categorias, FONDEF_financiamiento
import plotly.graph_objs as go
from plotly.subplots import make_subplots
from django.http import HttpResponse
import numpy as np

def home(request):
    return render(request, 'home.html')
    
def repositorio(request):
    return render(request, 'repositorio.html')

def lineas_accion(request):
    return render(request, 'lineas_accion.html')

def lineas_accion_2(request):
    return render(request, 'lineas_accion_2.html')

def la4(request):
    return render(request, 'lineas_accion_4.html')

def la1(request):
    return render(request, 'lineas_accion_1.html')

def plot2(request):

    def add_percentage_symbol(values):
        return [f'{value:.0f}%' for value in values]
    
    lp= LiderazgoPublicaciones.objects.all()

    años = list(lp.values_list('año', flat=True))
    total_mujeres = list(lp.values_list('total_mujeres', flat=True))
    total_hombres = list(lp.values_list('total_hombres', flat=True))
    total_publicaciones = list(lp.values_list('total_publicaciones', flat=True))

    lf = LiderazgoFemenino.objects.all()

    # Filtrar lf los datos para el año 2022
    lf_2022 = lf.filter(año=2022)
    categorias_2022 = list(lf_2022.values_list('categoria', flat=True))
    total_mujeres_2022 = list(lf_2022.values_list('total_mujeres', flat=True))
    total_hombres_2022 = list(lf_2022.values_list('total_hombres', flat=True))

    # Filtrar lf los datos para el año 2023
    lf_2023 = lf.filter(año=2023)
    categorias_2023 = list(lf_2023.values_list('categoria', flat=True))
    total_mujeres_2023 = list(lf_2023.values_list('total_mujeres', flat=True))
    total_hombres_2023 = list(lf_2023.values_list('total_hombres', flat=True))

    # Filtrar los datos de ProyectosITT
    pitt = ProyectosITT.objects.all()
    años_itt = list(pitt.values_list('año', flat=True))
    total_itt_mujeres = list(pitt.values_list('total_mujeres', flat=True))
    total_itt_hombres = list(pitt.values_list('total_hombres', flat=True))

    # Agregar el símbolo '%' a los valores
    total_mujeres_2022_with_percent = add_percentage_symbol(total_mujeres_2022)
    total_hombres_2022_with_percent = add_percentage_symbol(total_hombres_2022)
    total_mujeres_2023_with_percent = add_percentage_symbol(total_mujeres_2023)
    total_hombres_2023_with_percent = add_percentage_symbol(total_hombres_2023)
    total_mujeres_with_percent = add_percentage_symbol(total_mujeres)
    total_hombres_with_percent = add_percentage_symbol(total_hombres)
    total_itt_mujeres_with_percent = add_percentage_symbol(total_itt_mujeres)
    total_itt_hombres_with_percent = add_percentage_symbol(total_itt_hombres)


    fig = go.Figure()
    # Crear gráfico de barras para el año 2022
    fig.add_trace(
        go.Bar(name='Mujeres 2022', 
            #    marker_color='purple',
               marker = dict(color = 'rgba(255,174,255,0.5)', 
                              line = dict(color='rgb(0,0,0)',width=1),
                            ), 
               x=categorias_2022, 
               y=total_mujeres_2022, 
               text=total_mujeres_2022_with_percent,
               hovertemplate='Mujeres: %{y}%<extra></extra>',
               textposition='auto', 
               textangle=0),
    )

    fig.add_trace(
        go.Bar(name='Hombres 2022', 
            #    marker_color='green',
               marker = dict(color = 'rgba(3,187,133,0.3)',
                              line = dict(color='rgb(0,0,0)',width=1)), 
               x=categorias_2022, 
               y=total_hombres_2022, 
               text=total_hombres_2022_with_percent,
               hovertemplate='Hombres: %{y}%<extra></extra>',  
               textposition='auto', 
               textangle=0),
    )   

    # Crear gráfico de barras para el año 2023
    fig.add_trace(
        go.Bar(name='Mujeres 2023', 
               x=categorias_2023, 
               y=total_mujeres_2023, 
            #    marker_color='cornflowerblue',
               marker = dict(color = 'rgba(100,149,237,0.3)',
                              line = dict(color='rgb(0,0,0)',width=1)), 
               text=total_mujeres_2023_with_percent,
               hovertemplate='Mujeres: %{y}%<extra></extra>', 
               textposition='auto', 
               textangle=0,
               visible=False),
    )

    fig.add_trace(
        go.Bar(name='Hombres 2023', 
               x=categorias_2023, 
               y=total_hombres_2023, 
            #    marker_color='darkturquoise',
               marker = dict(color = 'rgba(0,206,209,0.3)',
                              line = dict(color='rgb(0,0,0)',width=1)),  
               text=total_hombres_2023_with_percent,
               hovertemplate='Hombres: %{y}%<extra></extra>', 
               textposition='auto', 
               textangle=0,
               visible=False),
    )

    fig.update_layout(
        # title='Evolucion en el área de investigación de publicaciones (2022-2023)',
        title_font_size=12,
        template='none',
        yaxis=dict(title='Porcentaje'),
        barmode='stack',   
        bargap=0.2,
        font_family='Roboto',
        #font size de los valores en las barras
        font=dict(size=14, color='#4d4d4d', family='Roboto'),
        yaxis2=dict(showticklabels=False),
        # xaxis=dict(domain=[0, 0.45]),
        # xaxis2=dict(domain=[0.55, 1]),
        xaxis=dict(type='category'),
        xaxis2=dict(type='category'),
        xaxis_tickangle=-90,
        xaxis2_tickangle=-90,
        autosize=True,
        margin=dict(l=100, r=100, t=50, b=200, autoexpand=True),
        legend=dict(font=dict(size=12)),
        hovermode='x',
    )

    fig.update_traces(textfont=dict(size=12, color='#000', family='Roboto'))

    #agregar un dropdwon para seleccionar el año
    fig.update_layout(
        updatemenus=[
            dict(
                buttons=list([
                    dict(label="2022",
                         method="update",
                         args=[{"visible": [True, True, False, False]},
                               ]),
                    dict(label="2023",
                         method="update",
                         args=[{"visible": [False, False, True, True]},
                               ]),
                ]),
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
        'modeBarButtonsToRemove': ['zoom', 'pan', 'select', 'autoScale', 'lasso'],
        'responsive': 'true'
    }
    

    fig.update_yaxes(tickformat=".1f%")

    fig2 = go.Figure()


    fig2.add_trace(go.Bar(x=años, 
                          y=total_hombres, 
                          name='Hombres', 
                        #   marker_color='green', 
                          text=total_hombres_with_percent, 
                          textposition='auto', 
                          textangle=0,
                          marker = dict(color = 'rgba(3,187,133,0.3)',
                              line = dict(color='rgb(0,0,0)',width=1)),

                          hovertemplate='Hombres: %{y}%<extra></extra>',
                
                          ))
    
    fig2.add_trace(go.Bar(x=años, 
                          y=total_mujeres, 
                          name='Mujeres', 
                        #   marker_color= 'rgba(255, 174, 155, 0.5)', 
                          text=total_mujeres_with_percent, 
                          textposition='auto', 
                          textangle=0,
                          marker = dict(color = 'rgba(255,174,255,0.5)', 
                              line = dict(color='rgb(0,0,0)',width=1),
                            ),
                          hovertemplate='Mujeres: %{y}%<extra></extra>',
                          textfont=dict(size=12, color='#000', family='Roboto')   
                          )
                          )

    fig2.update_layout(
        # title='Evolución de Liderazgo en Publicaciones Científicas (2020-2023)',
        template='none', 
        yaxis=dict(title='Porcentaje'),
        xaxis=dict(title='Años', type='category'),
        barmode='stack',
        bargap=0.6,
        paper_bgcolor='#ffffff',
        font_family='Roboto',
        font_size=12, 
        font_color='#808080',
        autosize=True,
        hovermode='x',
    )

    fig3 = go.Figure()

    fig3.add_trace(go.Scatter(x=años_itt, 
                              y=total_itt_mujeres, 
                              name='Mujeres', 
                              mode='lines+markers+text', 
                              textposition='bottom right', 
                              text=total_itt_mujeres_with_percent,
                              hovertemplate='Mujeres: %{y}%<extra></extra>',
                              textfont=dict(size=12, color='#000', family='Roboto'),   
                              marker=dict(color='rgba(255,174,255,0.5)', size=6)))
    
    fig3.add_trace(go.Scatter(x=años_itt, 
                              y=total_itt_hombres, 
                              name='Hombres', 
                              mode='lines+markers+text', 
                              textposition='top center', 
                              text=total_itt_hombres_with_percent,
                              hovertemplate='Hombres: %{y}%<extra></extra>',
                              textfont=dict(size=12, color='#000', family='Roboto'),   
                              marker=dict(color='rgba(3,187,133,0.3)', size=6)))
   
    fig3.update_layout(
        template='none',
        # title='Evolución Proyectos de Innovación y Transferencia Tecnológica (2020-2023)', 
        yaxis=dict(title='Porcentaje'),
        xaxis=dict(title='Años', type='category'),
        paper_bgcolor='#ffffff',
        font_family='Roboto',
        font_size=12, 
        font_color='#4d4d4d',
        autosize=True,
        hovermode='x',
    )

    fig3.update_traces(line=dict(width=1))

    html = fig.to_html(full_html=False, config=config)
    html2 = fig2.to_html(full_html=False, config=config)
    html3 = fig3.to_html(full_html=False, config=config)

    context = {
        'chart': html,
        'chart_id': 'chart',
        'chart2': html2,
        'chart2_id': 'chart2',
        'chart3': html3,
        'chart3_id': 'chart3'
    }

    return render(request, 'lineas_accion_2.html', context)


def plot3(request):
    # Usar datos de FONDEF_categorias
    fc = FONDEF_categorias.objects.all()

    # Usar datos de FONDEF_financiamiento
    ff = FONDEF_financiamiento.objects.all()

    # Filtrar los datos de FONDEF_financiamiento
    años_ff = list(ff.values_list('año', flat=True))
    total_ff = list(ff.values_list('financiamiento', flat=True))
    sexo_ff = list(ff.values_list('sexo', flat=True))

    # Filtrar los datos de FONDEF_categorias
    años = list(fc.values_list('año', flat=True))
    categorias = list(fc.values_list('categoria', flat=True))
    total_mujeres = list(fc.values_list('total_mujeres', flat=True))
    total_hombres = list(fc.values_list('total_hombres', flat=True))

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
        yaxis=dict(title='Total'),
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
        categorias_año_ff = ['financiamiento']
        total_mujeres_año_ff = [total_ff[i] for i in range(len(años_ff)) if años_ff[i] == año and sexo_ff[i] == 'Mujer']
        total_hombres_año_ff = [total_ff[i] for i in range(len(años_ff)) if años_ff[i] == año and sexo_ff[i] == 'Hombre']

        if total_mujeres_año_ff:  # Verificar si hay datos para mujeres
            fig2.add_trace(
                go.Bar(name=f'Financiamiento Mujeres {año}', 
                       x=categorias_año_ff, 
                       y=total_mujeres_año_ff, 
                       marker=dict(color='rgba(255,174,255,0.5)', 
                                   line=dict(color='rgb(0,0,0)', width=1)),
                       text=total_mujeres_año_ff,
                       hovertemplate=f'Financiamiento Mujeres {año}: {{%y}}<extra></extra>',
                       textposition='auto', 
                       textangle=0,
                       visible=(año == años_unicos_ff[0])),
            )

        if total_hombres_año_ff:  # Verificar si hay datos para hombres
            fig2.add_trace(
                go.Bar(name=f'Financiamiento Hombres {año}', 
                       x=categorias_año_ff, 
                       y=total_hombres_año_ff, 
                       marker=dict(color='rgba(3,187,133,0.3)',
                                   line=dict(color='rgb(0,0,0)', width=1)), 
                       text=total_hombres_año_ff,
                       hovertemplate=f'Financiamiento Hombres {año}: {{%y}}<extra></extra>',  
                       textposition='auto', 
                       textangle=0,
                       visible=(año == años_unicos_ff[0])),
            )

    fig2.update_layout(
        template='none',
        yaxis=dict(title='Total Financiamiento'),
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

    # Agregar un dropdown para seleccionar el año en FONDEF_financiamiento
    botones_ff = []
    for i, año in enumerate(años_unicos_ff):
        # visibilidad = [False] * len(fig2.data)
        # visibilidad[2*i] = True
        # visibilidad[2*i + 1] = True
        botones_ff.append(
            dict(
                label=str(año),
                method="update",
                args=[
                      {"title": f"Financiamiento del año {año}"},
                      {"visible": [True, True, False, False] if i == 0 else [False, False, True, True]}
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




