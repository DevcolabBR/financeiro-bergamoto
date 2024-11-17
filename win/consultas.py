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

def get_num_vendas(db_path):  # Retorna o número de vendas por vendedor
    conexao = sqlite3.connect(db_path)
    cursor = conexao.cursor()

    # Consulta para contar as vendas por vendedor
    query = """
    SELECT vendedores.nome_vendedor, COUNT(vendas.id_produto) AS total_vendas
    FROM vendedores
    LEFT JOIN vendas ON vendedores.id_vendedor = vendas.id_vendedor
    GROUP BY vendedores.id_vendedor
    """
    cursor.execute(query)
    resultados = cursor.fetchall()

    conexao.close()
    return resultados
