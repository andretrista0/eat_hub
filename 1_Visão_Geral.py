# Bibliotecas
import pandas as pd
import plotly.express as px
import folium
from folium.plugins import MarkerCluster
import streamlit as st
from PIL import Image
import numpy as np
from streamlit_folium import st_folium

st.set_page_config(page_title="EATHUB - Visão Geral", layout="wide")

#Importante DataFrame
df = pd.read_csv('zomato.csv')
df1 = df.copy()

# ==================================================
# FUNÇÕES
# ==================================================

# Função para obter o nome da cidade pelo código
def country_name(country_id):
    COUNTRIES = {
        1: "India",
        14: "Australia",
        30: "Brazil",
        37: "Canada",
        94: "Indonesia",
        148: "New Zealand",
        162: "Philippines",
        166: "Qatar",
        184: "Singapore",
        189: "South Africa",
        191: "Sri Lanka",
        208: "Turkey",
        214: "United Arab Emirates",
        215: "England",
        216: "United States of America",
    }
    return COUNTRIES.get(country_id)

# Função para traduzir código de cor em nome de cor
COLORS = {
"3F7E00": "darkgreen",
"5BA829": "green",
"9ACD32": "lightgreen",
"CDD614": "orange",
"FFBA00": "red",
"CBCBC8": "darkred",
"FF7800": "darkred",
}
def color_name(color_code):
  return COLORS[color_code]

# ==================================================
# TRATANDO DATAFRAME
# ==================================================

#Tratando Dataframe
df1=df1.dropna(subset=['Cuisines'])
df1=df1.drop_duplicates()

#Deixando apenas 1 tipo de culinaria por restaurente
df1["Cuisines"] = df1.loc[:, "Cuisines"].astype(str).apply(lambda x: x.split(",")[0])

#Criando coluna country
df1['Country'] = df1['Country Code'].map(country_name)

#Criando coluna com os nomes das cores
df1['Rating color name'] = df1['Rating color'].apply(color_name)

df1 = df1.reset_index()

# Supondo que df1['Country'].unique() retorna o array que você mencionou
array_paises = df1['Country'].unique()
# Transformando o array em lista
lista_paises = list(array_paises)

# ==================================================
# MENU LATERAL
# ==================================================
logo = Image.open('logo_eathub2.png')
st.sidebar.image(logo, width=250)
st.sidebar.markdown("""---""")
st.sidebar.markdown('### Filtros')

filtro_paises = st.sidebar.multiselect('Escolha os países em que deseja visualizar os restaurantes', lista_paises, default=lista_paises)
df1 = df1.loc[df1['Country'].isin(filtro_paises),:]

# ==================================================
# Página Principal
# ==================================================

st.header('Visão Geral')
st.markdown("""---""")

st.markdown('#### Dados Gerais')
with st.container():
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        rest_cadastrados = df1['Restaurant ID'].nunique()
        formatted_rest_cadastrados = "{:,.0f}".format(rest_cadastrados)
        col1.metric('Restaurantes', formatted_rest_cadastrados) 
    with col2:
        paises_cadastrados = df1['Country Code'].nunique()
        col2.metric('Países', paises_cadastrados)
    with col3:
        cidades_cadastradas = df1['City'].nunique()
        col3.metric('Cidades', cidades_cadastradas)
    with col4:
        avaliacoes_cadastradas = df1['Votes'].sum()
        formatted_rest_cadastrados = "{:,.0f}".format(avaliacoes_cadastradas)
        col4.metric('Avaliações', formatted_rest_cadastrados)        
    with col5:
        culinarias_cadastradas = df1['Cuisines'].nunique()
        col5.metric('Culinárias', culinarias_cadastradas)

with st.container():
    df1_cidade_localizacao_restaurantes = df1.loc[:,['Restaurant Name', 'Latitude', 'Longitude', 'Average Cost for two', 'Cuisines', 'Aggregate rating']].groupby(['Restaurant Name', 'Cuisines']).median().reset_index()

    # Cria o painel no qual o mapa será adicionado
    fig = folium.Figure(width=1920, height=1080)

    # Cria o objeto map e adiciona ao painel
    mapa = folium.Map(max_bounds=True).add_to(fig)

    # Função para agrupar os marcadores
    marker_cluster = MarkerCluster().add_to(mapa)

    df1_cidade_localizacao_restaurantes = df1_cidade_localizacao_restaurantes

    for i , localizacao in df1_cidade_localizacao_restaurantes.iterrows():
      folium.Marker([localizacao['Latitude'], localizacao['Longitude']], icon=folium.Icon(icon='pushpin'), popup=localizacao[['Average Cost for two', 'Cuisines', 'Aggregate rating']]).add_to(marker_cluster)

    st_folium(mapa, width=1024, height=600)
