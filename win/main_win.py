#%%
import sqlite3
from consultas import get_vendedores, adicionar_coluna_numero_vendas, atualizar_numero_vendas
#%%
# 1. Conectar ou criar o banco de dados
conexao = sqlite3.connect("vendas_colaboradores.db")  # Cria ou conecta ao arquivo 'meu_banco.db'
cursor = conexao.cursor()  # Cria um cursor para executar comandos SQL
#%%
# 2. Criar uma tabela
cursor.execute("""
CREATE TABLE IF NOT EXISTS vendedores (
    id_vendedor INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_vendedor TEXT NOT NULL,
    idade INTEGER NOT NULL,
    pin TEXT UNIQUE NOT NULL,
    setor TEXT NOT NULL,
    supervisor TEXT NOT NULL
)
""")
print("Tabela criada ou já existente.")

## TABELA DE VENDAS
cursor.execute("""
CREATE TABLE IF NOT EXISTS vendas (
    id_produto INTEGER PRIMARY KEY AUTOINCREMENT,
    id_vendedor INTEGER NOT NULL,
    nome_produto TEXT NOT NULL,
    preco VARCHAR(100),
    FOREIGN KEY (id_vendedor) REFERENCES usuarios (id_vendedor)
)
""")
print("Tabela criada ou já existente.")
#%%
# 3. Inserir dados
try:
    cursor.execute("""
    INSERT OR IGNORE INTO vendedores (nome_vendedor, idade, pin, setor, supervisor)
    VALUES (?, ?, ?, ?, ?)
    """, ("João Silva", 30, "1234", "Vendas", "Maria Souza"))
    cursor.execute("""
    INSERT OR IGNORE INTO vendedores (nome_vendedor, idade, pin, setor, supervisor)
    VALUES (?, ?, ?, ?, ?)
    """, ("Ana Pereira", 28, "5678", "Marketing", "Carlos Lima"))

    cursor.execute("""
    INSERT OR IGNORE INTO vendedores (nome_vendedor, idade, pin, setor, supervisor)
    VALUES (?, ?, ?, ?, ?)
    """, ("Pedro Santos", 35, "9101", "TI", "Fernanda Costa"))
    
    cursor.execute("""
    INSERT OR IGNORE INTO vendas (id_vendedor, nome_produto, preco)
    VALUES (?, ?, ?)
    """, (1, "Notebook", 3000))

    cursor.execute("""
    INSERT OR IGNORE INTO vendas (id_vendedor, nome_produto, preco)
    VALUES (?, ?, ?)
    """, (3, "celular", 2000))
    cursor.execute("""
    INSERT OR IGNORE INTO vendas (id_vendedor, nome_produto, preco)
    VALUES (?, ?, ?)
    """, (2, "Tablet", 1500))

    cursor.execute("""
    INSERT OR IGNORE INTO vendas (id_vendedor, nome_produto, preco)
    VALUES (?, ?, ?)
    """, (1, "Monitor", 800))

    cursor.execute("""
    INSERT OR IGNORE INTO vendas (id_vendedor, nome_produto, preco)
    VALUES (?, ?, ?)
    """, (3, "Teclado", 200))

    cursor.execute("""
    INSERT OR IGNORE INTO vendas (id_vendedor, nome_produto, preco)
    VALUES (?, ?, ?)
    """, (2, "Mouse", 100))

    cursor.execute("""
    INSERT OR IGNORE INTO vendas (id_vendedor, nome_produto, preco)
    VALUES (?, ?, ?)
    """, (1, "Impressora", 600))

    print("Usuário inserido com sucesso.")
except sqlite3.IntegrityError as e:
    print("Erro ao inserir dados:", e)

conexao.commit()  # Salva as alterações no banco de dados

#%% 
# 4. Consultar dados
adicionar_coluna_numero_vendas("vendas_colaboradores.db")
atualizar_numero_vendas("vendas_colaboradores.db")
#%%
# 5. Fechar a conexão
conexao.commit()  # Salva as alterações no banco de dados
conexao.close()
print("\nConexão fechada.")

# %%
