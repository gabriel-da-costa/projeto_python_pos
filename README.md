Mini-Projeto Integrado em Python

Este projeto é uma aplicação completa que integra análise de dados com Pandas, um desafio de programação funcional, uma API com FastAPI e uma interface de usuário com Streamlit.

Objetivo

O objetivo principal é demonstrar a integração de diferentes tecnologias Python em um único projeto coeso, cobrindo desde a manipulação de dados até a exposição dos resultados através de uma API e uma interface web.

Estrutura do Projeto

projeto_python_pos/
├── data/
│   └── dados.csv
├── src/
│   ├── core/
│   │   ├── __init__.py
│   │   ├── metrics.py      
│   │   └── models.py      
│   ├── __init__.py
│   ├── app.py              
│   ├── make_stats.py      
│   └── stats.json         
├── ui/
│   └── app.py              
├── .gitignore
├── requirements.txt
└── README.md


Como Executar o Projeto

Siga os passos abaixo para configurar e rodar a aplicação.

1. Pré-requisitos

Python 3.8 ou superior

pip (gerenciador de pacotes do Python)

2. Instalação

Primeiro, clone o repositório e navegue para a pasta do projeto. Em seguida, crie um ambiente virtual e instale as dependências:

# Criar e ativar um ambiente virtual (recomendado)
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate

# Instalar as dependências
pip install -r requirements.txt


3. Gerar as Estatísticas

Antes de iniciar a API, gerar o arquivo stats.json. Este arquivo contém os cálculos feitos a partir do dados.csv.

Execute o seguinte comando na raiz do projeto:

python src/make_stats.py


Isso irá criar (ou sobrescrever) o arquivo src/stats.json com as estatísticas atualizadas.

4. Iniciar a API FastAPI

Com as estatísticas geradas, você pode iniciar o servidor da API.

uvicorn src.app:app --reload


A API estará disponível em http://127.0.0.1:8000.

5. Iniciar a Interface Streamlit (Opcional)

Para visualizar os dados de forma interativa, abra um novo terminal (mantendo a API rodando no primeiro) e execute a aplicação Streamlit:

streamlit run ui/app.py


A interface do Streamlit estará disponível em http://localhost:8501.

Screenshots da API

<img width="1364" height="672" alt="Image" src="https://github.com/user-attachments/assets/2fa5da5f-db05-455f-afb4-3ae36da74ca4" />

<img width="1359" height="629" alt="Image" src="https://github.com/user-attachments/assets/8a7b5601-b6f8-4f28-ac54-fb980b1b4347" />

Aqui estão exemplos dos retornos da API após a execução.

Documentação Interativa (/docs)

Acesse http://127.0.0.1:8000/docs para ver a documentação gerada automaticamente pelo FastAPI.

<img width="1362" height="480" alt="Image" src="https://github.com/user-attachments/assets/52852970-81c9-4094-9510-609c85027288" />

Retorno do Endpoint (/stats)

Acesse http://127.0.0.1:8000/stats para ver o conteúdo do stats.json.

<img width="1358" height="676" alt="Image" src="https://github.com/user-attachments/assets/a9e0a077-c96c-48d6-9768-96e1f21eed7b" />
