import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns

data = pd.read_parquet("app/data/df_ml_final.parquet")

# solo para los kpis con churn 
data_churn = data[data["Churn"] == 1].reset_index(drop=True)

# KPI 1: Abandono por grupo de edad
def kpi_abandono_por_edad():
    tabla = data.groupby(['Cat_age', 'Churn']).size().reset_index(name='Usuarios')
    colores = ["#6586f0", "#3dace7"]

    fig = px.bar(
        tabla,
        x="Cat_age",
        y="Usuarios",
        color="Churn",
        barmode='group',
        color_discrete_sequence=colores,
        labels={"Cat_age": "Grupo de Edad", "Usuarios": "Número de Usuarios", "Churn": "Churn"},
        width=500,
        height=400
    )

    fig.update_layout(
        xaxis_title_font_size=10,
        yaxis_title_font_size=10,
        legend_title="Churn",
        legend_title_font_size=10,
        legend_font_size=10,
        bargap=0.15,
        template='plotly_white'
    )
    
    return fig

def kpi_motivos_de_llamada_previo_al_churn():
    tabla = data.groupby(['Cat_motive', 'Churn']).size().reset_index(name='Usuarios')
    colores = ["#6586f0", "#3dace7"]

    fig = px.bar(
        tabla,
        x="Cat_motive",
        y="Usuarios",
        color="Churn",
        barmode='group',
        color_discrete_sequence=colores,
        labels={"Cat_motive": "Motivo de Llamada", "Usuarios": "Número de Usuarios", "Churn": "Churn"},
        width=500,
        height=400
    )
    fig.update_layout(
        xaxis_title_font_size=10,
        yaxis_title_font_size=10,
        legend_title="Churn",
        legend_title_font_size=10,
        legend_font_size=10,
        bargap=0.15,
        template='plotly_white'
    )
    
    return fig

def kpi_churn_por_nivel_de_cuenta():
    bins = [0, 1000, 3000, float('inf')]
    labels = ['0 - 1000', '1000 - 3000', '3000+']
    data_churn['Rangos_Trnx'] = pd.cut(data_churn['Trnx'], bins=bins, labels=labels)

    datos = data_churn.groupby(['Qualification', 'Rangos_Trnx'])['Id_user'].nunique().reset_index(name='Usuarios')
    u_totales = datos.groupby('Qualification', as_index=False)['Usuarios'].sum().rename(columns={'Usuarios': 'Total_Usuarios'})
    
    datos = datos.merge(u_totales)
    datos = datos.sort_values(['Qualification', 'Rangos_Trnx'])
    colores = ["#6586f0", "#3dace7", "#588af7"]

    fig = px.bar(
        datos,
        x='Qualification',
        y='Usuarios',
        color='Rangos_Trnx',
        barmode='group',
        color_discrete_sequence=colores,
        text='Usuarios',
        width=500,
        height=500
    )
    fig.update_traces(textposition='outside')
    fig.update_layout(
        xaxis_title_font_size=10,
        yaxis_title_font_size=10,
        legend_title="Rangos de Transacciones",
        legend_title_font_size=10,
        legend_font_size=10,
        bargap=0.15,
        template='plotly_white'
    )

    return fig

def kpi_distribucion_horario():

    tabla = data['Cat_turn'].value_counts()
    colors = ["#c6dbef", "#6baed6", "#2171b5"]
    
    fig = px.pie(
        names=tabla.index,
        values=tabla.values,
        color_discrete_sequence=colors,
        width=500,
        height=500
    )
    fig.update_traces(textposition='inside', textinfo='percent+label')
    fig.update_layout(
        legend_title="Categoría de Turno",
        legend_title_font_size=10,
        legend_font_size=10,
        template='plotly_white'
    )

    return fig

def kpi_atencion_telefonica():
    tabla = data.groupby(['Por_que_canal_nos_esta_contactando', 'Churn']).size().reset_index(name='Usuarios')
    colores = ["#6586f0", "#3dace7"]

    fig = px.bar(
        tabla,
        x="Por_que_canal_nos_esta_contactando",
        y="Usuarios",
        color="Churn",
        barmode='group',
        color_discrete_sequence=colores,
        labels={"Por_que_canal_nos_esta_contactando": "Canal de Atención Telefónica", "Usuarios": "Número de Usuarios", "Churn": "Churn"},
        width=500,
        height=400
    )
    fig.update_layout(
        xaxis_title_font_size=10,
        yaxis_title_font_size=10,
        legend_title="Churn",
        legend_title_font_size=10,
        legend_font_size=10,
        bargap=0.15,
        template='plotly_white'
    )
    return fig