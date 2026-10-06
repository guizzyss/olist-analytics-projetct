import os
from sqlalchemy import create_engine
from dotenv import load_dotenv

# Carrega as variáveis escondidas no arquivo .env
load_dotenv()

def carregar_para_postgres(dicionario_dfs):
    """
    Recebe os DataFrames limpos e os insere no PostgreSQL.
    """
    print("Iniciando a conexão com o PostgreSQL")

    # Pegando as credenciais do .env
    DB_USER = os.getenv("DB_USER")
    DB_PASS = os.getenv("DB_PASSWORD")
    DB_HOST = os.getenv("DB_HOST", "localhost")
    DB_PORT = os.getenv("DB_PORT", "5433")
    DB_NAME = os.getenv("DB_NAME", "olist_db")

    # String de conexão no padrão SQLAlchemy
    string_conexao = f"postgresql+psycopg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    
    try:
        engine = create_engine(string_conexao)
        
        # Iterando sobre o dicionário e enviando cada tabela para o banco
        for nome_tabela, df in dicionario_dfs.items():
            print(f"Carregando a tabela '{nome_tabela}' no banco de dados...")
            
            # to_sql cria ou substitui a tabela automaticamente
            df.to_sql(name=nome_tabela, con=engine, if_exists='append', index=False, chunksize=10000)
            
        print("Carga de dados concluída com sucesso!")
        
    except ConnectionError as ce: 
        print(f"Erro ao conectar ou carregar dados no PostgreSQL: {ce}")
    
    except Exception as e:
        print(f"Erro desconhecido. Por favor, verifique o código: {e}")

    finally:
        # Fechando a conexão com o banco de dados
        engine.dispose()
        print("Conexão com o PostgreSQL encerrada.")