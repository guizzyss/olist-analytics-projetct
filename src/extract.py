import kagglehub

def extrair_dados_kaggle():
    """
    Conecta na API do Kaggle e baixa a última versão do dataset da Olist.
    Retorna o caminho (path) absoluto da pasta onde os CSVs foram salvos.
    """
    print("Iniciando extração de dados da API do Kaggle...")
    
    # O kagglehub baixa os arquivos para o cache do sistema e retorna o caminho
    caminho_dados = kagglehub.dataset_download("olistbr/brazilian-ecommerce")
    
    print(f"Extração concluída! Dados disponíveis em: {caminho_dados}")
    return caminho_dados

# Bloco de teste (só roda se você executar este arquivo isoladamente)
if __name__ == "__main__":
    extrair_dados_kaggle()