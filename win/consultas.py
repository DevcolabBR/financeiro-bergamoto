import sqlite3

db_path = "bergamoto.db" # Caminho do banco de dados

def get_vendedores(db_path):
    conexao = sqlite3.connect(db_path)
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE setor = 'vendas'")
    vendedores = cursor.fetchall()
    for vendedor in vendedores:
        print(vendedor)
    conexao.close()

def set_metas(db_path,nova_meta,setor):
    conexao = sqlite3.connect(db_path)
    cursor = conexao.cursor()
    cursor.execute("UPDATE usuarios SET metas = ? WHERE setor = ?", (nova_meta,setor))
    conexao.commit()
    conexao.close()

def create_vendedores(db_path):
    conexao = sqlite3.connect(db_path)
    cursor = conexao.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS vendedores AS
        SELECT * FROM usuarios WHERE setor = 'vendas'
                   ''')
    
    conexao.commit()
    conexao.close()

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

def adicionar_coluna_total_vendas(db_path):
    conexao = sqlite3.connect(db_path)
    cursor = conexao.cursor()
    
    # Adicionar uma nova coluna chamada `numero_vendas` na tabela vendedores
    cursor.execute("ALTER TABLE usuarios ADD COLUMN total_vendas INTEGER DEFAULT 0")
    
    conexao.commit()
    conexao.close()

def atualizar_total_vendas(db_path):
    conexao = sqlite3.connect(db_path)
    cursor = conexao.cursor()
    
    # Consulta para contar as vendas por vendedor
    query = """
    SELECT usuarios.id, SUM(vendas.valor_unitario) AS total_vendas
    FROM usuarios
    LEFT JOIN vendas ON usuarios.name = vendas.name
    GROUP BY usuarios.id
    """
    
    cursor.execute(query)
    resultados = cursor.fetchall()
    
    # Atualizar a tabela vendedores com os resultados
    for id_vendedor, total_vendas in resultados:
        cursor.execute(
            "UPDATE usuarios SET total_vendas = ? WHERE id = ?",
            (total_vendas, id_vendedor)
        )
    

def get_vendas_setor(db_path,setor):
        conexao = sqlite3.connect(db_path)
        cursor = conexao.cursor()
        query = """SELECT usuarios.setor,SUM(vendas.valor_unitario)
        FROM usuarios 
        LEFT JOIN vendas ON usuarios.name = vendas.name
        WHERE usuarios.setor = ?
        GROUP BY usuarios.setor
        """
        cursor.execute(query,(setor,))
        resultados = cursor.fetchall()

        #exibir resultados
        for setor, total_vendas in resultados :
            print(f"setor{setor},||Total de Vendas: {total_vendas}")
        conexao.close()
        
def get_mais_vendidos(db_path):
    conexao = sqlite3.connect(db_path)
    cursor = conexao.cursor()

    query = """
    SELECT produto, SUM(valor_unitario) AS total_vendas
    FROM vendas
    GROUP BY produto
    ORDER BY total_vendas DESC
    LIMIT 1
    """

    cursor.execute(query)
    resultado = cursor.fetchone()

    if resultado:
        produto, total_vendas = resultado
        print(f"Produto mais vendido: {produto}, Total Vendido: {total_vendas}")
    else:
        print("Nenhum produto encontrado.")

    conexao.close()