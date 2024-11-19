import sqlite3

db_path = "data/bergamoto.db" # Caminho do banco de dados

def get_vendedores(db_path):  # Função para consultar os vendedores
    # Conectar ao banco de dados
    conexao = sqlite3.connect(db_path)
    cursor = conexao.cursor()
    
    # Realizar a consulta
    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall()
    
    # Fechar a conexão
    conexao.close()
    
    return usuarios

def adicionar_coluna_numero_vendas(db_path):
    conexao = sqlite3.connect(db_path)
    cursor = conexao.cursor()
    
    # Adicionar uma nova coluna chamada `numero_vendas` na tabela vendedores
    cursor.execute("ALTER TABLE usuarios ADD COLUMN numero_vendas INTEGER DEFAULT 0")
    
    conexao.commit()
    conexao.close()

def atualizar_numero_vendas(db_path):
    conexao = sqlite3.connect(db_path)
    cursor = conexao.cursor()
    
    # Consulta para contar as vendas por vendedor
    query = """
    SELECT usuarios.id, COUNT(vendas.id) AS total_vendas
    FROM usuarios
    LEFT JOIN vendas ON usuarios.name = vendas.name
    GROUP BY usuarios.id
    """
    
    cursor.execute(query)
    resultados = cursor.fetchall()
    
    # Atualizar a tabela vendedores com os resultados
    for id_vendedor, total_vendas in resultados:
        cursor.execute(
            "UPDATE usuarios SET numero_vendas = ? WHERE id = ?",
            (total_vendas, id_vendedor)
        )
    
    conexao.commit()
    conexao.close()

def get_num_vendas(db_path):  # Função para consultar o número de vendas por vendedor
    conexao = sqlite3.connect(db_path)
    cursor = conexao.cursor()
    cursor.execute("""
        SELECT v.nome, COUNT(vd.id) as numero_vendas
        FROM usuarios v
        LEFT JOIN vendas vd ON v.rowid = vd.name
        GROUP BY v.rowid
    """)
    numero_vendas = cursor.fetchall()
    conexao.close()
    return numero_vendas
