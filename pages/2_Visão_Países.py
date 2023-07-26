# Bibliotecas
import pandas as pd
import plotly.express as px
import folium
from folium.plugins import MarkerCluster
import streamlit as st
from PIL import Image
import numpy as np
from streamlit_folium import st_folium

st.set_page_config(page_title="EATHUB - Visão Países", layout="wide")

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
st.sidebar.image(logo, width=300)
st.sidebar.markdown("""---""")
st.sidebar.markdown('### Filtros')

filtro_paises = st.sidebar.multiselect('Escolha os países em que deseja visualizar os restaurantes', lista_paises, default=lista_paises)
df1 = df1.loc[df1['Country'].isin(filtro_paises),:]

# ==================================================
# Página Principal
# ==================================================

st.header('Visão Países')
st.markdown("""---""")

with st.container():
    st.markdown('#### Quantidade de Restaurantes Registrados por País')
    # - Quantidade de restaurantes registrados por país
    df1_qtd_rest_pais = df1.loc[:,['Country', 'Restaurant ID']].groupby('Country').nunique().sort_values(by=['Restaurant ID'], ascending=False).reset_index()
    fig = px.bar(df1_qtd_rest_pais, x='Country', y='Restaurant ID', labels={'Country':'País', 'Restaurant ID':'Quantidade de Restaurantes'})
    st.plotly_chart(fig, use_container_width=True)

with st.container():
    st.markdown('#### Quantidade de Cidades Registradas por País')
    # - Quantidade de cidades registrados por país
    df1_qtd_cidade_pais = df1.loc[:,['Country', 'City']].groupby('Country').nunique().sort_values(by=['City'], ascending=False).reset_index()
    fig = px.bar(df1_qtd_cidade_pais, x='Country', y='City', labels={'Country':'País', 'City':'Quantidade de Cidades'})
    st.plotly_chart(fig, use_container_width=True)
    
    
    
with st.container():
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('#### Média de Avaliação feitas por País')
        # - Média de avaliações feitas por país
        df1_media_avaliacao_pais = df1.loc[:,['Country', 'Votes']].groupby('Country').mean().sort_values(by=['Votes'], ascending=False).reset_index()
        fig = px.bar(df1_media_avaliacao_pais, x='Country', y='Votes', labels={'Country':'País', 'Votes':'Quantidade de Média de Avaliações'})
        st.plotly_chart(fig, use_container_width=True)
        
        
    with col2:
        st.markdown('#### Média de Preço de um Prato Para Dois')
        # - Preço de um prato para duas pessoas
        df1_media_custo2_pais = df1.loc[:,['Country', 'Average Cost for two']].groupby('Country').mean().round(2).sort_values(by=['Average Cost for two'], ascending=False).reset_index()
        fig= px.bar(df1_media_custo2_pais, x='Country', y='Average Cost for two', labels={'Country':'País', 'Average Cost for two':'Preço Médio de um Prato Para Dois'})
        st.plotly_chart(fig, use_container_width=True)