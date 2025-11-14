from fastapi import FastAPI
from fastapi.responses import FileResponse
import funcao
#Como executar o fastapi
# python -m uvicorn main:app --reload

app = FastAPI(title="Gerenciador de produtps")

#Criando uma rota
@app.get("/")
def home():
    return { "mensagem": "Bem-vindo ao gerenciador de produtos"}

@app.post("/produtos")
def criar_produto(produto: str, preco: str):
    funcao.adicionar_produto(produto, preco)
    return {"mensagem": "produto adicionado com sucesso!"}
@app.get("/produtos")
def listar_produtos():
    produtos = funcao.listar_produtos()
    lista = []
    for linha in produtos:
        lista.append(
        {
            "id":linha [0],
            "nome":linha [1],
            "preco":linha [2],
        }
        )
    return{"produtos":lista}

@app.delete("/produtos/{id_produtos}")
def deletar_produtos(id_produtos: int):
    produtos = funcao.buscar_produtos(id_produtos)
    if produtos:
        funcao.deletar_produtos(id_produtos)
        return{"mensagem": "Produto excluido com sucesso!"}
    else:
        {"erro":"Produto não encotrado"}
        
app = FastAPI()

@app.get("/favicon.ico")
def favicon():
    return FileResponse("favicon.ico")



app = FastAPI()

@app.get("/")
def read_root():
    return {"msg": "API funcionando!"}