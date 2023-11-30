import requests
from datetime import datetime
import click
import logging

# Configuração do logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def converter_data(data_str):
    """Converte uma string de data para um objeto datetime."""
    return datetime.strptime(data_str, '%Y-%m-%dT%H:%M:%SZ')

def formatar_data(data):
    """Formata um objeto datetime em uma string mais legível."""
    return data.strftime('%Y-%m-%d %H:%M:%S')

def exibir_info_repositorio(repo):
    """Exibe informações formatadas de um repositório."""
    logger.info(f"Repositório: {repo['nome']}, Estrelas: {repo['estrelas']}, Forks: {repo['forks']}")
    logger.info(f"Link: {repo['link']}")
    logger.info(f"Criado em: {repo['data_criacao']}, Atualizado em: {repo['data_atualizacao']}\n")

def coletar_repositorios(config, num_paginas=None):
    """Coleta informações sobre repositórios no GitHub.

    Args:
        config (dict): Configurações específicas para o tipo de repositório.
        num_paginas (int): Número de páginas a serem consultadas.

    Returns:
        list: Lista de repositórios coletados.
    """
    repositorios = []  # Lista para armazenar os repositórios coletados

    try:
        for _ in range(int(num_paginas)) if num_paginas else range(1):
            # Faz a solicitação HTTP
            response = requests.get(config['github_api_url'], params=config['query_params'])
            response.raise_for_status()  # Lança uma exceção para erros HTTP

            # Converte a resposta para formato JSON
            data = response.json()

            # Itera sobre os repositórios
            for repo in data['items']:
                nome = repo['name']
                estrelas = repo['stargazers_count']
                forks = repo['forks']
                link = repo['html_url']
                data_criacao = converter_data(repo['created_at'])
                data_atualizacao = converter_data(repo['updated_at'])

                repositorios.append({
                    'nome': nome,
                    'estrelas': estrelas,
                    'forks': forks,
                    'link': link,
                    'data_criacao': formatar_data(data_criacao),
                    'data_atualizacao': formatar_data(data_atualizacao)
                })

    except requests.exceptions.RequestException as e:
        logger.error(f"Erro ao fazer a solicitação HTTP: {e}")

    return repositorios

@click.command()
@click.option(
    '--tipo-repositorio',
    type=click.Choice(['linguagem', 'IA', 'machine_learning', 'back_end', 'front_end', 'outros'], case_sensitive=False),
    prompt='Escolha o tipo de repositório',
    help='O tipo de repositório no GitHub.'
)
@click.option(
    '--ordenacao',
    type=click.Choice(['stars', 'forks', 'updated'], case_sensitive=False),
    prompt='Escolha a ordenação',
    help='O critério de ordenação dos repositórios.'
)
@click.option(
    '--linguagem',
    type=str,
    prompt='Informe a linguagem desejada (por exemplo, Python, Java, Ruby)',
    help='A linguagem de programação desejada.'
)
@click.option(
    '--num-paginas',
    type=int,
    help='Número de páginas a serem consultadas.'
)
def main(tipo_repositorio, ordenacao, linguagem, num_paginas):
    try:
        # Configuração específica para o tipo de repositório
        config = {
            'github_api_url': 'https://api.github.com/search/repositories',
            'query_params': {
                'q': f'language:{linguagem}',
                'sort': ordenacao,
                'page': '1'
            }
        }

        # Coleta os repositórios
        repositorios = coletar_repositorios(config, num_paginas)

        # Exibe informações dos repositórios
        for repo in repositorios:
            exibir_info_repositorio(repo)

    except click.Abort:
        logger.info("Operação abortada pelo usuário.")
    except Exception as e:
        logger.error(f"Erro inesperado: {e}")

if __name__ == '__main__':
    main()
