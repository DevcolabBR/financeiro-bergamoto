#%%
import sqlite3
from tkinter import Tk, ttk
#%%
# Função para conectar ao banco
def conectar_banco():
    conexao = sqlite3.connect("bergamoto.db")
    cursor = conexao.cursor()
    return conexao, cursor
#%%
# Função para buscar dados do banco
def buscar_dados():
    conexao, cursor = conectar_banco()
    cursor.execute("SELECT name, setor, metas FROM vendedores")  # Altere a tabela e colunas conforme necessário
    dados = cursor.fetchall()
    conexao.close()
    return dados

# Função para criar a interface
def criar_interface():
    # Janela principal
    janela = Tk()
    janela.title("Tabela de Dados")

    # Criar Treeview
    colunas = ("Nome", "Setor", "Metas")
    tabela = ttk.Treeview(janela, columns=colunas, show="headings")

    # Configurar cabeçalhos
    for coluna in colunas:
        tabela.heading(coluna, text=coluna)
        tabela.column(coluna, width=100)

    # Inserir dados na tabela
    dados = buscar_dados()
    for item in dados:
        tabela.insert("", "end", values=item)

    # Empacotar tabela
    tabela.pack(fill="both", expand=True)

    # Executar janela
    janela.mainloop()

# Executar o programa
criar_interface()

# %%
