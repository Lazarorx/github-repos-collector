# 🧪 Guia de Testes

Este documento explica como executar e escrever testes para o GitHub Repos Collector.

## 📋 Visão Geral

O projeto usa **pytest** para testes automatizados, com cobertura de código medida pelo **pytest-cov**.

### Estatísticas Atuais

- ✅ **17 testes** implementados
- ✅ **100% dos testes** passando
- 📊 **29% de cobertura** de código (em crescimento)

## 🚀 Executando Testes

### Instalação

```bash
# Instalar dependências de teste
pip install -r requirements.txt
```

### Comandos Básicos

```bash
# Executar todos os testes
pytest

# Executar com saída detalhada
pytest -v

# Executar testes específicos
pytest tests/test_app.py

# Executar uma classe de testes
pytest tests/test_app.py::TestConverterData

# Executar um teste específico
pytest tests/test_app.py::TestConverterData::test_converter_data_valida
```

### Testes com Cobertura

```bash
# Executar com relatório de cobertura
pytest --cov=app

# Gerar relatório HTML
pytest --cov=app --cov-report=html

# Abrir relatório no navegador
# Windows
start htmlcov/index.html

# Linux/Mac
open htmlcov/index.html
```

## 📊 Estrutura dos Testes

```
tests/
├── __init__.py
└── test_app.py          # Testes principais
```

### Testes Implementados

#### 1. TestConverterData
Testa a conversão de strings de data para objetos datetime.

```python
def test_converter_data_valida():
    """Testa conversão de data válida"""
    data_str = "2024-01-15T10:30:00Z"
    resultado = converter_data(data_str)
    assert isinstance(resultado, datetime)
```

#### 2. TestFormatarData
Testa a formatação de datas para strings legíveis.

```python
def test_formatar_data_formato_correto():
    """Testa se a data é formatada corretamente"""
    data = datetime(2024, 1, 15, 10, 30, 45)
    resultado = formatar_data(data)
    assert resultado == "2024-01-15 10:30:45"
```

#### 3. TestFiltrarPorData
Testa o filtro de repositórios por data de criação.

```python
def test_filtrar_com_dias():
    """Testa filtragem por dias"""
    # Testa que apenas repos recentes são retornados
```

#### 4. TestFiltrarPorEstrelas
Testa o filtro de repositórios por número de estrelas.

```python
def test_filtrar_com_minimo():
    """Testa filtragem por número mínimo de estrelas"""
    # Testa que apenas repos com estrelas suficientes são retornados
```

#### 5. TestCache
Testa o sistema de cache (salvar e carregar).

```python
def test_salvar_e_carregar_cache():
    """Testa salvar e carregar cache"""
    # Testa o ciclo completo de cache
```

#### 6. TestDiretorios
Testa a criação automática de diretórios.

```python
def test_diretorios_existem():
    """Testa se os diretórios necessários existem"""
```

#### 7. TestIntegracaoFiltros
Testa a combinação de múltiplos filtros.

```python
def test_filtros_combinados():
    """Testa aplicação de múltiplos filtros"""
    # Testa filtro de data + filtro de estrelas
```

## ✍️ Escrevendo Novos Testes

### Estrutura Básica

```python
class TestMinhaFuncionalidade:
    """Testes para minha funcionalidade"""
    
    def test_caso_basico(self):
        """Testa o caso básico"""
        # Arrange (preparar)
        entrada = "valor"
        
        # Act (executar)
        resultado = minha_funcao(entrada)
        
        # Assert (verificar)
        assert resultado == "esperado"
    
    def test_caso_erro(self):
        """Testa tratamento de erro"""
        with pytest.raises(ValueError):
            minha_funcao(None)
```

### Usando Fixtures

```python
@pytest.fixture
def repos_exemplo():
    """Fixture com repositórios de exemplo"""
    return [
        {
            'nome': 'test-repo',
            'estrelas': 100,
            'forks': 50
        }
    ]

def test_com_fixture(repos_exemplo):
    """Usa a fixture"""
    assert len(repos_exemplo) == 1
```

### Testando com Arquivos Temporários

```python
def test_salvar_arquivo(tmp_path):
    """Testa salvamento de arquivo"""
    arquivo = tmp_path / "test.json"
    salvar_dados(arquivo, {"teste": "valor"})
    assert arquivo.exists()
```

## 🎯 Boas Práticas

### 1. Nomes Descritivos
```python
# ❌ Ruim
def test_1():
    pass

# ✅ Bom
def test_filtrar_por_estrelas_retorna_apenas_repos_populares():
    pass
```

### 2. Um Conceito por Teste
```python
# ❌ Ruim - testa múltiplas coisas
def test_tudo():
    assert funcao1() == "ok"
    assert funcao2() == "ok"
    assert funcao3() == "ok"

# ✅ Bom - um teste por conceito
def test_funcao1_retorna_ok():
    assert funcao1() == "ok"

def test_funcao2_retorna_ok():
    assert funcao2() == "ok"
```

### 3. Arrange-Act-Assert
```python
def test_exemplo():
    # Arrange - preparar dados
    repos = [{'estrelas': 100}]
    
    # Act - executar função
    resultado = filtrar_por_estrelas(repos, 50)
    
    # Assert - verificar resultado
    assert len(resultado) == 1
```

### 4. Testes Independentes
```python
# ❌ Ruim - depende de ordem
repos_global = []

def test_adicionar():
    repos_global.append({'nome': 'test'})

def test_contar():
    assert len(repos_global) == 1  # Falha se executado sozinho

# ✅ Bom - independente
def test_adicionar():
    repos = []
    repos.append({'nome': 'test'})
    assert len(repos) == 1
```

## 🔍 Debugging de Testes

### Mostrar Prints
```bash
# Mostrar prints durante os testes
pytest -s

# Mostrar prints apenas de testes que falharam
pytest --tb=short
```

### Parar no Primeiro Erro
```bash
pytest -x
```

### Executar Último Teste que Falhou
```bash
pytest --lf
```

### Modo Verbose
```bash
pytest -vv
```

## 📈 Aumentando a Cobertura

### Ver Linhas Não Cobertas
```bash
pytest --cov=app --cov-report=term-missing
```

### Focar em Arquivo Específico
```bash
pytest --cov=app --cov-report=term-missing tests/test_app.py
```

### Meta de Cobertura
```bash
# Falhar se cobertura < 80%
pytest --cov=app --cov-fail-under=80
```

## 🚨 Testes de Integração

Para testar a API do GitHub (cuidado com rate limits):

```python
@pytest.mark.integration
def test_buscar_repos_reais():
    """Testa busca real na API do GitHub"""
    config = {
        'github_api_url': 'https://api.github.com/search/repositories',
        'query_params': {'q': 'language:Python', 'sort': 'stars'}
    }
    repos = coletar_repositorios(config, num_paginas=1)
    assert len(repos) > 0
```

Executar apenas testes de integração:
```bash
pytest -m integration
```

Pular testes de integração:
```bash
pytest -m "not integration"
```

## 🔄 CI/CD

Os testes são executados automaticamente no GitHub Actions:

- ✅ A cada push
- ✅ A cada pull request
- ✅ Em múltiplos sistemas operacionais (Windows, Linux, macOS)
- ✅ Em múltiplas versões do Python (3.7 - 3.11)

Ver resultados: [GitHub Actions](https://github.com/yourusername/github-repos-collector/actions)

## 📝 Checklist para PRs

Antes de submeter um Pull Request:

- [ ] Todos os testes passam localmente
- [ ] Novos recursos têm testes
- [ ] Cobertura não diminuiu
- [ ] Testes são independentes
- [ ] Nomes de testes são descritivos
- [ ] Código segue o estilo do projeto

## 🆘 Problemas Comuns

### Testes Falhando Localmente

```bash
# Limpar cache
pytest --cache-clear

# Reinstalar dependências
pip install -r requirements.txt --force-reinstall
```

### Import Errors

```bash
# Adicionar diretório ao PYTHONPATH
export PYTHONPATH="${PYTHONPATH}:$(pwd)"  # Linux/Mac
set PYTHONPATH=%PYTHONPATH%;%CD%          # Windows
```

### Testes Lentos

```bash
# Executar em paralelo (requer pytest-xdist)
pip install pytest-xdist
pytest -n auto
```

## 📚 Recursos

- [Pytest Documentation](https://docs.pytest.org/)
- [Pytest-cov Documentation](https://pytest-cov.readthedocs.io/)
- [Testing Best Practices](https://docs.python-guide.org/writing/tests/)

## 🎯 Próximos Passos

Para melhorar a cobertura de testes:

1. Adicionar testes para `exportar_csv()`
2. Adicionar testes para `exportar_json()`
3. Adicionar testes para `coletar_repositorios()`
4. Adicionar testes para `menu_interativo()`
5. Adicionar testes de integração com API real
6. Adicionar testes de performance

---

**Contribua com testes! Cada teste torna o projeto mais robusto.** 🧪
