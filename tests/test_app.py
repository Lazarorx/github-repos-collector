"""
Testes para o GitHub Repos Collector
"""
import pytest
from datetime import datetime, timedelta
import json
import os
from pathlib import Path
import sys

# Adiciona o diretório raiz ao path
sys.path.insert(0, str(Path(__file__).parent.parent))

from app import (
    converter_data,
    formatar_data,
    filtrar_por_data,
    filtrar_por_estrelas,
    salvar_cache,
    carregar_cache,
    CACHE_DIR,
    EXPORT_DIR
)


class TestConverterData:
    """Testes para a função converter_data"""
    
    def test_converter_data_valida(self):
        """Testa conversão de data válida"""
        data_str = "2024-01-15T10:30:00Z"
        resultado = converter_data(data_str)
        assert isinstance(resultado, datetime)
        assert resultado.year == 2024
        assert resultado.month == 1
        assert resultado.day == 15
    
    def test_converter_data_formato_correto(self):
        """Testa se a data convertida tem os valores corretos"""
        data_str = "2023-12-25T23:59:59Z"
        resultado = converter_data(data_str)
        assert resultado.hour == 23
        assert resultado.minute == 59
        assert resultado.second == 59


class TestFormatarData:
    """Testes para a função formatar_data"""
    
    def test_formatar_data_formato_correto(self):
        """Testa se a data é formatada corretamente"""
        data = datetime(2024, 1, 15, 10, 30, 45)
        resultado = formatar_data(data)
        assert resultado == "2024-01-15 10:30:45"
    
    def test_formatar_data_com_zeros(self):
        """Testa formatação com zeros à esquerda"""
        data = datetime(2024, 1, 5, 9, 5, 3)
        resultado = formatar_data(data)
        assert resultado == "2024-01-05 09:05:03"


class TestFiltrarPorData:
    """Testes para a função filtrar_por_data"""
    
    def test_filtrar_sem_dias(self):
        """Testa que retorna todos os repos quando dias=None"""
        repos = [
            {'nome': 'repo1', 'data_criacao': '2024-01-01 10:00:00'},
            {'nome': 'repo2', 'data_criacao': '2023-01-01 10:00:00'}
        ]
        resultado = filtrar_por_data(repos, None)
        assert len(resultado) == 2
    
    def test_filtrar_com_dias(self):
        """Testa filtragem por dias"""
        hoje = datetime.now()
        ontem = hoje - timedelta(days=1)
        mes_passado = hoje - timedelta(days=40)
        
        repos = [
            {'nome': 'repo_recente', 'data_criacao': formatar_data(ontem)},
            {'nome': 'repo_antigo', 'data_criacao': formatar_data(mes_passado)}
        ]
        
        resultado = filtrar_por_data(repos, dias=7)
        assert len(resultado) == 1
        assert resultado[0]['nome'] == 'repo_recente'
    
    def test_filtrar_lista_vazia(self):
        """Testa filtragem de lista vazia"""
        resultado = filtrar_por_data([], dias=7)
        assert len(resultado) == 0


class TestFiltrarPorEstrelas:
    """Testes para a função filtrar_por_estrelas"""
    
    def test_filtrar_sem_minimo(self):
        """Testa que retorna todos os repos quando min_estrelas=None"""
        repos = [
            {'nome': 'repo1', 'estrelas': 100},
            {'nome': 'repo2', 'estrelas': 10}
        ]
        resultado = filtrar_por_estrelas(repos, None)
        assert len(resultado) == 2
    
    def test_filtrar_com_minimo(self):
        """Testa filtragem por número mínimo de estrelas"""
        repos = [
            {'nome': 'repo_popular', 'estrelas': 1000},
            {'nome': 'repo_medio', 'estrelas': 500},
            {'nome': 'repo_pequeno', 'estrelas': 50}
        ]
        
        resultado = filtrar_por_estrelas(repos, min_estrelas=100)
        assert len(resultado) == 2
        assert all(r['estrelas'] >= 100 for r in resultado)
    
    def test_filtrar_nenhum_atende(self):
        """Testa quando nenhum repo atende o critério"""
        repos = [
            {'nome': 'repo1', 'estrelas': 10},
            {'nome': 'repo2', 'estrelas': 20}
        ]
        resultado = filtrar_por_estrelas(repos, min_estrelas=100)
        assert len(resultado) == 0
    
    def test_filtrar_lista_vazia(self):
        """Testa filtragem de lista vazia"""
        resultado = filtrar_por_estrelas([], min_estrelas=100)
        assert len(resultado) == 0


class TestCache:
    """Testes para as funções de cache"""
    
    @pytest.fixture
    def repos_exemplo(self):
        """Fixture com repositórios de exemplo"""
        return [
            {
                'nome': 'test-repo',
                'estrelas': 100,
                'forks': 50,
                'link': 'https://github.com/test/repo',
                'data_criacao': '2024-01-01 10:00:00',
                'data_atualizacao': '2024-01-15 10:00:00'
            }
        ]
    
    def test_salvar_e_carregar_cache(self, repos_exemplo, tmp_path):
        """Testa salvar e carregar cache"""
        # Usa diretório temporário
        import app
        app.CACHE_DIR = tmp_path
        
        linguagem = "TestLang"
        salvar_cache(repos_exemplo, linguagem)
        
        # Verifica se o arquivo foi criado
        cache_file = tmp_path / f"cache_{linguagem}.json"
        assert cache_file.exists()
        
        # Carrega o cache
        resultado = carregar_cache(linguagem)
        assert resultado == repos_exemplo
    
    def test_carregar_cache_inexistente(self, tmp_path):
        """Testa carregar cache que não existe"""
        import app
        app.CACHE_DIR = tmp_path
        
        resultado = carregar_cache("LinguagemInexistente")
        assert resultado is None
    
    def test_cache_contem_data(self, repos_exemplo, tmp_path):
        """Testa se o cache salva a data"""
        import app
        app.CACHE_DIR = tmp_path
        
        linguagem = "TestLang"
        salvar_cache(repos_exemplo, linguagem)
        
        cache_file = tmp_path / f"cache_{linguagem}.json"
        with open(cache_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        assert 'data' in data
        assert 'repositorios' in data
        assert data['repositorios'] == repos_exemplo


class TestDiretorios:
    """Testes para criação de diretórios"""
    
    def test_diretorios_existem(self):
        """Testa se os diretórios necessários existem"""
        assert CACHE_DIR.exists()
        assert EXPORT_DIR.exists()
    
    def test_diretorios_sao_path(self):
        """Testa se os diretórios são objetos Path"""
        assert isinstance(CACHE_DIR, Path)
        assert isinstance(EXPORT_DIR, Path)


class TestIntegracaoFiltros:
    """Testes de integração para múltiplos filtros"""
    
    def test_filtros_combinados(self):
        """Testa aplicação de múltiplos filtros"""
        hoje = datetime.now()
        ontem = hoje - timedelta(days=1)
        mes_passado = hoje - timedelta(days=40)
        
        repos = [
            {
                'nome': 'repo_perfeito',
                'estrelas': 1000,
                'data_criacao': formatar_data(ontem)
            },
            {
                'nome': 'repo_poucas_estrelas',
                'estrelas': 50,
                'data_criacao': formatar_data(ontem)
            },
            {
                'nome': 'repo_antigo',
                'estrelas': 1000,
                'data_criacao': formatar_data(mes_passado)
            }
        ]
        
        # Aplica filtro de data
        resultado = filtrar_por_data(repos, dias=7)
        # Aplica filtro de estrelas
        resultado = filtrar_por_estrelas(resultado, min_estrelas=100)
        
        assert len(resultado) == 1
        assert resultado[0]['nome'] == 'repo_perfeito'


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
