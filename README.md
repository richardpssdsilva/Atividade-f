📦 Sistema de Gerenciamento de Estoque

Aplicação completa para controle de produtos, desenvolvida em Python, com interface web em Streamlit e banco de dados PostgreSQL.
Permite cadastrar, visualizar, atualizar e remover itens do estoque de forma simples e rápida.

🚀 Tecnologias Utilizadas

Python 3.x

Streamlit

PostgreSQL

psycopg2 ou SQLAlchemy

Pandas

🌟 Funcionalidades

✔ Cadastro de produtos
✔ Listagem de itens do estoque
✔ Atualização de informações (nome, preço, quantidade, categoria)
✔ Remoção de produtos
✔ Controle de quantidade em tempo real
✔ Interface web intuitiva e responsiva
✔ Conexão com banco de dados PostgreSQL

📂 Estrutura do Projeto
📦 estoque
├── app.py               # Interface e lógica principal da aplicação
├── database.py          # Conexão e operações no PostgreSQL
├── requirements.txt     # Dependências do projeto
├── README.md            # Documentação

Crie um banco no PostgreSQL e execute:

CREATE TABLE produtos (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    quantidade INTEGER NOT NULL,
    preco NUMERIC(10,2),
    categoria VARCHAR(50)
);


Edite o arquivo database.py com suas credenciais PostgreSQL:

conn = psycopg2.connect(
    host="localhost",
    database="seu_banco",
    user="seu_usuario",
    password="sua_senha",
    port="5432"
)

▶️ Executar o Sistema
streamlit run app.py


A aplicação abrirá automaticamente no navegador (geralmente em http://localhost:8501).

🖥 Prévia da Interface

Exemplo de como o usuário verá o sistema (opcional para o README).
Você pode adicionar imagens ou GIFs futuramente.

📌 Melhorias Futuras (Sugestões)

Login e autenticação de usuários

Sistema de permissões

Dashboard com gráficos (Plotly/Altair)

Exportação de relatórios (CSV, PDF)

Histórico de movimentações do estoque

Dockerização da aplicação

🤝 Contribuição

Sinta-se livre para abrir issues ou enviar pull requests.
Feedbacks são sempre bem-vindos! 😊