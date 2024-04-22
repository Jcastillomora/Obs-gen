from django.shortcuts import render
from core.models import AcademicosDAP, PIDitt, LiderazgoFemenino, LiderazgoPublicaciones, ProyectosITT
import plotly.graph_objs as go
from plotly.subplots import make_subplots
from django.http import HttpResponse

# Gráfico de propiedad intelectual por año y género del modelo PIDitt(ditt.csv)
def plot(request):

    # Variables para el gráfico desde el modelo PIDitt
    pi_ditt = PIDitt.objects.all()
    años = list(pi_ditt.values_list('año', flat=True))
    total_mujeres = list(pi_ditt.values_list('total_mujeres', flat=True))
    total_hombres = list(pi_ditt.values_list('total_hombres', flat=True))
    total_pi = list(pi_ditt.values_list('total_pi', flat=True))

    # Creación de gráfico "fig", tiene 2 filas en una columna
    fig = make_subplots(rows=2, cols=1)

    # Gráfico de barras para hombres y mujeres
    fig.add_trace(go.Bar(x=años, y=total_pi, name='Total PI', marker=dict(color='orange')), row=2, col=1)

    # Se agregan las líneas de tendencia para el gráfico de dispersión
    fig.add_trace(go.Scatter(x=años, y=total_hombres, mode='lines', name='Hombres', line=dict(color='blue')))
    fig.add_trace(go.Scatter(x=años, y=total_mujeres, mode='lines', name='Mujeres', line=dict(color='red')))
    fig.add_trace(go.Scatter(x=años, y=total_pi, mode='lines', name='Total PI', line=dict(color='green')))

    # Cambiar el estilo de la figura "fig""
    fig.update_layout(
        template='none',
        title='Propiedad Intelectual por Año y Género',
        # xaxis=dict(title='Año'),
        yaxis=dict(title='Total'),
        legend=dict(x=1.15, y=1),
        paper_bgcolor='#4d4d4d',
        font_family='Roboto',
        font_size=14,
        font_color='black',
        autosize=True,
    )

    # Configurar el eje x de la figura "fig"  
    fig.update_xaxes(title_text='Año', row=2, col=1)

    # Creación de gráfico de barras "fig2"
    fig2 = go.Figure()
    fig2.add_trace(go.Bar(x=años, y=total_hombres, name='Hombres', marker_color='blue'))
    fig2.add_trace(go.Bar(x=años, y=total_mujeres, name='Mujeres', marker_color='red'))

    # Configurar la figura 2
    fig2.update_layout(
        template='plotly_dark',
        title='Grafico de Barras Prueba', 
        yaxis=dict(title='Total PI'),
        xaxis=dict(title='Año'),
        barmode='stack',
        paper_bgcolor='#ffffff',
        font_family='Roboto',
        font_size=14, 
        font_color='black',
        autosize=True,
    )

    # Convertir las figuras a HTML
    html = fig.to_html(full_html=False)
    html2 = fig2.to_html(full_html=False)

    # Contexto para renderizar las figuras en el template
    context = {
        'chart': html,
        'chart2': html2,
        'chart_id': 'chart',
        'chart2_id': 'chart2'
    }

    return render(request, 'base.html', context)
    

def lineas_accion(request):
    return render(request, 'lineas_accion.html')

def lineas_accion_1(request):
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

    fig = make_subplots(rows=1, cols=2, subplot_titles=('2022', '2023'))

    # Crear gráfico de barras para el año 2022
    fig.add_trace(
        go.Bar(name='Mujeres 2022', marker_color='purple', x=categorias_2022, y=total_mujeres_2022, text=total_mujeres_2022_with_percent, textposition='auto', textangle=0),
        row=1, col=1
    )

    fig.add_trace(
        go.Bar(name='Hombres 2022', marker_color='green', x=categorias_2022, y=total_hombres_2022, text=total_hombres_2022_with_percent, textposition='auto', textangle=0),
        row=1, col=1
    )   

    # Crear gráfico de barras para el año 2023
    fig.add_trace(
        go.Bar(name='Mujeres 2023', x=categorias_2023, y=total_mujeres_2023, marker_color='cornflowerblue', text=total_mujeres_2023_with_percent, textposition='auto', textangle=0),
        row=1, col=2
    )

    fig.add_trace(
        go.Bar(name='Hombres 2023', x=categorias_2023, y=total_hombres_2023, marker_color='darkturquoise', text=total_hombres_2023_with_percent, textposition='auto', textangle=0),
        row=1, col=2
    )

    fig.update_layout(
        # title='Evolucion en el área de investigación de publicaciones (2022-2023)',
        title_font_size=14,
        template='none',
        yaxis=dict(title='Porcentaje'),   
        barmode='relative',
        font_family='Roboto',
        font_size=12,
        font_color='#4d4d4d',
        yaxis2=dict(showticklabels=False),
        xaxis=dict(domain=[0, 0.45]),
        xaxis2=dict(domain=[0.55, 1]),
        xaxis_tickangle=-90,
        xaxis2_tickangle=-90,
        autosize=True,
        margin=dict(l=50, r=50, t=80, b=180, autoexpand=True),
        legend=dict(font=dict(size=9)),

    )

    fig.update_traces(textfont=dict(size=10, color='#ffffff', family='Roboto'), textangle=-90)

    fig.update_yaxes(tickformat=".1f%")

    fig2 = go.Figure()
    fig2.add_trace(go.Bar(x=años, y=total_hombres, name='Hombres', marker_color='green', text=total_hombres_with_percent, textposition='auto', textangle=0))
    fig2.add_trace(go.Bar(x=años, y=total_mujeres, name='Mujeres', marker_color='purple', text=total_mujeres_with_percent, textposition='auto', textangle=0))

    fig2.update_layout(
        title='Evolución de Liderazgo en Publicaciones Científicas (2020-2023)',
        template='none', 
        yaxis=dict(title='Porcentaje'),
        xaxis=dict(title='Años', type='category'),
        barmode='stack',
        paper_bgcolor='#ffffff',
        font_family='Roboto',
        font_size=12, 
        font_color='#808080',
        autosize=True,
    )

    fig3 = go.Figure()

    fig3.add_trace(go.Scatter(x=años_itt, y=total_itt_mujeres, name='Mujeres', mode='lines+markers+text', textposition='bottom right', text=total_itt_mujeres_with_percent, marker=dict(color='purple', size=6)))
    fig3.add_trace(go.Scatter(x=años_itt, y=total_itt_hombres, name='Hombres', mode='lines+markers+text', textposition='top center', text=total_itt_hombres_with_percent, marker=dict(color='green', size=6)))
   
    fig3.update_layout(
        template='none',
        title='Evolución Proyectos de Innovación y Transferencia Tecnológica (2020-2023)', 
        yaxis=dict(title='Porcentaje'),
        xaxis=dict(title='Años', type='category'),
        paper_bgcolor='#ffffff',
        font_family='Roboto',
        font_size=12, 
        font_color='#808080',
        autosize=True,
        hoverlabel_bgcolor='#ffffff',
        hoverlabel_bordercolor='#ffffff',
        hoverlabel_font_family='Roboto',
        hovermode='x',
    )

    fig3.update_traces(line=dict(width=1))

    html = fig.to_html(full_html=False)
    html2 = fig2.to_html(full_html=False)
    html3 = fig3.to_html(full_html=False)

    context = {
        'chart': html,
        'chart_id': 'chart',
        'chart2': html2,
        'chart2_id': 'chart2',
        'chart3': html3,
        'chart3_id': 'chart3'
    }

    return render(request, 'lineas_accion_1.html', context)





