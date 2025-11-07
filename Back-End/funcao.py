from conexao import conector

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