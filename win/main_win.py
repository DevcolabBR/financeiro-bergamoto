#%%
import os
import sqlite3
from consultas import get_vendedores, adicionar_coluna_numero_vendas, atualizar_numero_vendas,set_metas,create_vendedores,adicionar_coluna_total_vendas,atualizar_total_vendas

conexao = sqlite3.connect("bergamoto.db")
cursor = conexao.cursor() 
#%% 
# 4. Consultar vendedores
get_vendedores("bergamoto.db")

#%%
# 5. Definir metas-(APENAS SETOR DE VENDAS)
set_metas("bergamoto.db",400,"vendas")
#%%
# 6. CONSULTAR QUANTIDADE DE VENDAS POR VENDEDOR
adicionar_coluna_numero_vendas("bergamoto.db")
atualizar_numero_vendas("bergamoto.db")

#%%
# CRIA TABELA DE VENDEDORES
create_vendedores("bergamoto.db")
#%%
# CONSULTA $$$ VENDIDOS)
adicionar_coluna_total_vendas("bergamoto.db")
atualizar_total_vendas("bergamoto.db")
#Fechar a conexão
conexao.commit()  # Salva as alterações no banco de dados
conexao.close()
print("\nConexão fechada.")

# %%
