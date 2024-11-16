import sqlite3

# 1. Conectar ou criar o banco de dados
conexao = sqlite3.connect("vendas_colaboradores.db")  # Cria ou conecta ao arquivo 'meu_banco.db'
cursor = conexao.cursor()  # Cria um cursor para executar comandos SQL

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

# 3. Inserir dados
try:
    cursor.execute("""
    INSERT OR IGNORE INTO vendedores (nome, idade, pin, setor, supervisor)
    VALUES (?, ?, ?, ?, ?)
    """, ("João Silva", 30, "1234", "Vendas", "Maria Souza"))
    cursor.execute("""
    INSERT OR IGNORE INTO vendedores (nome, idade, pin, setor, supervisor)
    VALUES (?, ?, ?, ?, ?)
    """, ("Ana Pereira", 28, "5678", "Marketing", "Carlos Lima"))

    cursor.execute("""
    INSERT OR IGNORE INTO vendedores (nome, idade, pin, setor, supervisor)
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

    print("Usuário inserido com sucesso.")
except sqlite3.IntegrityError as e:
    print("Erro ao inserir dados:", e)


     
# 4. Consultar dados
cursor.execute("SELECT * FROM vendedores")
usuarios = cursor.fetchall()  # Pega todos os registros
print("\nUsuários cadastrados:")
for usuario in usuarios:
    print(usuario)

# 5. Fechar a conexão
conexao.commit()  # Salva as alterações no banco de dados
conexao.close()
print("\nConexão fechada.")
