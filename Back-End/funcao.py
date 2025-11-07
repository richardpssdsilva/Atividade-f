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
            
