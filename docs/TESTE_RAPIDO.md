# 🧪 Teste Rápido - Verificação de Funcionamento

## ✅ Checklist de Instalação

### 1. Verificar Python
```bash
python --version
```
**Esperado**: Python 3.7 ou superior

### 2. Instalar Dependências
```bash
pip install -r requirements.txt
```
**Esperado**: Instalação bem-sucedida de `requests` e `click`

### 3. Verificar Help
```bash
python app.py --help
```
**Esperado**: Lista de opções disponíveis

---

## 🎯 Testes Funcionais

### Teste 1: Modo Interativo (RECOMENDADO)
```bash
python app.py
```

**Entrada de Teste**:
- Linguagem: `Python`
- Ordenação: `1`
- Páginas: `1`
- Filtros: `n`
- Cache: `s`
- Exportar: `2` (CSV)

**Resultado Esperado**:
- ✅ Coleta ~30 repositórios Python
- ✅ Exibe os 10 primeiros no console
- ✅ Cria arquivo CSV em `exports/`
- ✅ Salva cache em `cache/`

---

### Teste 2: Linha de Comando Simples
```bash
python app.py --linguagem=JavaScript --num-paginas=1 --exportar=csv
```

**Resultado Esperado**:
- ✅ Coleta ~30 repositórios JavaScript
- ✅ Exibe todos no console
- ✅ Cria arquivo CSV em `exports/`

---

### Teste 3: Com Filtros
```bash
python app.py --linguagem=Python --dias=30 --min-estrelas=100 --exportar=json
```

**Resultado Esperado**:
- ✅ Coleta repositórios Python
- ✅ Filtra por data (últimos 30 dias)
- ✅ Filtra por estrelas (mínimo 100)
- ✅ Cria arquivo JSON em `exports/`

---

### Teste 4: Com Cache
```bash
# Primeira execução (cria cache)
python app.py --linguagem=Rust --num-paginas=2

# Segunda execução (usa cache - deve ser instantâneo)
python app.py --linguagem=Rust --usar-cache --min-estrelas=50 --exportar=csv
```

**Resultado Esperado**:
- ✅ Primeira execução: ~10-15 segundos
- ✅ Segunda execução: Instantâneo (< 1 segundo)
- ✅ Filtro aplicado aos dados em cache

---

### Teste 5: Exportação Múltipla
```bash
python app.py --linguagem=Go --exportar=ambos
```

**Resultado Esperado**:
- ✅ Cria arquivo CSV em `exports/`
- ✅ Cria arquivo JSON em `exports/`
- ✅ Ambos com os mesmos dados

---

## 📊 Verificação dos Arquivos Gerados

### Estrutura de Diretórios
```
github-repos-collector/
├── cache/
│   ├── cache_Python.json
│   ├── cache_JavaScript.json
│   └── cache_Rust.json
└── exports/
    ├── repos_Python_20260120_143022.csv
    ├── repos_JavaScript_20260120_143530.csv
    └── repos_Go_20260120_144015.json
```

### Verificar CSV
1. Abra o arquivo CSV no Excel
2. Verifique as colunas: nome, estrelas, forks, link, data_criacao, data_atualizacao
3. Verifique se os dados estão corretos

### Verificar JSON
```bash
# Windows
type exports\repos_Python_*.json

# Linux/Mac
cat exports/repos_Python_*.json
```

---

## 🐛 Resolução de Problemas

### Erro: "ModuleNotFoundError: No module named 'requests'"
**Solução**:
```bash
pip install -r requirements.txt
```

### Erro: "python não é reconhecido"
**Solução**:
- Instale Python: https://www.python.org/downloads/
- Marque "Add Python to PATH" durante instalação

### Erro: "API rate limit exceeded"
**Solução**:
- Aguarde alguns minutos
- Use `--usar-cache` para evitar novas chamadas à API

### Erro: Arquivo CSV não abre corretamente no Excel
**Solução**:
- O arquivo usa UTF-8 com BOM
- Tente abrir com "Abrir com" → Excel
- Ou importe como dados externos no Excel

---

## ✅ Checklist Final

Marque cada item após testar:

- [ ] Python instalado e funcionando
- [ ] Dependências instaladas
- [ ] Modo interativo funciona
- [ ] Linha de comando funciona
- [ ] Filtro por data funciona
- [ ] Filtro por estrelas funciona
- [ ] Exportação CSV funciona
- [ ] Exportação JSON funciona
- [ ] Cache funciona
- [ ] Arquivos abrem no Excel
- [ ] Diretórios criados automaticamente

---

## 🎉 Teste de Aceitação Final

Execute este comando completo:

```bash
python app.py --linguagem=Python --num-paginas=2 --dias=60 --min-estrelas=500 --exportar=ambos --usar-cache
```

**Deve**:
1. ✅ Coletar 60 repositórios Python
2. ✅ Filtrar por data (últimos 60 dias)
3. ✅ Filtrar por estrelas (mínimo 500)
4. ✅ Exportar para CSV e JSON
5. ✅ Salvar em cache
6. ✅ Exibir resumo no console

**Se tudo funcionar, o projeto está 100% operacional!** 🎊

---

## 📞 Suporte

Se algum teste falhar:
1. Verifique a versão do Python (3.7+)
2. Reinstale as dependências
3. Verifique a conexão com internet
4. Consulte a documentação completa
5. Abra uma issue no GitHub

---

**Boa sorte com os testes!** 🚀
