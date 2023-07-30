# Bibliotecas
import pandas as pd
import plotly.express as px
import folium
from folium.plugins import MarkerCluster
import streamlit as st
from PIL import Image
import numpy as np
from streamlit_folium import st_folium

st.set_page_config(page_title="EATHUB - Visão Culinária", layout="wide")

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

# Supondo que df1['Cuisines'].unique() retorna o array que você mencionou
array_culinaria = df1['Cuisines'].unique()
# Transformando o array em lista
lista_culinaria = list(array_culinaria)

df2 = df1.copy()
df2 = df2.reset_index()
df3 = df1.copy()
df3 = df3.reset_index()
# ==================================================
# MENU LATERAL
# ==================================================
logo = Image.open('logo_eathub2.png')
st.sidebar.image(logo, width=250)
st.sidebar.markdown("""---""")
st.sidebar.markdown('### Filtros')

# Filtro de País
filtro_paises = st.sidebar.multiselect('Escolha os países em que deseja visualizar os restaurantes', lista_paises, default=lista_paises)
df1 = df1.loc[df1['Country'].isin(filtro_paises),:]
df2 = df2.loc[df2['Country'].isin(filtro_paises),:]

#Filtro de restaurante
filtro_qtd_rest = st.sidebar.slider('Selecione a quantidade de restaurantes', value=10, min_value=1, max_value=20)

filtro_culinaria = st.sidebar.multiselect('Escolha os tipos culinários', lista_culinaria, default=lista_culinaria[:10])
df1 = df1.loc[df1['Cuisines'].isin(filtro_culinaria),:]

# ==================================================
# Página Principal
# ==================================================

st.header('Visão Culinária')
st.markdown("""---""")

with st.container():
    st.header('Top 5 restaurantes com maior nota na plataforma')
    df3_top_melhores_rest = df3.loc[:,['Restaurant ID', 'Restaurant Name', 'Country', 'City', 'Cuisines', 'Average Cost for two','Aggregate rating', 'Votes']].groupby(['Restaurant ID', 'Restaurant Name', 'Country', 'City', 'Cuisines']).mean().round(2).sort_values(by='Aggregate rating', ascending=False).reset_index()
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.metric(label=(f"{df3_top_melhores_rest['Cuisines'][0]}: {df3_top_melhores_rest['Restaurant Name'][0]}"), value=(f"{df3_top_melhores_rest['Aggregate rating'][0]}/5.0"), help=(f"País - Cidade:  {df3_top_melhores_rest['Country'][0]} - {df3_top_melhores_rest['City'][0]}"))
    with col2:
        st.metric(label=(f"{df3_top_melhores_rest['Cuisines'][1]}: {df3_top_melhores_rest['Restaurant Name'][1]}"), value=(f"{df3_top_melhores_rest['Aggregate rating'][1]}/5.0"), help=(f"País - Cidade: {df3_top_melhores_rest['Country'][1]} - {df3_top_melhores_rest['City'][1]}"))
    with col3:
        st.metric(label=(f"{df3_top_melhores_rest['Cuisines'][2]}: {df3_top_melhores_rest['Restaurant Name'][2]}"), value=(f"{df3_top_melhores_rest['Aggregate rating'][2]}/5.0"), help=(f"País - Cidade: {df3_top_melhores_rest['Country'][2]} - {df3_top_melhores_rest['City'][2]}"))
    with col4:
        st.metric(label=(f"{df3_top_melhores_rest['Cuisines'][3]}: {df3_top_melhores_rest['Restaurant Name'][3]}"), value=(f"{df3_top_melhores_rest['Aggregate rating'][3]}/5.0"), help=(f"País - Cidade: {df3_top_melhores_rest['Country'][3]} - {df3_top_melhores_rest['City'][3]}"))
    with col5:
        st.metric(label=(f"{df3_top_melhores_rest['Cuisines'][4]}: {df3_top_melhores_rest['Restaurant Name'][4]}"), value=(f"{df3_top_melhores_rest['Aggregate rating'][4]}/5.0"), help=(f"País - Cidade: {df3_top_melhores_rest['Country'][4]} - {df3_top_melhores_rest['City'][4]}"))        


        
#with st.container():
#   st.header(f'Top {filtro_qtd_rest} Restaurantes')
#    df1_top_melhores_rest = df1.loc[:,['Restaurant ID', 'Restaurant Name', 'Country', 'City', 'Cuisines', 'Average Cost for two','Aggregate rating', 'Votes']].groupby(['Restaurant ID', 'Restaurant Name', 'Country', 'City', 'Cuisines']).mean().round(2).sort_values(by='Aggregate rating', ascending=False).reset_index()
#    st.table(df1_top_melhores_rest.head(filtro_qtd_rest))

with st.container():
    st.header(f'Top {filtro_qtd_rest} restaurantes ')
    df1_top_melhores_rest = df1.loc[:,['Restaurant ID', 'Restaurant Name', 'Country', 'City', 'Cuisines', 'Average Cost for two','Aggregate rating', 'Votes']].groupby(['Restaurant ID', 'Restaurant Name', 'Country', 'City', 'Cuisines']).mean().round(2).sort_values(by='Aggregate rating', ascending=False).reset_index()

    # Renomear as colunas para o português
    df1_top_melhores_rest.rename(columns={
        'Restaurant ID': 'ID do Restaurante',
        'Restaurant Name': 'Nome do Restaurante',
        'Country': 'País',
        'City': 'Cidade',
        'Cuisines': 'Cozinhas',
        'Average Cost for two': 'Custo Médio para Dois',
        'Aggregate rating': 'Avaliação Média',
        'Votes': 'Votos'
    }, inplace=True)

    # Definir o índice iniciando em 1
    df1_top_melhores_rest.index = range(1, len(df1_top_melhores_rest) + 1)

    st.table(df1_top_melhores_rest.head(filtro_qtd_rest))
        
with st.container():
    col1, col2 = st.columns(2)
    with col1:
        st.header(f'Top {filtro_qtd_rest} tipos de culinários com maior nota')
        df1_top_melhores_rest_culinaria = df2.loc[:,['Cuisines', 'Aggregate rating']].groupby(['Cuisines']).mean().round(2).sort_values(by='Aggregate rating', ascending=False).reset_index()
        fig = px.bar(df1_top_melhores_rest_culinaria.head(filtro_qtd_rest), x='Cuisines', y='Aggregate rating', labels={'Cuisines': 'Tipo de Culinária', 'Aggregate rating': 'Avaliação Média'}, text_auto=True)
        st.plotly_chart(fig, use_container_width=True)
        
        
    with col2:
        st.header(f'Top {filtro_qtd_rest} tipos de culinários com menor nota')
        df1_top_piores_rest_culinaria = df2.loc[:,['Cuisines', 'Aggregate rating']].groupby(['Cuisines']).mean().round(2).sort_values(by='Aggregate rating', ascending=True).reset_index()
        fig = px.bar(df1_top_piores_rest_culinaria.head(filtro_qtd_rest), x='Cuisines', y='Aggregate rating', labels={'Cuisines': 'Tipo de Culinária', 'Aggregate rating': 'Avaliação Média'}, text_auto=True)
        st.plotly_chart(fig, use_container_width=True)    
    

    
