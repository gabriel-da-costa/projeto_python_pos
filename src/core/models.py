"""
Módulo contendo as classes de modelo para manipulação de dados e estatísticas (OOP).
"""
import pandas as pd
from typing import List, Dict, Any

# Importa a função de programação funcional do outro módulo
from .metrics import analisar

class DataLoader:
    """
    Classe responsável por carregar e validar dados de um arquivo CSV.
    """
    def __init__(self, file_path: str):
        """
        Inicializa o DataLoader com o caminho do arquivo.

        Args:
            file_path (str): O caminho para o arquivo CSV.
        """
        self.file_path = file_path
        self.dataframe = None

    def load(self) -> pd.DataFrame:
        """
        Carrega o arquivo CSV e realiza validações básicas.

        Raises:
            FileNotFoundError: Se o arquivo não for encontrado.
            ValueError: Se as colunas essenciais ('preco', 'qtd') não estiverem presentes.

        Returns:
            pd.DataFrame: O DataFrame carregado e validado.
        """
        try:
            self.dataframe = pd.read_csv(self.file_path)
            self._validate_columns()
            return self.dataframe
        except FileNotFoundError:
            raise FileNotFoundError(f"Erro: O arquivo '{self.file_path}' não foi encontrado.")
        except Exception as e:
            raise Exception(f"Ocorreu um erro inesperado ao ler o arquivo: {e}")

    def _validate_columns(self):
        """Verifica se o DataFrame contém as colunas necessárias."""
        required_columns = ['preco', 'qtd']
        missing_columns = [col for col in required_columns if col not in self.dataframe.columns]
        if missing_columns:
            raise ValueError(f"Erro: Colunas ausentes no CSV: {', '.join(missing_columns)}")


class StatsService:
    """
    Classe para calcular estatísticas a partir de um DataFrame de vendas.
    """
    def __init__(self, dataframe: pd.DataFrame):
        """
        Inicializa o StatsService com um DataFrame.

        Args:
            dataframe (pd.DataFrame): O DataFrame contendo os dados de vendas.
        """
        if not isinstance(dataframe, pd.DataFrame):
            raise TypeError("O argumento 'dataframe' deve ser um DataFrame do Pandas.")
        self.df = dataframe.copy() # Cria uma cópia para evitar side effects
        self._prepare_data()

    def _prepare_data(self):
        """Adiciona colunas calculadas, como 'receita'."""
        if 'preco' in self.df.columns and 'qtd' in self.df.columns:
            self.df['receita'] = self.df['preco'] * self.df['qtd']
        else:
            raise ValueError("DataFrame deve conter as colunas 'preco' e 'qtd'.")

    def get_total_quantity(self) -> int:
        """Calcula a quantidade total de itens vendidos."""
        return int(self.df['qtd'].sum())

    def get_total_revenue(self) -> float:
        """Calcula a receita total."""
        return float(self.df['receita'].sum())

    def get_average_price(self) -> float:
        """Calcula o preço médio ponderado pela quantidade."""
        # Preço médio simples: self.df['preco'].mean()
        # Aqui calculamos a média do preço por item vendido
        if self.df['qtd'].sum() > 0:
             return float(self.df['receita'].sum() / self.df['qtd'].sum())
        return 0.0

    def run_fp_challenge(self, column_name: str, limit: int) -> Dict[str, Any]:
        """
        Executa o desafio de programação funcional sobre uma coluna do DataFrame.

        Args:
            column_name (str): O nome da coluna para aplicar o desafio (ex: 'qtd').
            limit (int): O limite a ser passado para a função 'analisar'.

        Returns:
            Dict[str, Any]: O resultado do desafio.
        """
        if column_name not in self.df.columns:
            raise ValueError(f"Coluna '{column_name}' não encontrada no DataFrame.")
        
        # Converte a coluna para uma lista de inteiros
        data_list = self.df[column_name].astype(int).tolist()
        
        # Reutiliza a função 'analisar'
        return analisar(data_list, limit)