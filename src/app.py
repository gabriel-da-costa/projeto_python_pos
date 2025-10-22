"""
Módulo da API FastAPI.

Fornece endpoints para:
- Verificar a saúde da aplicação (`/health`).
- Obter as estatísticas calculadas (`/stats`).
- Realizar uma operação de soma (`/soma`).
"""
import json
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict, Any

# Cria a instância da aplicação FastAPI
app = FastAPI(
    title="API de Análise de Vendas",
    description="Uma API para fornecer estatísticas de vendas e operações simples.",
    version="1.0.0"
)

# Caminho para o arquivo de estatísticas
STATS_FILE_PATH = "src/stats.json"

# Modelo Pydantic para a requisição do endpoint /soma
class SomaRequest(BaseModel):
    """Modelo para os dados de entrada da operação de soma."""
    x: float
    y: float

# Modelo Pydantic para a resposta do endpoint /soma
class SomaResponse(BaseModel):
    """Modelo para a resposta da operação de soma."""
    resultado: float

@app.get("/health", summary="Verifica a saúde da API")
def health_check() -> Dict[str, str]:
    """
    Endpoint de verificação de saúde. Retorna um status 'ok' se a API estiver funcionando.
    """
    return {"status": "ok"}


@app.get("/stats", summary="Retorna as estatísticas de vendas")
def get_stats() -> Dict[str, Any]:
    """
    Lê e retorna o conteúdo do arquivo `stats.json`.
    Levanta uma exceção HTTP 404 se o arquivo não for encontrado.
    """
    try:
        with open(STATS_FILE_PATH, 'r', encoding='utf-8') as f:
            stats = json.load(f)
        return stats
    except FileNotFoundError:
        raise HTTPException(
            status_code=404,
            detail="Arquivo de estatísticas não encontrado. Execute 'python src/make_stats.py' primeiro."
        )
    except json.JSONDecodeError:
        raise HTTPException(
            status_code=500,
            detail="Erro ao ler o arquivo de estatísticas. O arquivo pode estar corrompido."
        )


@app.post("/soma", response_model=SomaResponse, summary="Realiza a soma de dois números")
def soma(request: SomaRequest) -> SomaResponse:
    """
    Recebe dois números (`x` e `y`) e retorna a soma deles.
    """
    resultado = request.x + request.y
    return SomaResponse(resultado=resultado)
