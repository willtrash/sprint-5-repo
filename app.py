import pandas as pd
import plotly.express as px
import streamlit as st

st.header('Análise de dados de veículos')

car_data = pd.read_csv(
    'vehicles.csv')
build_histogram = st.checkbox('Criar um histograma')
build_scatterplot = st.checkbox('Criar um gráfico de dispersão')

if build_histogram:
    # escrever uma mensagem
    st.write(
        'Criando um histograma para o conjunto de dados de anúncios de vendas de carros')

    # criar um histograma
    fig = px.histogram(car_data, x="odometer")

    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)

if build_scatterplot:
    # escrever uma mensagem
    st.write(
        'Criando um gráfico de dispersão para o conjunto de dados de anúncios de vendas de carros')

    # criar um gráfico de dispersão
    fig = px.scatter(car_data, x="model_year", y="price")

    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)
