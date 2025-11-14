# pip install streamlit requests
import streamlit as st
import requests

#rodar o streamlit
# python -m streamlit run app.py

#URL da API Fastapi
API_URL = "http://127.0.0.1:8000"

menu = st.sidebar.radio("Menu", 
    ["Listar produtos", "Cadastrar produtos", "Deletar produtos", "Atualizar Produtos"]
)
if menu == "Listar produtos":
    st.subheader("Todos os produto")
    response = requests.get(f"{API_URL}/produtos")
    if response .status_code == 200:
        produtos = response.json().get("produtos", [])
        if produtos:
            st.dataframe(produtos)
        else:
            st.info("Nenhum produto cadastrado ainda!")
    else:
        st.error("Erro ao conectar com a APi.")

elif menu == "Cadastrar produtos":
    st.subheader("➕ Adicionar produtos")
    nome = st.text_input("nome do produto")
    categoria = st.text_input("categoria do produto")
    quantidade = st.number_input("quantidade de produtos", min_value=0, max_value=223100, step=1)
    preco = st.number_input("preço de produtos", min_value=0.0, max_value=10000.0, step=0.5)
    if st.button("Salvar produto"):
        dados = {"nome": nome, "categoria": categoria, "preco": preco, "quantidade": quantidade}
        response = requests.post(f"{API_URL}/produtos", params=dados)
        if response.status_code == 200:
            st.success("produto adicionado com sucesso!")
        else:
            st.error("Erro ao adicionar produto.")

elif menu == "Deletar produtos":
    st.subheader("🚮 Deletar produtos")
    id_produtos = st.number_input("Id doproduto a excluir", min_value=1, step=1)
    if st.button("Excluir"):
        response = requests.delete(f"{API_URL}/produtos/{id_produtos}")
        if response.status_code == 200:
            data = response.json()
            if "erro" not in data:
                st.success("produto excluido com sucesso!")
            else:
                st.error("Erro ao tentar excluir produto")
        else:
            st.error("Erro ao excluir o produto")
            
            
elif menu == "Atualizar Produtos":
    st.subheader("⬆ Atualizar Produtos")
    id_produtos = st.number_input("Id do produto a Atualizar", min_value=0, step=1)
    nova_quantidade = st.number_input("Nova quantidade", min_value=0, step=1)
    if st.button("Atualizar"):
        dados = {
            "id_produtos": id_produtos,
            "nova_quantidade": nova_quantidade
        }
        response = requests.put(f"{API_URL}/produtos/{id_produtos}", params=dados)
        if response.status_code == 200:
            data = response.json()
            if "erro" not in data:
                st.success("Produto Atualizado com sucesso!")
            else:
                st.error("Erro ao tentar Atualizar Produto")
        else:
            st.error("Erro ao tentar Atualizar Produto")