import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine
import streamlit as st

# Conexão com o banco de dados
db_user = 'postgres'
db_password = '1234'  # Certifique-se de que a senha esteja correta e entre aspas
db_host = 'localhost'
db_port = '5432'
db_name = 'tempo'

engine = create_engine(f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}')

# Função para carregar dados de uma view
def load_data(view_name):
    return pd.read_sql(f"SELECT * FROM {view_name}", engine)

# Título do dashboard
st.title('Dashboard de Temperaturas IoT')

# Gráfico 1: Média de temperatura por dispositivo
st.header('Média de Temperatura por Dispositivo')
df_avg_temp = load_data('media_temp_sala')  # Nome da view ajustado
fig1 = px.bar(df_avg_temp, x='room_id/id', y='media_temp')
st.plotly_chart(fig1)

# Gráfico 2: Contagem de leituras por hora (exemplo)
st.header('Leituras por Hora do Dia')
df_leituras_hora = load_data('leituras_por_hora')  # Certifique-se de que esta view exista
fig2 = px.line(df_leituras_hora, x='hora', y='contagem')
st.plotly_chart(fig2)

# Gráfico 3: Temperaturas máximas e mínimas por dia (exemplo)
st.header('Temperaturas Máximas e Mínimas por Dia')
df_temp_max_min = load_data('temp_max_min_por_dia')  # Certifique-se de que esta view exista
fig3 = px.line(df_temp_max_min, x='data', y=['temp_max', 'temp_min'])
st.plotly_chart(fig3)
