from conexao import conector

def criar_tabela():
    conexao,cursor = conector()
    if conector:
        try:
            cursor.execute("""

                CREATE TABLE IF NOT EXISTS produtos (
                id SERIAL PRIMARY KEY,
                nome TEXT NOT NULL,
                categoria TEXT NOT NULL,
                preco REAL NOT NULL,
            )
            """)
            conexao.commit()
        except Exception as erro:
            print(f"Erro ao criar a tabela{erro}")
        finally:
            cursor.close()
            conexao.commit()
    
      
def adicionar_produto(nome, preco):
    conexao, cursor = conector()
    if conexao: 
        try: 
            cursor.execute(
                "INSERT INTO profutos (nome, preco) VALUES (%s, %s, %s, %s)",
                (nome, preco)
                )
            conexao.commit()
        except Exception as erro: 
            print(f"Erro ao adicionar o produto {erro}")
        finally:
            cursor.close()
            conexao.commit()
            
def listar_produtos():
    conexao, cursor = conector()
    if conexao: 
        try: 
            cursor.execute(
                "SELECT * FROM produtos ORDER BY id"
                )
            return cursor.fetchall()
        except Exception as erro: 
            print(f"Erro ao listar os produtos {erro}")
            return []
        finally:
            cursor.close()
            conexao.commit()

def atualizar_produtos(nome, preco):
    conexao, cursor = conector()
    if conexao: 
        try: 
            cursor.execute(
                "UPDATE produtos SET nome = %s WHERE id = %s", (nome, preco)
                )
            conexao.commit()
        except Exception as erro: 
            print(f"Erro ao atualizar o produtos {erro}")
        finally:
            cursor.close()
            conexao.commit()

def deletar_filme(id_produtos):
    conexao, cursor = conector()
    if conexao: 
        try: 
            cursor.execute(
                "DELETE FROM produtos WHERE id = %s", (id_produtos,)
                )
            conexao.commit()
        except Exception as erro: 
            print(f"Erro ao deletar o produto {erro}")
        finally:
            cursor.close()
            conexao.commit()

def buscar_produtos(id_produtos):
    conexao, cursor = conector()
    if conexao: 
        try: 
            cursor.execute(
                "SELECT * FROM produtos WHERE id = %s", (id_produtos)
                )
            return cursor.fetchone()
            conexao.commit()
        except Exception as erro: 
            print(f"Erro ao deletar o produto {erro}")
            return []
        finally:
            cursor.close()
            conexao.commit()