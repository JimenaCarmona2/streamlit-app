import pandas as pd
import plotly.express as px

data = pd.read_parquet("app/data/df_ml_final.parquet")
data_churn = data[data["Churn"] == 1].reset_index(drop=True)

def cargar_data():
    return data, data_churn

# pageChurn

def kpi_abandono_por_edad():
    tabla = data_churn.groupby(['Cat_age', 'Churn']).size().reset_index(name='Usuarios')
    colores = ["#6586f0"]

    fig = px.bar(
        tabla,
        x="Cat_age",
        y="Usuarios",
        color_discrete_sequence=colores,
        labels={"Usuarios": "Número de Usuarios"},
        title="Churn por Grupo de Edad"
    )

    fig.update_layout(
        xaxis_title = None,
        yaxis_title_font_size=10,
        legend_title_font_size=10,
        height=400,
    )
    
    return fig

def kpi_motivos_de_llamada_top3():
    tabla = data_churn.groupby(['Cat_motive', 'Churn']).size().reset_index(name='Usuarios')

    top3 = tabla.sort_values('Usuarios', ascending=False).head(3)
    colores = ["#6586f0"]

    fig = px.bar(
        top3,
        x="Cat_motive",
        y="Usuarios",
        color_discrete_sequence=colores,
        labels={"Usuarios": "Número de Usuarios"},
        title="Motivos de Llamada Previos al Churn",
    )
    fig.update_layout(
        xaxis_title = None,
        yaxis_title_font_size=10,
        legend_title_font_size=10,
        height=400
    )
    
    return fig

def kpi_churn_por_nivel_de_cuenta():
    bins = [0, 1000, 3000, float('inf')]
    labels = ['0 - 1000', '1000 - 3000', '3000+']
    data_churn['Rangos_Trnx'] = pd.cut(data_churn['Trnx'], bins=bins, labels=labels)

    datos = data_churn.groupby(['Rangos_Trnx'])['Id_user'].nunique().reset_index(name='Usuarios')

    resultado = {
        row['Rangos_Trnx']: int(row['Usuarios'])
        for _, row in datos.iterrows()
    }
    return resultado

def kpi_distribucion_horario():

    tabla = data_churn['Cat_turn'].value_counts()
    colors = ["#c6dbef", "#6baed6", "#2171b5"]
    
    fig = px.pie(
        names=tabla.index,
        values=tabla.values,
        color_discrete_sequence=colors,
        title="Churn de Usuarios por Turno",
    )
    fig.update_traces(textinfo='percent+label')
    fig.update_layout(showlegend=False, height=400)

    return fig

def kpi_atencion_telefonica():
    tabla = data_churn.groupby(['Por_que_canal_nos_esta_contactando', 'Churn']).size().reset_index(name='Usuarios')
    colores = ["#6586f0", "#65DDF0", "#9E65F0"]

    fig = px.pie(
        tabla,
        names="Por_que_canal_nos_esta_contactando",
        values="Usuarios",
        color_discrete_sequence=colores,
        title="Churn por Canal de Atención",
        hole=0.5,
    )
    fig.update_layout(
        title_font_size=16,
        legend_title="Canal",
        legend_title_font_size=10,
        legend_font_size=10,
        height=400
    )
    return fig

# pageInfo

# Gráficas
def churn_en_el_tiempo():
    data_temp = data.dropna(subset=['Fecha']).copy()
    data_temp['Fecha_Mes'] = data_temp['Fecha'].dt.to_period('M')

    tabla = data_temp.groupby('Fecha_Mes')['Churn'].mean().reset_index()
    tabla['Churn_Rate'] = tabla['Churn'] * 100

    tabla = tabla.sort_values('Fecha_Mes')

    tabla['Fecha_Mes_dt'] = tabla['Fecha_Mes'].dt.to_timestamp()
    fig = px.line(
        tabla,
        x='Fecha_Mes_dt',
        y='Churn_Rate',
        markers=True,
        labels={'Fecha_Mes_str': 'Mes', 'Churn_Rate': 'Tasa de Churn (%)'},
        title='Churn en el Tiempo',
    )
    fig.update_layout(
        xaxis_title=None,
        yaxis_title_font_size=10,
        legend_title_font_size=10,
        height=400
    )
    return fig

def costo_por_cliente():
    pass

def calificacion_call_center(df):
    tabla = df['Respcsat'].value_counts().reset_index()
    tabla.columns = ['Calificación', 'Cantidad']

    tabla = tabla.drop(tabla[tabla['Calificación'] == 0].index)

    colores = ["#6586f0", "#65DDF0", "#9E65F0", "#F065E1", "#F06565"]
    fig = px.bar(
        tabla,
        x='Calificación',
        y='Cantidad',
        #color='Calificación',
        color_discrete_sequence=colores,
        title='Calificación del Call Center',
    )
    fig.update_layout(
        xaxis_title=None,
        yaxis_title_font_size=10,
        legend_title_font_size=10,
        height=400,
        showlegend=False
    )
    return fig

# Métricas
def usuarios_totales(df):
    total_usuarios = df['Id_user'].nunique()
    format_total = f"{total_usuarios:,}".replace(".", ",")
    return format_total
    
def tasa_de_churn(df, df_churn):
    total_usuarios = df['Id_user'].nunique()
    usuarios_churn = df_churn['Id_user'].nunique()
    format_churn = f"{usuarios_churn:,}".replace(".", ",")
    tasa_churn = round((usuarios_churn / total_usuarios) * 100, 2)
    return format_churn + f" ({tasa_churn}%)"

def meta_1():
    df_sat = data.dropna(subset=['Respcsat']).copy()
    kpi_general = (df_sat["Respcsat"] <= 3).mean() * 100
    tasa = round(kpi_general, 2)
    return f"{tasa}%"

def meta_2():
    df_tx = data.dropna(subset=['Trnx', "Id_user"]).copy()
    total_trnx = df_tx["Trnx"].sum()
    usuarios_act = df_tx["Id_user"].nunique()

    if usuarios_act == 0:
        frecuencia = 0
    else:
        frecuencia = round(total_trnx / usuarios_act, 0)
    
    return f"{frecuencia}"


