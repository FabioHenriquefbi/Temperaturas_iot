import pandas as pd
from sqlalchemy import create_engine

# Caminho do arquivo CSV
file_path = 'C:\\Users\\Fabio\\OneDrive\\Área de Trabalho\\Unifecaf\\Disruptive Architectures IOT, Big Data e IA\\Fabio_RA_42799_Porfólio\\IOT-temp.csv'

# Ler o arquivo CSV
df = pd.read_csv(file_path)

# Verificar se o DataFrame está preenchido
if df.empty:
    print("O DataFrame está vazio. Verifique o arquivo CSV.")
else:
    print("O DataFrame contém dados.")
    print(df.head())

# Mostrar as colunas do DataFrame
print(df.columns)

# Remover a coluna 'id' do DataFrame
df = df.drop(columns=['id'])

# Converte o campo 'noted_date' para o formato datetime do pandas
df['noted_date'] = pd.to_datetime(df['noted_date'], format='%d-%m-%Y %H:%M')

# Configurações do PostgreSQL
db_user = 'postgres'
db_password = '1234'  # Sua senha definida anteriormente
db_host = 'localhost'
db_port = '5432'
db_name = 'tempo'

# Criar uma engine de conexão
engine = create_engine(f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}')

# Processar os dados, se necessário
df['nova_coluna'] = df['temp'].apply(lambda x: x * 2)  # Exemplo de processamento

# Verificar se há dados a serem inseridos
if not df.empty:
    # Inserir dados no banco de dados
    with engine.connect() as connection:
        df.to_sql('tabela_tempo', con=connection, if_exists='append', index=False)
    print("Dados inseridos com sucesso!")
else:
    print("Nenhum dado foi inserido porque o DataFrame está vazio.")
