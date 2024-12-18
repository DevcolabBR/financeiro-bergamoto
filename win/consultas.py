import sqlite3
from consultas import get_vendedores

db_path = "bergamoto.db" # Caminho do banco de dados

def get_vendedores(db_path):
    conexao = sqlite3.connect(db_path)
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM colaboradores WHERE setor = 'vendas'")
    vendedores = cursor.fetchall()
    for vendedor in vendedores:
        print(vendedor)
    conexao.close()

def set_metas(db_path,nova_meta,setor):
    conexao = sqlite3.connect(db_path)
    cursor = conexao.cursor()
    cursor.execute("UPDATE colaboradores SET metas = ? WHERE setor = ?", (nova_meta,setor))
    conexao.commit()
    conexao.close()

def create_vendedores(db_path):
    conexao = sqlite3.connect(db_path)
    cursor = conexao.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS vendedores AS
        SELECT * FROM colaboradores WHERE setor = 'vendas'
                   ''')
    
    conexao.commit()
    conexao.close()

def adicionar_coluna_numero_vendas(db_path):
    conexao = sqlite3.connect(db_path)
    cursor = conexao.cursor()
    
    # Adicionar uma nova coluna chamada `numero_vendas` na tabela vendedores
    cursor.execute("ALTER TABLE colaboradores ADD COLUMN numero_vendas INTEGER DEFAULT 0")
    
    conexao.commit()
    conexao.close()

def atualizar_numero_vendas(db_path):
    conexao = sqlite3.connect(db_path)
    cursor = conexao.cursor()
    
    # Consulta para contar as vendas por vendedor
    query = """
    SELECT colaborador_id,
       SUM(pedidos.total) AS total_vendas
    FROM colaboradores
    JOIN pedidos ON colaboradores.id = pedidos.colaborador_id
    GROUP BY pedidos.colaborador_id
    ORDER BY total_vendas DESC;
    """
    cursor.execute(query)
    resultados = cursor.fetchall()
    
    # Atualizar a tabela vendedores com os resultados
    for id_vendedor, total_vendas in resultados:
        cursor.execute(
            "UPDATE colaboradores SET numero_vendas = ? WHERE id = ?",
            (total_vendas, id_vendedor)
        )
    
    conexao.commit()
    conexao.close() 

def get_vendas_setor(db_path,setor):
        conexao = sqlite3.connect(db_path)
        cursor = conexao.cursor()
        query_vendedores = """
        SELECT 
        colaboradores.setor, 
        colaboradores.name, 
        COUNT(pedidos.id) AS quantidade_vendas, 
        SUM(pedidos.total) AS total_vendas
        FROM colaboradores
        JOIN pedidos ON colaboradores.id = pedidos.colaborador_id
        WHERE colaboradores.setor = ?
        GROUP BY colaboradores.id
        ORDER BY quantidade_vendas DESC;
        """
        cursor.execute(query_vendedores, (setor,))
        resultados = cursor.fetchall()

        #exibir resultados
        a = 0
        for setor, nome, quantidade_vendas, total_vendas in resultados:
            
            a = a + total_vendas
            print(f"Setor: {setor}, Nome: {nome}, Quantidade de Vendas: {quantidade_vendas}, Total de Vendas: {total_vendas}")
        
        print("==============================================================================================================")
        print("Total de Vendas do Setor: ",a)

        
        conexao.close()
        
def get_mais_vendidos(db_path):
    conexao = sqlite3.connect(db_path)
    cursor = conexao.cursor()

    query = """
    SELECT produtos.nome,COUNT(itens_pedido.produto_id) AS total_vendas
    FROM itens_pedido
    JOIN produtos ON itens_pedido.produto_id = produtos.id
    GROUP BY itens_pedido.produto_id
    LIMIT 5
    """

    cursor.execute(query)
    resultado = cursor.fetchone()

    if resultado:
        produto, total_vendas = resultado
        print(f"Produto mais vendido: {produto}, Total Vendido: {total_vendas}")
    else:
        print("Nenhum produto encontrado.")
    conexao.close()

def set_meta_alcancada(db_path):
    conexao = sqlite3.connect(db_path)
    cursor = conexao.cursor()

    query = """
    SELECT colaborador.name, metas, numero_vendas
    FROM colaboradores
    WHERE numero_vendas >= metas
    """
    cursor.execute(query)
    resultado = cursor.execute(query).fetchone()

    if resultado:
        name, meta, vendas = resultado
        print(f"Colaborador {name} atingiu a meta de {meta} com {vendas} vendas.")