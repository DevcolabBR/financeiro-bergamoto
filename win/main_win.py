#%%
import os
import sqlite3
from consultas import get_vendedores, adicionar_coluna_numero_vendas, atualizar_numero_vendas

# Ensure the 'data' directory exists
os.makedirs("data", exist_ok=True)

# 1. Conectar ou criar o banco de dados
conexao = sqlite3.connect("data/bergamoto.db")
cursor = conexao.cursor()  # Cria um cursor para executar comandos SQL
  # Cria um cursor para executar comandos SQL
#%%
#%% 
# 4. Consultar dados
get_vendedores("data/bergamoto.db")
#%%
# 5. Fechar a conexão
conexao.commit()  # Salva as alterações no banco de dados
conexao.close()
print("\nConexão fechada.")

# %%
