# 📦 Guia de Instalação

Este guia cobre todas as formas de instalar o GitHub Repos Collector.

## 🚀 Instalação Rápida

### Opção 1: Via pip (Recomendado)

```bash
pip install github-repos-collector
```

Após a instalação, você pode usar:
```bash
# Comando completo
github-repos-collector

# Ou comando curto
grc
```

### Opção 2: Via Git Clone

```bash
# Clone o repositório
git clone https://github.com/yourusername/github-repos-collector.git
cd github-repos-collector

# Instale as dependências
pip install -r requirements.txt

# Execute
python app.py
```

### Opção 3: Windows (Scripts Automáticos)

1. Baixe o projeto
2. Clique duplo em `instalar.bat` (instala dependências)
3. Clique duplo em `iniciar.bat` (inicia o programa)

## 🔧 Instalação para Desenvolvimento

Se você quer contribuir ou modificar o código:

```bash
# Clone o repositório
git clone https://github.com/yourusername/github-repos-collector.git
cd github-repos-collector

# Crie um ambiente virtual (recomendado)
python -m venv venv

# Ative o ambiente virtual
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Instale em modo desenvolvimento
pip install -e .

# Instale dependências de desenvolvimento
pip install -e ".[dev]"
```

Isso instala o pacote em modo "editável", permitindo que você modifique o código e veja as mudanças imediatamente.

## 📋 Requisitos

### Requisitos Mínimos

- **Python**: 3.7 ou superior
- **Sistema Operacional**: Windows, Linux, ou macOS
- **Espaço em disco**: ~10 MB
- **Conexão com internet**: Necessária para acessar a API do GitHub

### Dependências

O projeto usa apenas duas dependências principais:

```
requests>=2.31.0  # Para fazer requisições HTTP
click>=8.1.7      # Para interface de linha de comando
```

### Dependências de Desenvolvimento (Opcional)

```
pytest>=7.4.0         # Framework de testes
pytest-cov>=4.1.0     # Cobertura de código
black>=23.0.0         # Formatação de código
flake8>=6.0.0         # Linting
isort>=5.12.0         # Ordenação de imports
mypy>=1.0.0           # Verificação de tipos
```

## 🐍 Verificando a Instalação do Python

### Windows

```cmd
python --version
```

Se não estiver instalado, baixe em: https://www.python.org/downloads/

### Linux

```bash
python3 --version
```

Se não estiver instalado:
```bash
# Ubuntu/Debian
sudo apt-get update
sudo apt-get install python3 python3-pip

# Fedora
sudo dnf install python3 python3-pip
```

### macOS

```bash
python3 --version
```

Se não estiver instalado:
```bash
# Via Homebrew
brew install python3
```

## 🌐 Ambientes Virtuais (Recomendado)

Usar ambientes virtuais isola as dependências do projeto:

### Criar Ambiente Virtual

```bash
# Windows
python -m venv venv

# Linux/Mac
python3 -m venv venv
```

### Ativar Ambiente Virtual

```bash
# Windows (CMD)
venv\Scripts\activate

# Windows (PowerShell)
venv\Scripts\Activate.ps1

# Linux/Mac
source venv/bin/activate
```

### Desativar Ambiente Virtual

```bash
deactivate
```

## 📦 Instalação Offline

Se você não tem conexão com internet:

1. **Baixe as dependências** (em uma máquina com internet):
```bash
pip download -r requirements.txt -d packages/
```

2. **Transfira a pasta `packages/`** para a máquina offline

3. **Instale offline**:
```bash
pip install --no-index --find-links=packages/ -r requirements.txt
```

## 🔄 Atualizando

### Via pip

```bash
pip install --upgrade github-repos-collector
```

### Via Git

```bash
cd github-repos-collector
git pull origin main
pip install -r requirements.txt
```

## 🗑️ Desinstalação

### Via pip

```bash
pip uninstall github-repos-collector
```

### Manual

Se instalou via git clone, simplesmente delete a pasta:

```bash
# Linux/Mac
rm -rf github-repos-collector

# Windows
rmdir /s github-repos-collector
```

## 🐳 Docker (Futuro)

Planejamos adicionar suporte Docker em versões futuras:

```bash
# Futuro
docker pull ghcr.io/yourusername/github-repos-collector
docker run -it github-repos-collector
```

## 🧪 Verificando a Instalação

Após instalar, verifique se tudo está funcionando:

```bash
# Via pip
github-repos-collector --help

# Via git clone
python app.py --help

# Deve mostrar:
# Usage: app.py [OPTIONS]
# Coletor de Repositórios do GitHub - Versão Melhorada
```

## 🔍 Troubleshooting

### Erro: "python não é reconhecido"

**Solução**: Python não está no PATH. Reinstale Python marcando "Add Python to PATH".

### Erro: "pip não é reconhecido"

**Solução**: 
```bash
python -m pip install --upgrade pip
```

### Erro: "ModuleNotFoundError: No module named 'requests'"

**Solução**:
```bash
pip install -r requirements.txt
```

### Erro: "Permission denied"

**Solução** (Linux/Mac):
```bash
sudo pip install github-repos-collector
# ou
pip install --user github-repos-collector
```

### Erro: "SSL Certificate Error"

**Solução**:
```bash
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org github-repos-collector
```

### Erro no Windows: "Execution of scripts is disabled"

**Solução** (PowerShell como Admin):
```powershell
Set-ExecutionPolicy RemoteSigned
```

## 📊 Verificando Dependências

Para ver todas as dependências instaladas:

```bash
pip list
```

Para verificar dependências desatualizadas:

```bash
pip list --outdated
```

## 🔐 Instalação Segura

### Verificar Hash do Pacote

```bash
pip hash github-repos-collector
```

### Instalar de Fonte Confiável

```bash
pip install --index-url https://pypi.org/simple/ github-repos-collector
```

## 💻 Instalação em Diferentes Ambientes

### Anaconda/Miniconda

```bash
# Criar ambiente
conda create -n grc python=3.9

# Ativar ambiente
conda activate grc

# Instalar
pip install github-repos-collector
```

### Poetry

```bash
# Adicionar ao projeto
poetry add github-repos-collector

# Ou para desenvolvimento
poetry add --dev github-repos-collector
```

### Pipenv

```bash
# Adicionar ao projeto
pipenv install github-repos-collector

# Ou para desenvolvimento
pipenv install --dev github-repos-collector
```

## 📱 Instalação em Sistemas Específicos

### Raspberry Pi

```bash
sudo apt-get update
sudo apt-get install python3-pip
pip3 install github-repos-collector
```

### Windows Subsystem for Linux (WSL)

```bash
# Instalar Python
sudo apt-get update
sudo apt-get install python3 python3-pip

# Instalar o programa
pip3 install github-repos-collector
```

### Termux (Android)

```bash
pkg install python
pip install github-repos-collector
```

## 🎓 Próximos Passos

Após a instalação:

1. Leia o [Guia Rápido](GUIA_RAPIDO.md)
2. Veja os [Exemplos](EXEMPLOS.md)
3. Execute seu primeiro comando:
   ```bash
   github-repos-collector --linguagem=Python --exportar=csv
   ```

## 📞 Suporte

Se encontrar problemas:

1. Verifique a [documentação](README.md)
2. Procure em [issues existentes](https://github.com/yourusername/github-repos-collector/issues)
3. Abra uma [nova issue](https://github.com/yourusername/github-repos-collector/issues/new)

---

**Última atualização:** Janeiro 2026
