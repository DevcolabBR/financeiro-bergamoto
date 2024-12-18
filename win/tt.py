#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sqlite3

#%%
def plot_vendas_por_categoria():
    con = sqlite3.connect('bergamoto.db')
    df_vendas_produtos = pd.read_sql_query("""
       SELECT produtos.nome,produtos.categoria,COUNT(itens_pedido.produto_id) AS total_vendas
        FROM itens_pedido
        JOIN produtos ON itens_pedido.produto_id = produtos.id
        GROUP BY itens_pedido.produto_id
    """, con)
    venda_categoria = df_vendas_produtos.groupby('categoria')['total_vendas'].sum().reset_index()
    # -- VENDAS POR CATEGORIA --
    plt.figure(figsize=(11, 6))
    plt.bar(venda_categoria['categoria'], venda_categoria['total_vendas'])
    plt.xlabel('Categoria')
    plt.grid(axis='y')
    plt.ylabel('Total de Vendas')
    plt.title('Quantidade de Vendas por Categoria')
    plt.show()
    con.close()
#%% -- FUNCIONARIOS POR SETOR -- 
def plot_vendedores_destaque():
    con = sqlite3.connect('bergamoto.db')
    df_vendedores_destaque = pd.read_sql_query("""
        SELECT vendedores.name, SUM(pedidos.total) AS total_vendas
        FROM pedidos
        JOIN vendedores ON pedidos.colaborador_id = vendedores.id
        GROUP BY vendedores.id
        ORDER BY total_vendas DESC
    """, con)
    vendedores_destaque = df_vendedores_destaque.head(5)
    plt.figure(figsize=(10, 6))
    plt.bar(vendedores_destaque['name'], vendedores_destaque['total_vendas'])
    plt.xlabel('Vendedores')
    plt.grid(axis='y')
    plt.ylabel('Total em vendas')
    plt.title('Vendedores em Destaque (2024)')
    plt.show()
    con.close()



# %% -- FUNCIONARIOS POR SETOR -- 
def plot_funcionarios_por_setor():
    con = sqlite3.connect('bergamoto.db')
    df_funcionarios_setor = pd.read_sql_query("""
        SELECT colaboradores.setor, COUNT(colaboradores.id) AS total_funcionarios
        FROM colaboradores
        GROUP BY colaboradores.setor
    """, con)
    plt.figure(figsize=(10, 6))
    plt.bar(df_funcionarios_setor['setor'], df_funcionarios_setor['total_funcionarios'])
    plt.xlabel('Setor')
    plt.grid(axis='y')
    plt.ylabel('Total de Funcionários')
    plt.title('Funcionários por Setor')
    plt.show()
    con.close()

# %%
