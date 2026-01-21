# 🛠️ Comandos Úteis

Referência rápida de comandos para desenvolvimento e manutenção do projeto.

## 🧪 Testes

```bash
# Executar todos os testes
pytest

# Testes com saída detalhada
pytest -v

# Testes com cobertura
pytest --cov=app

# Cobertura com relatório HTML
pytest --cov=app --cov-report=html

# Abrir relatório de cobertura
# Windows
start htmlcov/index.html
# Linux/Mac
open htmlcov/index.html

# Executar teste específico
pytest tests/test_app.py::TestConverterData::test_converter_data_valida

# Parar no primeiro erro
pytest -x

# Mostrar prints
pytest -s

# Executar apenas testes rápidos
pytest -m "not slow"
```

## 🎨 Qualidade de Código

```bash
# Formatar código com black
black app.py tests/

# Verificar formatação
black --check app.py tests/

# Lint com flake8
flake8 app.py

# Lint com detalhes
flake8 app.py --show-source --statistics

# Ordenar imports
isort app.py tests/

# Verificar ordenação
isort --check-only app.py tests/

# Type checking com mypy
mypy app.py

# Executar todos os checks
black app.py tests/ && isort app.py tests/ && flake8 app.py && mypy app.py
```

## 📦 Instalação e Build

```bash
# Instalar em modo desenvolvimento
pip install -e .

# Instalar com dependências de dev
pip install -e ".[dev]"

# Instalar apenas dependências
pip install -r requirements.txt

# Atualizar dependências
pip install --upgrade -r requirements.txt

# Build do pacote
python setup.py sdist bdist_wheel

# Verificar build
twine check dist/*

# Upload para PyPI (teste)
twine upload --repository testpypi dist/*

# Upload para PyPI (produção)
twine upload dist/*
```

## 🚀 Execução

```bash
# Modo interativo
python app.py

# Com parâmetros
python app.py --linguagem=Python --exportar=csv

# Usando comando instalado
github-repos-collector --linguagem=Python

# Comando curto
grc --linguagem=Python

# Ajuda
python app.py --help
```

## 🔍 Git

```bash
# Status
git status

# Adicionar arquivos
git add .

# Commit
git commit -m "Mensagem do commit"

# Push
git push origin main

# Pull
git pull origin main

# Criar branch
git checkout -b feature/nova-feature

# Mudar de branch
git checkout main

# Merge
git merge feature/nova-feature

# Ver histórico
git log --oneline

# Ver diferenças
git diff

# Desfazer mudanças
git checkout -- arquivo.py

# Criar tag
git tag -a v2.0.0 -m "Release v2.0.0"

# Push tag
git push origin v2.0.0

# Listar tags
git tag -l
```

## 📊 Análise

```bash
# Contar linhas de código
# Windows (PowerShell)
(Get-Content app.py).Count

# Linux/Mac
wc -l app.py

# Contar linhas de todos os arquivos Python
# Linux/Mac
find . -name "*.py" | xargs wc -l

# Ver tamanho dos arquivos
# Windows
dir
# Linux/Mac
ls -lh

# Buscar no código
# Windows
findstr /s /i "função" *.py
# Linux/Mac
grep -r "função" *.py
```

## 🧹 Limpeza

```bash
# Limpar cache Python
# Windows
del /s /q __pycache__
del /s /q *.pyc
# Linux/Mac
find . -type d -name __pycache__ -exec rm -rf {} +
find . -type f -name "*.pyc" -delete

# Limpar cache pytest
rm -rf .pytest_cache

# Limpar cobertura
rm -rf htmlcov .coverage coverage.xml

# Limpar build
rm -rf build dist *.egg-info

# Limpar tudo
# Windows
rmdir /s /q __pycache__ .pytest_cache htmlcov build dist
# Linux/Mac
rm -rf __pycache__ .pytest_cache htmlcov build dist *.egg-info
```

## 📝 Documentação

```bash
# Gerar documentação com Sphinx (futuro)
sphinx-build -b html docs/ docs/_build

# Servir documentação localmente
python -m http.server 8000 -d docs/

# Verificar links quebrados
# Requer linkchecker
linkchecker docs/
```

## 🔐 Segurança

```bash
# Verificar vulnerabilidades
pip-audit

# Verificar dependências desatualizadas
pip list --outdated

# Atualizar pip
python -m pip install --upgrade pip

# Verificar secrets no código
# Requer truffleHog
trufflehog filesystem .
```

## 📈 Métricas

```bash
# Complexidade ciclomática
radon cc app.py -a

# Índice de manutenibilidade
radon mi app.py

# Métricas raw
radon raw app.py

# Todas as métricas
radon cc app.py && radon mi app.py && radon raw app.py
```

## 🐳 Docker (Futuro)

```bash
# Build
docker build -t github-repos-collector .

# Run
docker run -it github-repos-collector

# Run com volume
docker run -it -v $(pwd)/exports:/app/exports github-repos-collector

# Docker Compose
docker-compose up
```

## 🔄 CI/CD

```bash
# Simular GitHub Actions localmente (requer act)
act

# Executar workflow específico
act -j test

# Listar workflows
act -l
```

## 📦 Dependências

```bash
# Listar dependências instaladas
pip list

# Listar dependências do projeto
pip freeze

# Gerar requirements.txt
pip freeze > requirements.txt

# Verificar dependências não usadas
pip-autoremove

# Atualizar todas as dependências
pip list --outdated --format=freeze | grep -v '^\-e' | cut -d = -f 1 | xargs -n1 pip install -U
```

## 🎯 Atalhos Úteis

```bash
# Alias úteis (adicione ao .bashrc ou .zshrc)
alias grc-test="pytest -v"
alias grc-cov="pytest --cov=app --cov-report=html"
alias grc-lint="flake8 app.py && black --check app.py"
alias grc-format="black app.py tests/ && isort app.py tests/"
alias grc-clean="rm -rf __pycache__ .pytest_cache htmlcov"
alias grc-run="python app.py"
```

## 🚀 Workflow Completo

```bash
# Workflow de desenvolvimento completo
git checkout -b feature/nova-feature  # Criar branch
# ... fazer mudanças ...
black app.py tests/                   # Formatar
isort app.py tests/                   # Ordenar imports
flake8 app.py                         # Lint
pytest -v                             # Testar
git add .                             # Adicionar
git commit -m "Add nova feature"      # Commit
git push origin feature/nova-feature  # Push
# ... criar PR no GitHub ...
```

## 📋 Checklist Pré-Commit

```bash
# Execute antes de cada commit
black app.py tests/           # ✅ Formatar
isort app.py tests/           # ✅ Ordenar imports
flake8 app.py                 # ✅ Lint
mypy app.py                   # ✅ Type check
pytest -v                     # ✅ Testes
git status                    # ✅ Verificar arquivos
```

## 🎓 Comandos de Aprendizado

```bash
# Ver ajuda do pytest
pytest --help

# Ver ajuda do black
black --help

# Ver ajuda do flake8
flake8 --help

# Ver versões
python --version
pip --version
pytest --version
black --version
```

## 💡 Dicas

### Windows PowerShell

```powershell
# Executar múltiplos comandos
black app.py; isort app.py; pytest

# Criar alias
Set-Alias grc python app.py
```

### Linux/Mac Bash

```bash
# Executar múltiplos comandos
black app.py && isort app.py && pytest

# Criar função
grc-all() {
    black app.py tests/ &&
    isort app.py tests/ &&
    flake8 app.py &&
    pytest -v
}
```

## 🔧 Troubleshooting

```bash
# Reinstalar dependências
pip uninstall -r requirements.txt -y
pip install -r requirements.txt

# Limpar cache pip
pip cache purge

# Verificar instalação
pip show github-repos-collector

# Verificar PATH
echo $PATH  # Linux/Mac
echo %PATH%  # Windows

# Verificar Python
which python  # Linux/Mac
where python  # Windows
```

## 📚 Recursos

- [pytest docs](https://docs.pytest.org/)
- [black docs](https://black.readthedocs.io/)
- [flake8 docs](https://flake8.pycqa.org/)
- [mypy docs](https://mypy.readthedocs.io/)
- [pip docs](https://pip.pypa.io/)
- [git docs](https://git-scm.com/doc)

---

**Dica:** Salve este arquivo nos favoritos para referência rápida!
