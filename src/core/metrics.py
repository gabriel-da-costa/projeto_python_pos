"""
Módulo para funções de cálculo usando programação funcional.
"""
from functools import reduce
from typing import List, Dict, Any

def analisar(lista: List[int], limite: int) -> Dict[str, Any]:
    """
    Aplica uma série de operações de programação funcional a uma lista de números.

    Regras:
    1. Filtra números pares que são maiores que o `limite`.
    2. Eleva ao quadrado cada número filtrado.
    3. Reduz a lista de quadrados para calcular a soma e a contagem.
    4. Retorna um dicionário com a soma dos quadrados, a contagem e a média inteira.

    Args:
        lista (List[int]): A lista de números a ser analisada.
        limite (int): O valor limite para o filtro.

    Returns:
        Dict[str, Any]: Um dicionário contendo 'soma_quadrados', 'contagem' e 'media_inteira'.
    """
    # 1. Filtra números pares maiores que o limite
    pares_filtrados = filter(lambda x: x % 2 == 0 and x > limite, lista)

    # 2. Eleva os números filtrados ao quadrado
    quadrados = map(lambda x: x**2, pares_filtrados)

    # 3. Reduz para acumular a soma e a contagem em uma única passada
    def acumulador(acc: tuple[int, int], valor: int) -> tuple[int, int]:
        """Função auxiliar para o reduce, acumula soma e contagem."""
        soma, contagem = acc
        return (soma + valor, contagem + 1)

    # O valor inicial para o reduce é (0, 0) -> (soma_inicial, contagem_inicial)
    soma_quadrados, contagem = reduce(acumulador, quadrados, (0, 0))

    # 4. Calcula a média inteira, tratando a divisão por zero
    media_inteira = soma_quadrados // contagem if contagem > 0 else 0

    return {
        "soma_quadrados": soma_quadrados,
        "contagem": contagem,
        "media_inteira": media_inteira,
    }