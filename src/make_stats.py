"""
Script principal para ler os dados, calcular as estatísticas e salvar em um arquivo JSON.
Este script utiliza as classes DataLoader e StatsService para organizar a lógica.
"""
import json
import sys
from core.models import DataLoader, StatsService

# Define os caminhos para os arquivos de entrada e saída
DATA_PATH = "data/dados.csv"
STATS_PATH = "src/stats.json"

def main():
    """
    Função principal que orquestra o processo de geração de estatísticas.
    """
    print("Iniciando a geração de estatísticas...")

    try:
        # 1. Carregar os dados usando a classe DataLoader
        data_loader = DataLoader(file_path=DATA_PATH)
        sales_df = data_loader.load()
        print(f"Dados carregados com sucesso de '{DATA_PATH}'.")

        # 2. Calcular as estatísticas usando a classe StatsService
        stats_service = StatsService(dataframe=sales_df)
        
        qtd_total = stats_service.get_total_quantity()
        receita_total = stats_service.get_total_revenue()
        preco_medio = stats_service.get_average_price()
        
        # 3. Executar o desafio de programação funcional
        desafio_fp_resultado = stats_service.run_fp_challenge(column_name='qtd', limit=2)
        print("Estatísticas e desafio FP calculados com sucesso.")

        # 4. Montar o dicionário final com todos os resultados
        stats = {
            "qtd_total": qtd_total,
            "receita_total": round(receita_total, 2),
            "preco_medio": round(preco_medio, 2),
            "desafio_fp": desafio_fp_resultado
        }

        # 5. Salvar os resultados no arquivo JSON
        with open(STATS_PATH, 'w', encoding='utf-8') as f:
            json.dump(stats, f, indent=2, ensure_ascii=False)
        
        print(f"Estatísticas salvas com sucesso em '{STATS_PATH}'.")

    except (FileNotFoundError, ValueError, TypeError, Exception) as e:
        # Captura e exibe erros de forma amigável
        print(f"\nERRO: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()