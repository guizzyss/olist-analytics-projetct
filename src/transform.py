import pandas as pd
import os

def limpar_e_transformar(caminho_dados):
    """
    Lê os CSVs baixados, aplica as regras de normalização e retorna 
    um dicionário de DataFrames limpos prontos para o banco de dados.
    """
    print("Iniciando a transformação dos dados com Pandas...")

    # 1. Leitura dos dados brutos
    caminho_pedidos = os.path.join(caminho_dados, "olist_orders_dataset.csv")
    df_pedidos = pd.read_csv(caminho_pedidos)

    # 2. Tratamento: Convertendo colunas de data (object/string) para datetime real
    colunas_data = [
        'order_purchase_timestamp', 
        'order_approved_at', 
        'order_delivered_carrier_date', 
        'order_delivered_customer_date', 
        'order_estimated_delivery_date'
    ]
    for col in colunas_data:
        df_pedidos[col] = pd.to_datetime(df_pedidos[col])

    # 3. Tratamento: Lidando com valores nulos (exemplo)
    # Aqui você pode decidir se remove (dropna) ou preenche (fillna)
    # df_pedidos = df_pedidos.dropna(subset=['order_approved_at'])

    print("Transformação concluída!")
    
    # Retorna um dicionário para facilitar o envio para múltiplas tabelas no SQL
    return {
        "pedidos": df_pedidos
        # Você adicionará df_itens, df_clientes aqui depois
    }