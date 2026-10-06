import pandas as pd
import os

def limpar_e_transformar(caminho_dados):
    print ("Iniciando a transformação dos dados brutos")

    #1. Leitura de todas as tabelas CSV base
    df_clientes = pd.read_csv(os.path.join(caminho_dados, "olist_customers_dataset.csv"))
    df_produtos = pd.read_csv(os.path.join(caminho_dados, "olist_products_dataset.csv"))
    df_pedidos = pd.read_csv(os.path.join(caminho_dados, "olist_orders_dataset.csv"))
    df_itens = pd.read_csv(os.path.join(caminho_dados, "olist_order_items_dataset.csv"))
    df_pagamentos = pd.read_csv(os.path.join(caminho_dados, "olist_order_payments_dataset.csv"))
    df_vendedores = pd.read_csv(os.path.join(caminho_dados, "olist_sellers_dataset.csv"))

    #2. Limpeza e transformação dos dados
    colunas_data_pedidos = [
        "order_purchase_timestamp",
        "order_approved_at",
        "order_delivered_carrier_date",
        "order_delivered_customer_date",
        "order_estimated_delivery_date"
    ]

    for col in colunas_data_pedidos:
        df_pedidos[col] = pd.to_datetime(df_pedidos[col], errors='coerce')

    #Convertendo data de limite de envio na tabela de itens
    df_itens['shipping_limit_date'] = pd.to_datetime(df_itens['shipping_limit_date'], errors='coerce')

    #3. Integridade referencial: Garantindo que todos os pedidos em df_itens existam em df_pedidos
    #a) Garantindo que todo pedido está vinculado a um cliente existente
    df_pedidos = df_pedidos[df_pedidos['customer_id'].isin(df_clientes['customer_id'])]

    #b) Garantindo que os itens pertencem a pedidos válidos (existentes em df_pedidos)
    df_itens = df_itens[
        df_itens['order_id'].isin(df_pedidos['order_id']) &
        df_itens['product_id'].isin(df_produtos['product_id']) &
        df_itens['seller_id'].isin(df_vendedores['seller_id'])
    ]

    #c) Garantindo que os pagamentos pertencem a pedidos válidos (existentes em df_pedidos)
    df_pagamentos = df_pagamentos[df_pagamentos['order_id'].isin(df_pedidos['order_id'])]

    print ("Mapeamento e validação de integridade referencial concluídos com sucesso!")

    #4. Criando um dicionário com os DataFrames limpos
    return {
        "dim_clientes": df_clientes,
        "dim_produtos": df_produtos,
        "dim_vendedores": df_vendedores,
        "fato_pedidos": df_pedidos,
        "fato_itens": df_itens,
        "fato_pagamentos": df_pagamentos
    }