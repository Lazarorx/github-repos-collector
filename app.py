import requests
from datetime import datetime, timedelta
import click
import logging
import csv
import json
import os
from pathlib import Path
from typing import List, Dict, Optional, Any, Tuple
from tqdm import tqdm
import time
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text
from rich import box

# Configuração do logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Console Rich para output formatado
console = Console()

# Diretório para cache e exportações
CACHE_DIR = Path("cache")
EXPORT_DIR = Path("exports")
CONFIG_DIR = Path.home() / ".grc"
CACHE_DIR.mkdir(exist_ok=True)
EXPORT_DIR.mkdir(exist_ok=True)
CONFIG_DIR.mkdir(exist_ok=True)

# Arquivo de configuração
CONFIG_FILE = CONFIG_DIR / "config.json"


def get_github_token() -> Optional[str]:
    """Obtém o token do GitHub de várias fontes.
    
    Ordem de prioridade:
    1. Variável de ambiente GITHUB_TOKEN
    2. Arquivo de configuração ~/.grc/config.json
    
    Returns:
        Token do GitHub ou None se não encontrado.
    """
    # 1. Variável de ambiente
    token = os.environ.get('GITHUB_TOKEN')
    if token:
        return token
    
    # 2. Arquivo de configuração
    if CONFIG_FILE.exists():
        try:
            with open(CONFIG_FILE, 'r') as f:
                config = json.load(f)
                return config.get('github_token')
        except Exception as e:
            logger.warning(f"Erro ao ler configuração: {e}")
    
    return None


def save_github_token(token: str) -> None:
    """Salva o token do GitHub no arquivo de configuração.
    
    Args:
        token: Token do GitHub para salvar.
    """
    config = {}
    if CONFIG_FILE.exists():
        try:
            with open(CONFIG_FILE, 'r') as f:
                config = json.load(f)
        except:
            pass
    
    config['github_token'] = token
    
    with open(CONFIG_FILE, 'w') as f:
        json.dump(config, f, indent=2)
    
    # Proteger o arquivo (apenas leitura/escrita pelo usuário)
    try:
        os.chmod(CONFIG_FILE, 0o600)
    except:
        pass  # Windows pode não suportar chmod


def get_auth_headers() -> Tuple[Dict[str, str], bool]:
    """Obtém os headers de autenticação para a API do GitHub.
    
    Returns:
        Tupla com (headers, is_authenticated)
    """
    token = get_github_token()
    
    if token:
        return {
            'Authorization': f'token {token}',
            'Accept': 'application/vnd.github.v3+json'
        }, True
    else:
        return {
            'Accept': 'application/vnd.github.v3+json'
        }, False


def show_auth_status() -> None:
    """Mostra o status de autenticação."""
    token = get_github_token()
    
    if token:
        # Mascarar token (mostrar apenas primeiros e últimos 4 caracteres)
        masked = f"{token[:4]}...{token[-4:]}" if len(token) > 8 else "****"
        click.secho("🔑 Autenticação: Ativa", fg='green', bold=True)
        click.echo(f"   Token: {masked}")
        click.echo(f"   Rate Limit: 5000 requisições/hora")
    else:
        click.secho("⚠️  Autenticação: Não configurada", fg='yellow', bold=True)
        click.echo(f"   Rate Limit: 60 requisições/hora")
        click.echo()
        click.echo("💡 Dica: Configure um token para aumentar o rate limit:")
        click.echo("   1. Crie um token em: https://github.com/settings/tokens")
        click.echo("   2. Configure com: export GITHUB_TOKEN='seu_token'")
        click.echo("   3. Ou use: python app.py config set-token seu_token")
    
    click.echo()

def converter_data(data_str: str) -> datetime:
    """Converte uma string de data para um objeto datetime.
    
    Args:
        data_str: String de data no formato ISO 8601 (YYYY-MM-DDTHH:mm:ssZ).
    
    Returns:
        Objeto datetime correspondente.
    
    Raises:
        ValueError: Se a string não estiver no formato esperado.
    """
    return datetime.strptime(data_str, '%Y-%m-%dT%H:%M:%SZ')

def formatar_data(data: datetime) -> str:
    """Formata um objeto datetime em uma string mais legível.
    
    Args:
        data: Objeto datetime a ser formatado.
    
    Returns:
        String formatada no padrão 'YYYY-MM-DD HH:mm:ss'.
    """
    return data.strftime('%Y-%m-%d %H:%M:%S')

def exibir_info_repositorio(repo: Dict[str, Any]) -> None:
    """Exibe informações formatadas de um repositório (modo legado).
    
    Args:
        repo: Dicionário contendo informações do repositório.
    """
    logger.info(f"Repositório: {repo['nome']}, Estrelas: {repo['estrelas']}, Forks: {repo['forks']}")
    logger.info(f"Link: {repo['link']}")
    logger.info(f"Criado em: {repo['data_criacao']}, Atualizado em: {repo['data_atualizacao']}\n")


def exibir_dashboard_estatisticas(repositorios: List[Dict[str, Any]]) -> None:
    """Exibe dashboard com estatísticas dos repositórios.
    
    Args:
        repositorios: Lista de repositórios.
    """
    if not repositorios:
        return
    
    # Calcular estatísticas
    total = len(repositorios)
    total_estrelas = sum(r['estrelas'] for r in repositorios)
    total_forks = sum(r['forks'] for r in repositorios)
    media_estrelas = total_estrelas // total if total > 0 else 0
    media_forks = total_forks // total if total > 0 else 0
    
    # Encontrar mais popular
    mais_popular = max(repositorios, key=lambda x: x['estrelas'])
    
    # Encontrar mais recente (por data de criação)
    repos_ordenados = sorted(repositorios, key=lambda x: x['data_criacao'], reverse=True)
    mais_recente = repos_ordenados[0]
    
    # Encontrar mais forks
    mais_forks = max(repositorios, key=lambda x: x['forks'])
    
    # Criar painel de estatísticas
    from rich.columns import Columns
    from rich.panel import Panel
    
    # Estatísticas gerais
    stats_geral = f"""[cyan]📊 Total de Repositórios:[/cyan] [bold white]{total}[/bold white]
[yellow]⭐ Total de Estrelas:[/yellow] [bold white]{total_estrelas:,}[/bold white]
[green]🔀 Total de Forks:[/green] [bold white]{total_forks:,}[/bold white]
[magenta]📈 Média de Estrelas:[/magenta] [bold white]{media_estrelas:,}[/bold white]
[blue]📊 Média de Forks:[/blue] [bold white]{media_forks:,}[/bold white]""".replace(',', '.')
    
    # Destaques
    stats_destaques = f"""[yellow]🏆 Mais Popular:[/yellow]
  [bold cyan]{mais_popular['nome']}[/bold cyan]
  [yellow]{mais_popular['estrelas']:,} ⭐[/yellow]

[green]🔥 Mais Forks:[/green]
  [bold cyan]{mais_forks['nome']}[/bold cyan]
  [green]{mais_forks['forks']:,} 🔀[/green]

[blue]🆕 Mais Recente:[/blue]
  [bold cyan]{mais_recente['nome']}[/bold cyan]
  [blue]{mais_recente['data_criacao'][:10]}[/blue]""".replace(',', '.')
    
    # Criar painéis
    painel_geral = Panel(
        stats_geral,
        title="[bold cyan]📊 ESTATÍSTICAS GERAIS[/bold cyan]",
        border_style="cyan",
        padding=(1, 2)
    )
    
    painel_destaques = Panel(
        stats_destaques,
        title="[bold yellow]🌟 DESTAQUES[/bold yellow]",
        border_style="yellow",
        padding=(1, 2)
    )
    
    # Exibir painéis lado a lado
    console.print()
    console.print(Columns([painel_geral, painel_destaques], equal=True, expand=True))
    console.print()


def exibir_repositorios_tabela(repositorios: List[Dict[str, Any]], titulo: str = "🔍 Repositórios Encontrados", 
                                mostrar_dashboard: bool = True) -> None:
    """Exibe repositórios em uma tabela formatada.
    
    Args:
        repositorios: Lista de repositórios.
        titulo: Título da tabela.
        mostrar_dashboard: Se deve exibir o dashboard de estatísticas.
    """
    if not repositorios:
        console.print("[yellow]⚠️  Nenhum repositório para exibir.[/yellow]")
        return
    
    # Criar tabela
    table = Table(
        title=titulo,
        box=box.ROUNDED,
        show_header=True,
        header_style="bold cyan",
        title_style="bold magenta",
        border_style="blue"
    )
    
    # Adicionar colunas
    table.add_column("Nº", style="dim", width=4, justify="right")
    table.add_column("Nome", style="cyan bold", no_wrap=False, max_width=30)
    table.add_column("⭐ Estrelas", style="yellow", justify="right", width=12)
    table.add_column("🔀 Forks", style="green", justify="right", width=10)
    table.add_column("📅 Atualizado", style="blue", width=12)
    
    # Adicionar linhas
    for idx, repo in enumerate(repositorios, 1):
        # Formatar números com separador de milhares
        estrelas = f"{repo['estrelas']:,}".replace(',', '.')
        forks = f"{repo['forks']:,}".replace(',', '.')
        
        # Pegar apenas a data (sem hora)
        data_atualizacao = repo['data_atualizacao'][:10]
        
        # Cor baseada em estrelas
        if repo['estrelas'] > 50000:
            estrelas_style = "bold yellow"
        elif repo['estrelas'] > 10000:
            estrelas_style = "yellow"
        else:
            estrelas_style = "dim yellow"
        
        table.add_row(
            str(idx),
            repo['nome'],
            f"[{estrelas_style}]{estrelas}[/{estrelas_style}]",
            forks,
            data_atualizacao
        )
    
    # Exibir tabela
    console.print()
    console.print(table)
    
    # Exibir dashboard se solicitado
    if mostrar_dashboard:
        exibir_dashboard_estatisticas(repositorios)

def filtrar_por_data(repositorios: List[Dict[str, Any]], dias: Optional[int] = None) -> List[Dict[str, Any]]:
    """Filtra repositórios criados nos últimos X dias.
    
    Args:
        repositorios (list): Lista de repositórios.
        dias (int): Número de dias para filtrar.
    
    Returns:
        list: Repositórios filtrados.
    """
    if not dias:
        return repositorios
    
    click.echo(f"🔍 Aplicando filtro de data (últimos {dias} dias)...", nl=False)
    
    data_limite = datetime.now() - timedelta(days=dias)
    repositorios_filtrados = []
    
    for repo in repositorios:
        data_criacao = datetime.strptime(repo['data_criacao'], '%Y-%m-%d %H:%M:%S')
        if data_criacao >= data_limite:
            repositorios_filtrados.append(repo)
    
    antes = len(repositorios)
    depois = len(repositorios_filtrados)
    removidos = antes - depois
    
    click.echo(f" ✓")
    click.echo(f"   Antes: {antes} | Depois: {depois} | Removidos: {removidos}")
    
    return repositorios_filtrados

def filtrar_por_estrelas(repositorios: List[Dict[str, Any]], min_estrelas: Optional[int] = None) -> List[Dict[str, Any]]:
    """Filtra repositórios com número mínimo de estrelas.
    
    Args:
        repositorios: Lista de repositórios.
        min_estrelas: Número mínimo de estrelas.
    
    Returns:
        Repositórios filtrados.
    """
    if not min_estrelas:
        return repositorios
    
    click.echo(f"⭐ Aplicando filtro de estrelas (mínimo: {min_estrelas})...", nl=False)
    
    antes = len(repositorios)
    repositorios_filtrados = [repo for repo in repositorios if repo['estrelas'] >= min_estrelas]
    depois = len(repositorios_filtrados)
    removidos = antes - depois
    
    click.echo(f" ✓")
    click.echo(f"   Antes: {antes} | Depois: {depois} | Removidos: {removidos}")
    
    return repositorios_filtrados

def salvar_cache(repositorios: List[Dict[str, Any]], linguagem: str) -> None:
    """Salva os repositórios em cache.
    
    Args:
        repositorios: Lista de repositórios a serem salvos.
        linguagem: Nome da linguagem para identificar o cache.
    """
    cache_file = CACHE_DIR / f"cache_{linguagem}.json"
    with open(cache_file, 'w', encoding='utf-8') as f:
        json.dump({
            'data': datetime.now().isoformat(),
            'repositorios': repositorios
        }, f, ensure_ascii=False, indent=2)
    logger.info(f"Cache salvo em: {cache_file}")

def carregar_cache(linguagem: str) -> Optional[List[Dict[str, Any]]]:
    """Carrega repositórios do cache se existir.
    
    Args:
        linguagem: Nome da linguagem para identificar o cache.
    
    Returns:
        Lista de repositórios do cache ou None se não existir.
    """
    cache_file = CACHE_DIR / f"cache_{linguagem}.json"
    if cache_file.exists():
        with open(cache_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            logger.info(f"Cache carregado de: {cache_file}")
            return data['repositorios']
    return None

def exportar_csv(repositorios: List[Dict[str, Any]], linguagem: str) -> Optional[Path]:
    """Exporta repositórios para arquivo CSV.
    
    Args:
        repositorios: Lista de repositórios.
        linguagem: Nome da linguagem para o arquivo.
    
    Returns:
        Path do arquivo criado ou None se não houver repositórios.
    """
    if not repositorios:
        click.secho("⚠️  Nenhum repositório para exportar.", fg='yellow')
        return
    
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = EXPORT_DIR / f"repos_{linguagem}_{timestamp}.csv"
    
    click.echo()
    click.echo("📄 Exportando para CSV...", nl=False)
    
    with open(filename, 'w', newline='', encoding='utf-8-sig') as f:
        writer = csv.DictWriter(f, fieldnames=['nome', 'estrelas', 'forks', 'link', 'data_criacao', 'data_atualizacao'])
        writer.writeheader()
        
        # Progress bar para escrita
        for repo in tqdm(repositorios, desc="   Escrevendo", unit="repo", 
                        leave=False, bar_format='{l_bar}{bar}| {n_fmt}/{total_fmt}'):
            writer.writerow(repo)
    
    click.echo(" ✓")
    click.secho(f"✅ CSV exportado com sucesso!", fg='green', bold=True)
    click.echo(f"   Arquivo: {filename}")
    click.echo(f"   Repositórios: {len(repositorios)}")
    click.echo(f"   Tamanho: {filename.stat().st_size / 1024:.2f} KB")
    
    return filename

def exportar_json(repositorios: List[Dict[str, Any]], linguagem: str) -> Optional[Path]:
    """Exporta repositórios para arquivo JSON.
    
    Args:
        repositorios: Lista de repositórios.
        linguagem: Nome da linguagem para o arquivo.
    
    Returns:
        Path do arquivo criado ou None se não houver repositórios.
    """
    if not repositorios:
        click.secho("⚠️  Nenhum repositório para exportar.", fg='yellow')
        return
    
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = EXPORT_DIR / f"repos_{linguagem}_{timestamp}.json"
    
    click.echo()
    click.echo("📄 Exportando para JSON...", nl=False)
    
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(repositorios, f, ensure_ascii=False, indent=2)
    
    click.echo(" ✓")
    click.secho(f"✅ JSON exportado com sucesso!", fg='green', bold=True)
    click.echo(f"   Arquivo: {filename}")
    click.echo(f"   Repositórios: {len(repositorios)}")
    click.echo(f"   Tamanho: {filename.stat().st_size / 1024:.2f} KB")
    
    return filename

def coletar_repositorios(config: Dict[str, Any], num_paginas: Optional[int] = None, 
                        usar_cache: bool = False, linguagem: Optional[str] = None) -> List[Dict[str, Any]]:
    """Coleta informações sobre repositórios no GitHub.

    Args:
        config: Configurações específicas para o tipo de repositório.
        num_paginas: Número de páginas a serem consultadas.
        usar_cache: Se deve usar cache existente.
        linguagem: Linguagem para identificar o cache.

    Returns:
        Lista de repositórios coletados.
    """
    # Obtém headers de autenticação
    headers, is_authenticated = get_auth_headers()
    
    # Tenta carregar do cache se solicitado
    if usar_cache and linguagem:
        click.echo("🔍 Verificando cache...", nl=False)
        cached = carregar_cache(linguagem)
        if cached:
            click.echo(f" ✓ Cache encontrado! {len(cached)} repositórios carregados.")
            return cached
        click.echo(" ✗ Cache não encontrado. Buscando na API...")
    
    repositorios = []  # Lista para armazenar os repositórios coletados
    paginas = int(num_paginas) if num_paginas else 1
    
    # Informações iniciais
    click.echo()
    click.secho("📊 Informações da Busca:", fg='cyan', bold=True)
    click.echo(f"   Linguagem: {linguagem or 'N/A'}")
    click.echo(f"   Páginas: {paginas}")
    click.echo(f"   Repositórios esperados: ~{paginas * 30}")
    
    # Mostra status de autenticação
    if is_authenticated:
        click.secho(f"   🔑 Autenticado: Sim (5000 req/hora)", fg='green')
    else:
        click.secho(f"   ⚠️  Autenticado: Não (60 req/hora)", fg='yellow')
    
    click.echo()

    try:
        # Progress bar para coleta de páginas
        with tqdm(total=paginas, desc="🔄 Coletando páginas", 
                  unit="página", colour="green", 
                  bar_format='{l_bar}{bar}| {n_fmt}/{total_fmt} [{elapsed}<{remaining}]') as pbar:
            
            for pagina in range(1, paginas + 1):
                config['query_params']['page'] = str(pagina)
                
                # Atualiza descrição com página atual
                pbar.set_description(f"🔄 Coletando página {pagina}/{paginas}")
                
                try:
                    # Faz a solicitação HTTP com autenticação
                    inicio = time.time()
                    response = requests.get(
                        config['github_api_url'], 
                        params=config['query_params'],
                        headers=headers
                    )
                    tempo_resposta = time.time() - inicio
                    
                    response.raise_for_status()  # Lança uma exceção para erros HTTP

                    # Converte a resposta para formato JSON
                    data = response.json()
                    
                    # Verifica rate limit
                    rate_limit_remaining = response.headers.get('X-RateLimit-Remaining', 'N/A')
                    rate_limit_reset = response.headers.get('X-RateLimit-Reset', 'N/A')
                    rate_limit_limit = response.headers.get('X-RateLimit-Limit', 'N/A')
                    
                    # Itera sobre os repositórios
                    repos_pagina = []
                    for repo in data['items']:
                        nome = repo['name']
                        estrelas = repo['stargazers_count']
                        forks = repo['forks']
                        link = repo['html_url']
                        data_criacao = converter_data(repo['created_at'])
                        data_atualizacao = converter_data(repo['updated_at'])

                        repos_pagina.append({
                            'nome': nome,
                            'estrelas': estrelas,
                            'forks': forks,
                            'link': link,
                            'data_criacao': formatar_data(data_criacao),
                            'data_atualizacao': formatar_data(data_atualizacao)
                        })
                    
                    repositorios.extend(repos_pagina)
                    
                    # Atualiza postfix com informações
                    pbar.set_postfix({
                        'repos': len(repositorios),
                        'tempo': f'{tempo_resposta:.2f}s',
                        'rate_limit': rate_limit_remaining
                    })
                    
                    # Atualiza progress bar
                    pbar.update(1)
                    
                    # Pequeno delay para não sobrecarregar a API
                    if pagina < paginas:
                        time.sleep(0.5)
                
                except requests.exceptions.HTTPError as e:
                    if e.response.status_code == 403:
                        click.echo()
                        click.secho("⚠️  Rate limit atingido!", fg='yellow', bold=True)
                        click.echo(f"   Aguarde até: {datetime.fromtimestamp(int(rate_limit_reset))}")
                        break
                    else:
                        raise
        
        # Resumo final
        click.echo()
        click.secho("✅ Coleta Concluída!", fg='green', bold=True)
        click.echo(f"   Total de repositórios: {len(repositorios)}")
        click.echo(f"   Páginas processadas: {min(pagina, paginas)}/{paginas}")
        
        # Mostra rate limit final
        if rate_limit_remaining != 'N/A':
            click.echo(f"   Requisições restantes: {rate_limit_remaining}")
            if int(rate_limit_remaining) < 10:
                click.secho(f"   ⚠️  Atenção: Poucas requisições restantes!", fg='yellow')
        
        click.echo()

        # Salva no cache
        if linguagem and repositorios:
            click.echo("💾 Salvando no cache...", nl=False)
            salvar_cache(repositorios, linguagem)
            click.echo(" ✓")

    except requests.exceptions.RequestException as e:
        click.echo()
        click.secho(f"❌ Erro ao fazer a solicitação HTTP: {e}", fg='red', bold=True)
        logger.error(f"Erro ao fazer a solicitação HTTP: {e}")

    return repositorios

def menu_interativo() -> None:
    """Menu interativo amigável para o usuário."""
    click.clear()
    click.secho("=" * 60, fg='cyan')
    click.secho("    COLETOR DE REPOSITÓRIOS DO GITHUB", fg='cyan', bold=True)
    click.secho("=" * 60, fg='cyan')
    click.echo()
    
    # Passo 1: Linguagem
    click.secho("📌 Passo 1: Escolha a linguagem", fg='yellow', bold=True)
    linguagem = click.prompt('   Digite a linguagem (ex: Python, JavaScript, Java)', type=str)
    click.echo()
    
    # Passo 2: Ordenação
    click.secho("📌 Passo 2: Como ordenar os resultados?", fg='yellow', bold=True)
    click.echo("   1. Por estrelas (mais populares)")
    click.echo("   2. Por forks (mais copiados)")
    click.echo("   3. Por atualização (mais recentes)")
    ordenacao_opcao = click.prompt('   Escolha', type=click.IntRange(1, 3), default=1)
    ordenacao_map = {1: 'stars', 2: 'forks', 3: 'updated'}
    ordenacao = ordenacao_map[ordenacao_opcao]
    click.echo()
    
    # Passo 3: Número de páginas
    click.secho("📌 Passo 3: Quantas páginas buscar?", fg='yellow', bold=True)
    click.echo("   (Cada página tem ~30 repositórios)")
    num_paginas = click.prompt('   Número de páginas', type=int, default=1)
    click.echo()
    
    # Passo 4: Filtros
    click.secho("📌 Passo 4: Aplicar filtros? (opcional)", fg='yellow', bold=True)
    aplicar_filtros = click.confirm('   Deseja aplicar filtros avançados?', default=False)
    
    dias_filtro = None
    min_estrelas = None
    
    if aplicar_filtros:
        click.echo()
        click.secho("   Filtro por data:", fg='green')
        if click.confirm('   Filtrar por repositórios recentes?', default=False):
            dias_filtro = click.prompt('   Criados nos últimos X dias', type=int, default=7)
        
        click.echo()
        click.secho("   Filtro por popularidade:", fg='green')
        if click.confirm('   Filtrar por número mínimo de estrelas?', default=False):
            min_estrelas = click.prompt('   Mínimo de estrelas', type=int, default=100)
    
    click.echo()
    
    # Passo 5: Cache
    click.secho("📌 Passo 5: Usar cache?", fg='yellow', bold=True)
    usar_cache = click.confirm('   Usar dados em cache (se disponível)?', default=True)
    click.echo()
    
    # Passo 6: Exportação
    click.secho("📌 Passo 6: Exportar resultados?", fg='yellow', bold=True)
    click.echo("   1. Apenas exibir no console")
    click.echo("   2. Exportar para CSV (Excel)")
    click.echo("   3. Exportar para JSON")
    click.echo("   4. Exportar para ambos (CSV + JSON)")
    exportar_opcao = click.prompt('   Escolha', type=click.IntRange(1, 4), default=1)
    click.echo()
    
    # Processamento
    click.secho("🔄 Coletando repositórios...", fg='cyan', bold=True)
    click.echo()
    
    config = {
        'github_api_url': 'https://api.github.com/search/repositories',
        'query_params': {
            'q': f'language:{linguagem}',
            'sort': ordenacao,
            'page': '1'
        }
    }
    
    # Coleta os repositórios
    repositorios = coletar_repositorios(config, num_paginas, usar_cache, linguagem)
    
    # Aplica filtros
    if dias_filtro:
        antes = len(repositorios)
        repositorios = filtrar_por_data(repositorios, dias_filtro)
        logger.info(f"Filtro de data aplicado: {antes} → {len(repositorios)} repositórios")
    
    if min_estrelas:
        antes = len(repositorios)
        repositorios = filtrar_por_estrelas(repositorios, min_estrelas)
        logger.info(f"Filtro de estrelas aplicado: {antes} → {len(repositorios)} repositórios")
    
    click.echo()
    click.secho(f"✓ Total de repositórios encontrados: {len(repositorios)}", fg='green', bold=True)
    click.echo()
    
    # Exibe repositórios em tabela formatada
    if repositorios:
        # Mostrar apenas os primeiros 20 no modo interativo
        repos_exibir = repositorios[:20]
        exibir_repositorios_tabela(repos_exibir, f"🔍 Top {len(repos_exibir)} Repositórios {linguagem}")
        
        if len(repositorios) > 20:
            console.print(f"[yellow]... e mais {len(repositorios) - 20} repositórios[/yellow]")
            console.print()
    
    # Exportação
    if exportar_opcao in [2, 4]:
        exportar_csv(repositorios, linguagem)
    
    if exportar_opcao in [3, 4]:
        exportar_json(repositorios, linguagem)
    
    click.echo()
    click.secho("=" * 60, fg='cyan')
    click.secho("✓ Processo concluído!", fg='green', bold=True)
    click.secho("=" * 60, fg='cyan')

@click.group(invoke_without_command=True)
@click.pass_context
def cli(ctx):
    """Coletor de Repositórios do GitHub - Versão Melhorada"""
    if ctx.invoked_subcommand is None:
        # Se nenhum subcomando, executa o comportamento padrão
        ctx.invoke(search)


@cli.command()
@click.option('--interativo', '-i', is_flag=True, help='Modo interativo com menu amigável')
@click.option(
    '--tipo-repositorio',
    type=click.Choice(['linguagem', 'IA', 'machine_learning', 'back_end', 'front_end', 'outros'], case_sensitive=False),
    help='O tipo de repositório no GitHub.'
)
@click.option(
    '--ordenacao',
    type=click.Choice(['stars', 'forks', 'updated'], case_sensitive=False),
    help='O critério de ordenação dos repositórios.'
)
@click.option(
    '--linguagem',
    type=str,
    help='A linguagem de programação desejada.'
)
@click.option(
    '--num-paginas',
    type=int,
    help='Número de páginas a serem consultadas.'
)
@click.option(
    '--dias',
    type=int,
    help='Filtrar repositórios criados nos últimos X dias.'
)
@click.option(
    '--min-estrelas',
    type=int,
    help='Número mínimo de estrelas.'
)
@click.option(
    '--exportar',
    type=click.Choice(['csv', 'json', 'ambos'], case_sensitive=False),
    help='Formato de exportação dos dados.'
)
@click.option(
    '--usar-cache',
    is_flag=True,
    help='Usar dados em cache se disponível.'
)
def search(interativo, tipo_repositorio, ordenacao, linguagem, num_paginas, dias, min_estrelas, exportar, usar_cache):
    """Buscar repositórios do GitHub"""
    
    # Se modo interativo ou nenhum parâmetro fornecido, usa o menu
    if interativo or not linguagem:
        menu_interativo()
        return
    
    try:
        # Modo linha de comando (original)
        config = {
            'github_api_url': 'https://api.github.com/search/repositories',
            'query_params': {
                'q': f'language:{linguagem}',
                'sort': ordenacao or 'stars',
                'page': '1'
            }
        }

        # Coleta os repositórios
        repositorios = coletar_repositorios(config, num_paginas, usar_cache, linguagem)
        
        # Aplica filtros
        if dias:
            repositorios = filtrar_por_data(repositorios, dias)
        
        if min_estrelas:
            repositorios = filtrar_por_estrelas(repositorios, min_estrelas)

        # Exibe repositórios em tabela formatada
        if repositorios:
            exibir_repositorios_tabela(repositorios, f"🔍 Repositórios {linguagem}")
        else:
            console.print("[yellow]⚠️  Nenhum repositório encontrado com os filtros aplicados.[/yellow]")
        
        # Exporta se solicitado
        if exportar in ['csv', 'ambos']:
            exportar_csv(repositorios, linguagem)
        
        if exportar in ['json', 'ambos']:
            exportar_json(repositorios, linguagem)

    except click.Abort:
        logger.info("Operação abortada pelo usuário.")
    except Exception as e:
        logger.error(f"Erro inesperado: {e}")


@cli.group()
def config():
    """Gerenciar configurações do GitHub Repos Collector"""
    pass


@config.command('set-token')
@click.argument('token')
def set_token(token):
    """Configurar token do GitHub
    
    Exemplo: python app.py config set-token ghp_xxxxxxxxxxxx
    """
    if not token.startswith('ghp_') and not token.startswith('github_pat_'):
        click.secho("⚠️  Aviso: O token não parece ser um token válido do GitHub", fg='yellow')
        if not click.confirm('Deseja continuar mesmo assim?'):
            return
    
    save_github_token(token)
    click.secho("✅ Token configurado com sucesso!", fg='green', bold=True)
    click.echo(f"   Arquivo: {CONFIG_FILE}")
    click.echo()
    click.echo("💡 O token foi salvo de forma segura.")
    click.echo("   Agora você tem 5000 requisições/hora!")


@config.command('show-token')
def show_token_cmd():
    """Mostrar token configurado (mascarado)"""
    token = get_github_token()
    
    if token:
        masked = f"{token[:4]}...{token[-4:]}" if len(token) > 8 else "****"
        click.secho("🔑 Token Configurado:", fg='green', bold=True)
        click.echo(f"   Token: {masked}")
        click.echo(f"   Arquivo: {CONFIG_FILE}")
    else:
        click.secho("⚠️  Nenhum token configurado", fg='yellow', bold=True)
        click.echo()
        click.echo("Configure um token com:")
        click.echo("   python app.py config set-token SEU_TOKEN")


@config.command('remove-token')
def remove_token():
    """Remover token configurado"""
    if not CONFIG_FILE.exists():
        click.secho("⚠️  Nenhum token configurado", fg='yellow')
        return
    
    if click.confirm('Tem certeza que deseja remover o token?'):
        try:
            config_data = {}
            with open(CONFIG_FILE, 'r') as f:
                config_data = json.load(f)
            
            if 'github_token' in config_data:
                del config_data['github_token']
                
                if config_data:
                    with open(CONFIG_FILE, 'w') as f:
                        json.dump(config_data, f, indent=2)
                else:
                    CONFIG_FILE.unlink()
                
                click.secho("✅ Token removido com sucesso!", fg='green', bold=True)
            else:
                click.secho("⚠️  Nenhum token encontrado", fg='yellow')
        except Exception as e:
            click.secho(f"❌ Erro ao remover token: {e}", fg='red')


@config.command('status')
def status():
    """Mostrar status de autenticação"""
    show_auth_status()


@cli.command()
def auth_status():
    """Verificar status de autenticação"""
    show_auth_status()


if __name__ == '__main__':
    cli()
