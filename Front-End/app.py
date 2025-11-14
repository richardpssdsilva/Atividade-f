# pip install streamlit requests

import streamlit as st
import requests

#URL da API Fastapi
API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="produtos", layout="wide")

st.title("Gerenciador de Produtos")


menu = st.sidebar.radio("Navegação",
    ["Listar produtos","Adicionar produtos"]
    )
if menu == "Listar Produtos":
    st.subheader(" lProdutos em Geral")
    response = requests.get(f"{API_URL}/produtos")
    if response.status_code == 200:
        st.write("Sucesso !!")
        produtos = response.json().get("produtos",[])
        if produtos:
            st.dataframe(produtos)
        else:
            st.info("Nenhum produto cadastrado ainda!")
    else:
        st.error("Erro de conexão com a API.")

elif menu == "Adicionar Produtos":
    st.subheader("➕ Adicionar produtos")
    nome = st.text_input("Titulo produtos")
    preco = st.number_input("Nota (0 a 10 )", min_value=0.0, max_value=10.0, step=0.5)
    if st.button("Salvar produtos"):
        dados = {"nome ":nome,"preco":preco}
        response = requests.post(f"{API_URL}/produtos",params=dados)
        if response.status_code == 200:
            st.success("profuto,e adicionado com sucesso!")
        else:
            st.error("Erro ao adicionar o produto")

elif menu=="Deletar Produtos":
    st.subheader(" 🚮  Deletar Produtos")
    id_produtos = st.number_input("Id do produto a excluir", max_value=1, step=1)
    if st.button("Excluir"):
        response = requests.delete(f"{API_URL}/produto/{id_produtos}")
        if response.status_code == 200:
            data = response.json()
            if "erro" not in data:
                st.success("Produto excluido com sucesso!")
            else:
                st.error("Erro ao tentar excluir produto")
        else:
            st.error("Erro ao tentar excluir produto")


elif menu == "Atualizar produtos":
    st.subheader("⬆ Atualizar produtos")
    id_produtos = st.number_input("Id do produtp a Atualizar", max_value=1, step=1)
    if st.button("Atualizar"):
        response = requests.up(f"{API_URL}/produto/{id_produtos}")
        if response.status_code == 200:
            data = response.json()
            if "erro" not in data:
                st.success("Produto Atualizado com sucesso!")
            else:
                st.error("Erro ao tentar Atualizar Produto")
        else:
            st.error("Erro ao tentar Atualizar Produto")


        

