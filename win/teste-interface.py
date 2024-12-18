#%%
import tkinter as tk
import sqlite3
from tkinter import ttk
from consultas import buscar_vendedores
from tt import plot_vendas_por_categoria, plot_vendedores_destaque

def conectar_banco():
    conexao = sqlite3.connect("bergamoto.db")
    cursor = conexao.cursor()
    return conexao, cursor
# Função do botão
def gerar_grafico():
    plot_vendedores_destaque()

def atualizar_colunas():
    # Obter colunas visíveis
    colunas_visiveis = [filtro for filtro, var in toggle_vars.items() if var.get()]
    
    # Atualizar colunas da tabela
    tabela["columns"] = colunas_visiveis
    for coluna in colunas_visiveis:
        tabela.heading(coluna, text=coluna)
        tabela.column(coluna, width=100)
    
    # Remover colunas não visíveis
    for coluna in tabela["columns"]:
        if coluna not in colunas_visiveis:
            tabela.heading(coluna, text="")
            tabela.column(coluna, width=0)

# Criação da janela principal
root = tk.Tk()
root.title("Financeiro Bergamoto")
root.geometry("600x400")
root.configure(bg="#333333")

# Título principal
titulo = tk.Label(root, text="Financeiro Bergamoto", font=("Arial", 14, "bold"), bg="#333333", fg="#66CCCC", anchor="w")
titulo.pack(fill="x", pady=10)

# Frame principal
main_frame = tk.Frame(root, bg="#333333")
main_frame.pack(fill="both", expand=True, padx=10, pady=10)

# Seção de filtros
filtro_frame = tk.LabelFrame(main_frame, text="Filtros", bg="#DDDDDD", font=("Arial", 10, "bold"))
filtro_frame.pack(side="left", padx=10, pady=10, anchor="n")

# Criação dos botões de alternância (filtros)
filtros = ["name","setor","metas","ponto_acumulado","numero_vendas"]
toggle_vars = {}

for filtro in filtros:
    var = tk.BooleanVar(value=True)  # Começam todos como habilitados
    toggle_vars[filtro] = var
    checkbox = ttk.Checkbutton(filtro_frame, text=filtro, variable=var, onvalue=True, offvalue=False, command=atualizar_colunas)
    checkbox.pack(anchor="w", padx=10, pady=2)

# Botão "Gerar gráfico"
botao_grafico = tk.Button(filtro_frame, text="Gerar gráfico", command=gerar_grafico)
botao_grafico.pack(pady=10)


# Tabela de vendedores
tabela_frame = tk.Frame(main_frame)
tabela_frame.pack(side="right", fill="both", expand=True)

# Criando a tabela (Treeview)
colunas = ("Nome", "Setor", "Metas","ponto_acumulado","numero_vendas")
tabela = ttk.Treeview(tabela_frame, columns=colunas, show="headings")

# Configurar cabeçalhos
for coluna in colunas:
    tabela.heading(coluna, text=coluna)
    tabela.column(coluna, width=100)

# Inserir dados na tabelas
dados = buscar_vendedores("bergamoto.db")
for item in dados:
    tabela.insert("", "end", values=item)

# Empacotar tabela
tabela.pack(fill="both", expand=True)

# Definindo títulos das colunas
for col in colunas:
    tabela.heading(col, text=col)
    tabela.column(col, anchor="center", width=100)

# Adicionando a tabela à interface
tabela.pack(fill="both", expand=True)

# Inicializar colunas visíveis
atualizar_colunas()

# Executando o loop da interface
root.mainloop()

# %%
