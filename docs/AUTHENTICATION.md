# 🔑 Autenticação GitHub

## 🎯 Visão Geral

A partir da versão 2.2.0, o GitHub Repos Collector suporta **autenticação via GitHub Personal Access Token**, aumentando o rate limit de **60 para 5000 requisições por hora** - um aumento de **83x**!

## 📊 Comparação: Sem vs Com Autenticação

| Aspecto | Sem Token | Com Token | Melhoria |
|---------|-----------|-----------|----------|
| **Rate Limit** | 60/hora | 5000/hora | **83x** |
| **Páginas/hora** | ~60 | ~5000 | **83x** |
| **Repos/hora** | ~1800 | ~150000 | **83x** |
| **Uso Prático** | ❌ Limitado | ✅ Viável | - |

## 🚀 Como Configurar

### Método 1: Variável de Ambiente (Recomendado)

#### Windows (PowerShell)
```powershell
$env:GITHUB_TOKEN="ghp_xxxxxxxxxxxxxxxxxxxx"
python app.py search --linguagem=Python
```

#### Windows (CMD)
```cmd
set GITHUB_TOKEN=ghp_xxxxxxxxxxxxxxxxxxxx
python app.py search --linguagem=Python
```

#### Linux/Mac
```bash
export GITHUB_TOKEN="ghp_xxxxxxxxxxxxxxxxxxxx"
python app.py search --linguagem=Python
```

#### Permanente (Linux/Mac)
Adicione ao `~/.bashrc` ou `~/.zshrc`:
```bash
export GITHUB_TOKEN="ghp_xxxxxxxxxxxxxxxxxxxx"
```

### Método 2: Arquivo de Configuração

```bash
# Configurar token
python app.py config set-token ghp_xxxxxxxxxxxxxxxxxxxx

# Usar normalmente
python app.py search --linguagem=Python
```

O token é salvo em `~/.grc/config.json` com permissões restritas.

## 🔐 Como Criar um Token

### Passo 1: Acessar GitHub Settings

1. Acesse: https://github.com/settings/tokens
2. Ou: GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)

### Passo 2: Gerar Novo Token

1. Clique em "Generate new token" → "Generate new token (classic)"
2. Dê um nome descritivo: `github-repos-collector`
3. Defina expiração (recomendado: 90 dias)
4. **NÃO selecione nenhum escopo** (apenas leitura pública)
5. Clique em "Generate token"

### Passo 3: Copiar Token

⚠️ **IMPORTANTE**: Copie o token imediatamente! Você não poderá vê-lo novamente.

O token começa com `ghp_` (classic) ou `github_pat_` (fine-grained).

### Passo 4: Configurar

```bash
# Método 1: Variável de ambiente
export GITHUB_TOKEN="ghp_seu_token_aqui"

# Método 2: Arquivo de configuração
python app.py config set-token ghp_seu_token_aqui
```

## 📋 Comandos de Configuração

### Verificar Status

```bash
python app.py auth-status
```

**Saída sem token:**
```
⚠️  Autenticação: Não configurada
   Rate Limit: 60 requisições/hora

💡 Dica: Configure um token para aumentar o rate limit:
   1. Crie um token em: https://github.com/settings/tokens
   2. Configure com: export GITHUB_TOKEN='seu_token'
   3. Ou use: python app.py config set-token seu_token
```

**Saída com token:**
```
🔑 Autenticação: Ativa
   Token: ghp_...xxxx
   Rate Limit: 5000 requisições/hora
```

### Configurar Token

```bash
python app.py config set-token ghp_xxxxxxxxxxxxxxxxxxxx
```

**Saída:**
```
✅ Token configurado com sucesso!
   Arquivo: ~/.grc/config.json

💡 O token foi salvo de forma segura.
   Agora você tem 5000 requisições/hora!
```

### Mostrar Token (Mascarado)

```bash
python app.py config show-token
```

**Saída:**
```
🔑 Token Configurado:
   Token: ghp_...xxxx
   Arquivo: ~/.grc/config.json
```

### Remover Token

```bash
python app.py config remove-token
```

**Saída:**
```
Tem certeza que deseja remover o token? [y/N]: y
✅ Token removido com sucesso!
```

### Ver Todas as Opções

```bash
python app.py config --help
```

## 🎨 Feedback Visual

Durante a busca, o status de autenticação é exibido:

**Sem autenticação:**
```
📊 Informações da Busca:
   Linguagem: Python
   Páginas: 3
   Repositórios esperados: ~90
   ⚠️  Autenticado: Não (60 req/hora)
```

**Com autenticação:**
```
📊 Informações da Busca:
   Linguagem: Python
   Páginas: 3
   Repositórios esperados: ~90
   🔑 Autenticado: Sim (5000 req/hora)
```

## 🔒 Segurança

### Armazenamento Seguro

- Token salvo em `~/.grc/config.json`
- Permissões restritas (0600 - apenas usuário)
- Nunca commitado no Git (.gitignore)

### Boas Práticas

1. ✅ **Use tokens com escopo mínimo** (nenhum escopo para leitura pública)
2. ✅ **Defina expiração** (90 dias recomendado)
3. ✅ **Revogue tokens não usados**
4. ✅ **Não compartilhe tokens**
5. ✅ **Use variáveis de ambiente em CI/CD**

### Revogar Token

Se o token foi comprometido:

1. Acesse: https://github.com/settings/tokens
2. Encontre o token
3. Clique em "Delete"
4. Gere um novo token

## 💡 Casos de Uso

### Uso Pessoal

```bash
# Configurar uma vez
python app.py config set-token ghp_xxxxxxxxxxxxxxxxxxxx

# Usar sempre
python app.py search --linguagem=Python --num-paginas=10
```

### CI/CD

```yaml
# GitHub Actions
env:
  GITHUB_TOKEN: ${{ secrets.GH_TOKEN }}

steps:
  - run: python app.py search --linguagem=Python --exportar=json
```

### Scripts Automatizados

```bash
#!/bin/bash
export GITHUB_TOKEN="ghp_xxxxxxxxxxxxxxxxxxxx"

# Coletar dados de múltiplas linguagens
for lang in Python JavaScript Go Rust; do
    python app.py search --linguagem=$lang --num-paginas=5 --exportar=csv
done
```

### Múltiplos Usuários

```bash
# Usuário 1
export GITHUB_TOKEN="ghp_token_usuario1"
python app.py search --linguagem=Python

# Usuário 2
export GITHUB_TOKEN="ghp_token_usuario2"
python app.py search --linguagem=JavaScript
```

## 🐛 Troubleshooting

### Token Inválido

**Problema**: `401 Unauthorized`

**Solução**:
1. Verifique se o token está correto
2. Verifique se o token não expirou
3. Gere um novo token

### Token Não Reconhecido

**Problema**: Ainda mostra 60 req/hora

**Solução**:
```bash
# Verificar se o token está configurado
python app.py auth-status

# Reconfigurar
python app.py config set-token ghp_xxxxxxxxxxxxxxxxxxxx
```

### Rate Limit Ainda Baixo

**Problema**: Mesmo com token, rate limit é 60

**Solução**:
- Token pode estar inválido ou expirado
- Verifique em: https://github.com/settings/tokens
- Gere um novo token

### Arquivo de Configuração Não Encontrado

**Problema**: `~/.grc/config.json` não existe

**Solução**:
```bash
# Criar diretório
mkdir -p ~/.grc

# Configurar token
python app.py config set-token ghp_xxxxxxxxxxxxxxxxxxxx
```

## 📈 Monitoramento de Rate Limit

O programa mostra o rate limit em tempo real:

```
✅ Coleta Concluída!
   Total de repositórios: 90
   Páginas processadas: 3/3
   Requisições restantes: 4997
```

### Alertas

- 🟢 **> 100 requisições**: Tudo OK
- 🟡 **10-100 requisições**: Atenção
- 🔴 **< 10 requisições**: Crítico

## 🔄 Ordem de Prioridade

O programa busca o token nesta ordem:

1. **Variável de ambiente** `GITHUB_TOKEN`
2. **Arquivo de configuração** `~/.grc/config.json`

Se nenhum for encontrado, usa modo não autenticado (60 req/hora).

## 📚 Referências

- [GitHub API Rate Limiting](https://docs.github.com/en/rest/overview/resources-in-the-rest-api#rate-limiting)
- [Creating a Personal Access Token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)
- [GitHub API Authentication](https://docs.github.com/en/rest/overview/other-authentication-methods)

## 🎯 Próximas Melhorias

- [ ] Suporte a GitHub Apps
- [ ] Renovação automática de token
- [ ] Múltiplos tokens (round-robin)
- [ ] Dashboard de uso de rate limit
- [ ] Notificações quando rate limit baixo

---

**Implementado em:** Janeiro 2026  
**Versão:** 2.2.0  
**Status:** ✅ Completo e Testado
