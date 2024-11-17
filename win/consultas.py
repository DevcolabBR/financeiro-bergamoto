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


def adicionar_coluna_numero_vendas(db_path):
    conexao = sqlite3.connect(db_path)
    cursor = conexao.cursor()
    
    # Adicionar uma nova coluna chamada `numero_vendas` na tabela vendedores
    cursor.execute("ALTER TABLE vendedores ADD COLUMN numero_vendas INTEGER DEFAULT 0")
    
    conexao.commit()
    conexao.close()

def atualizar_numero_vendas(db_path):
    conexao = sqlite3.connect(db_path)
    cursor = conexao.cursor()
    
    # Consulta para contar as vendas por vendedor
    query = """
    SELECT vendedores.id_vendedor, COUNT(vendas.id_produto) AS total_vendas
    FROM vendedores
    LEFT JOIN vendas ON vendedores.id_vendedor = vendas.id_vendedor
    GROUP BY vendedores.id_vendedor
    """
    
    cursor.execute(query)
    resultados = cursor.fetchall()
    
    # Atualizar a tabela vendedores com os resultados
    for id_vendedor, total_vendas in resultados:
        cursor.execute(
            "UPDATE vendedores SET numero_vendas = ? WHERE id_vendedor = ?",
            (total_vendas, id_vendedor)
        )
    
    conexao.commit()
    conexao.close()

