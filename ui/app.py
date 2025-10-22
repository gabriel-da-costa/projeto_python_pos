"""
Interface de usuário com Streamlit para consumir a API FastAPI.

Esta aplicação web permite:
1. Visualizar as principais métricas de vendas obtidas da API.
2. Testar o endpoint de soma através de um formulário.
3. Ver um gráfico de histograma da distribuição de preços dos produtos.
"""
import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# URL base da API (deve estar rodando localmente)
API_URL = "http://127.0.0.1:8000"
DATA_URL = "data/dados.csv"

# --- Configuração da Página ---
st.set_page_config(
    page_title="Dashboard de Vendas",
    page_icon="📊",
    layout="wide"
)

# --- Funções Auxiliares ---
def get_stats_from_api():
    """Busca as estatísticas do endpoint /stats da API."""
    try:
        response = requests.get(f"{API_URL}/stats")
        response.raise_for_status()  # Lança exceção para status de erro (4xx ou 5xx)
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Não foi possível conectar à API. Verifique se ela está rodando. Erro: {e}")
        return None

def post_soma_to_api(x, y):
    """Envia uma requisição de soma para o endpoint /soma da API."""
    try:
        payload = {"x": x, "y": y}
        response = requests.post(f"{API_URL}/soma", json=payload)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Erro ao chamar o endpoint de soma: {e}")
        return None

# --- Interface Principal ---
st.title("📊 Dashboard de Análise de Vendas")
st.markdown("Esta interface consome os dados da API FastAPI para apresentar as métricas de forma visual.")

# Busca os dados da API
stats = get_stats_from_api()

if stats:
    st.header("Métricas Principais")
    
    # Exibe as métricas em colunas
    col1, col2, col3 = st.columns(3)
    col1.metric("Receita Total", f"R$ {stats.get('receita_total', 0):,.2f}")
    col2.metric("Quantidade Vendida", f"{stats.get('qtd_total', 0):,}")
    col3.metric("Preço Médio por Item", f"R$ {stats.get('preco_medio', 0):.2f}")
    
    st.markdown("---")
    
    # --- Seção do Desafio de Programação Funcional ---
    st.header("Resultado do Desafio FP")
    fp_stats = stats.get('desafio_fp', {})
    
    fp_col1, fp_col2, fp_col3 = st.columns(3)
    fp_col1.metric("Soma dos Quadrados", f"{fp_stats.get('soma_quadrados', 0):,}")
    fp_col2.metric("Contagem de Itens", f"{fp_stats.get('contagem', 0):,}")
    fp_col3.metric("Média Inteira", f"{fp_stats.get('media_inteira', 0):,}")

    st.markdown("---")

    # --- Seção de Gráficos e Testes ---
    left_col, right_col = st.columns(2)

    with left_col:
        st.header("Histograma de Preços")
        try:
            df = pd.read_csv(DATA_URL)
            fig, ax = plt.subplots()
            sns.histplot(df['preco'], bins=20, kde=True, ax=ax)
            ax.set_title("Distribuição de Preços dos Produtos")
            ax.set_xlabel("Preço (R$)")
            ax.set_ylabel("Frequência")
            st.pyplot(fig)
        except FileNotFoundError:
            st.warning(f"Arquivo de dados '{DATA_URL}' não encontrado para gerar o gráfico.")
        except Exception as e:
            st.error(f"Ocorreu um erro ao gerar o gráfico: {e}")
    
    with right_col:
        st.header("Testar a API: Endpoint /soma")
        with st.form("soma_form"):
            num1 = st.number_input("Primeiro número (x)", value=10.5)
            num2 = st.number_input("Segundo número (y)", value=5.5)
            submitted = st.form_submit_button("Calcular Soma via API")
            
            if submitted:
                with st.spinner("Calculando..."):
                    result = post_soma_to_api(num1, num2)
                    if result:
                        st.success(f"O resultado da soma é: **{result.get('resultado')}**")
else:
    st.warning("Aguardando conexão com a API para exibir os dados...")
