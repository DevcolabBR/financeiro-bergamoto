#%%
import os
import sqlite3
from consultas import get_vendedores, adicionar_coluna_numero_vendas, atualizar_numero_vendas,set_metas,create_vendedores,get_vendas_setor,get_mais_vendidos,set_meta_alcancada

conexao = sqlite3.connect("bregamoto.db")
cursor = conexao.cursor() 
#%% 
# 4. Consultar vendedores
get_vendedores("bergamoto.db")
#%%
# 5. Definir metas-(funcionando para todos os setores)
set_metas("bergamoto.db",10000,"vendas")
#%%
# 6. CONSULTAR QUANTIDADE DE VENDAS POR VENDEDOR
adicionar_coluna_numero_vendas("bergamoto.db") ## OK
atualizar_numero_vendas("bergamoto.db") ## OK 
#%%
# CRIA TABELA DE VENDEDORES
create_vendedores("bergamoto.db") ## OK 
#%%
# CONSULTA $$$ VENDIDOS)
# %%
get_vendas_setor("bergamoto.db","vendas") ## OK
#%%
get_mais_vendidos("bergamoto.db") ## OK
#%%
set_meta_alcancada("bergamoto.db","vendas") ## OK
#Fechar a conexão
conexao.commit()  # Salva as alterações no banco de dados
conexao.close()
print("\nConexão fechada.")

# %%
