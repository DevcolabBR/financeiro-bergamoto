import sqlite3

db_path = "vendas_colaboradores.db" # Caminho do banco de dados

def get_vendedores(db_path):  # Função para consultar os vendedores
    # Conectar ao banco de dados
    conexao = sqlite3.connect(db_path)
    cursor = conexao.cursor()
    
    # Realizar a consulta
    cursor.execute("SELECT * FROM vendedores")
    vendedores = cursor.fetchall()
    
    # Fechar a conexão
    conexao.close()
    
    return vendedores

def get_num_vendas(db_path):  # Função para consultar o número de vendas por vendedor
    conexao = sqlite3.connect(db_path)
    cursor = conexao.cursor()
    cursor.execute("""
        SELECT v.nome, COUNT(vd.id_produto) as numero_vendas
        FROM vendedores v
        LEFT JOIN vendas vd ON v.rowid = vd.id_vendedor
        GROUP BY v.rowid
    """)
    numero_vendas = cursor.fetchall()
    conexao.close()
    return numero_vendas