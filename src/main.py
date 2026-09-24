from extract import extrair_dados_kaggle
from transform import limpar_e_transformar
from load import carregar_para_postgres

def executar_pipeline():
    print("=== INICIANDO PIPELINE ETL OLIST ===")
    
    # 1. Extract
    caminho_arquivos_brutos = extrair_dados_kaggle()
    
    # 2. Transform
    dados_limpos = limpar_e_transformar(caminho_arquivos_brutos)
    
    # 3. Load
    carregar_para_postgres(dados_limpos)
    
    print("=== PIPELINE FINALIZADO COM SUCESSO ===")

if __name__ == "__main__":
    executar_pipeline()