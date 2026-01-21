# 🚀 Guia Rápido - GitHub Repos Collector

## Para Iniciantes (Sem Conhecimento Técnico)

### Passo 1: Instalar Python
Se você não tem Python instalado:
- Windows: Baixe em https://www.python.org/downloads/
- Durante a instalação, marque "Add Python to PATH"

### Passo 2: Instalar Dependências
Abra o terminal/prompt de comando na pasta do projeto e execute:
```bash
pip install -r requirements.txt
```

### Passo 3: Executar o Programa
```bash
python app.py
```

Pronto! O programa vai te guiar passo a passo. 🎉

## Exemplos Práticos

### Exemplo 1: Encontrar Projetos Python Populares
```bash
python app.py
```
- Linguagem: `Python`
- Ordenar por: `1` (estrelas)
- Páginas: `2`
- Filtros: `n` (não)
- Cache: `s` (sim)
- Exportar: `2` (CSV para Excel)

**Resultado**: Arquivo CSV com os projetos Python mais populares que você pode abrir no Excel!

### Exemplo 2: Projetos JavaScript Recentes
```bash
python app.py
```
- Linguagem: `JavaScript`
- Ordenar por: `3` (atualização)
- Páginas: `1`
- Filtros: `s` (sim)
  - Filtrar por data: `s`
  - Últimos X dias: `7`
  - Filtrar por estrelas: `s`
  - Mínimo de estrelas: `100`
- Exportar: `2` (CSV)

**Resultado**: Projetos JavaScript criados na última semana com pelo menos 100 estrelas!

### Exemplo 3: Para Recrutadores - Encontrar Talentos
```bash
python app.py
```
- Linguagem: `Java`
- Ordenar por: `1` (estrelas)
- Páginas: `3`
- Filtros: `n`
- Exportar: `2` (CSV)

**Resultado**: Lista de projetos Java populares para identificar desenvolvedores ativos!

## Comandos Rápidos (Para Quem Prefere Terminal)

### Busca Simples
```bash
python app.py --linguagem=Python --num-paginas=2 --exportar=csv
```

### Com Filtros
```bash
python app.py --linguagem=JavaScript --dias=7 --min-estrelas=100 --exportar=csv
```

### Busca Completa
```bash
python app.py --linguagem=Rust --num-paginas=5 --dias=30 --min-estrelas=500 --exportar=ambos --usar-cache
```

## 📊 Abrindo os Resultados

### Arquivos CSV
1. Vá para a pasta `exports/`
2. Encontre o arquivo `repos_NomeDaLinguagem_data.csv`
3. Clique duas vezes para abrir no Excel
4. Pronto! Você pode ordenar, filtrar e analisar os dados

### Arquivos JSON
- Útil para programadores
- Pode ser importado em outras ferramentas de análise

## ❓ Perguntas Frequentes

**P: Quantos repositórios vou obter?**
R: Cada página tem aproximadamente 30 repositórios. Se você escolher 3 páginas, terá ~90 repositórios.

**P: O que é cache?**
R: É uma cópia salva dos resultados. Se você buscar a mesma linguagem novamente, será mais rápido!

**P: Posso buscar qualquer linguagem?**
R: Sim! Python, JavaScript, Java, C++, Rust, Go, TypeScript, etc.

**P: Os filtros são obrigatórios?**
R: Não! Você pode pular os filtros e buscar todos os repositórios.

**P: Preciso de conta no GitHub?**
R: Não! A ferramenta usa a API pública do GitHub.

## 🎯 Dicas

1. **Para análise rápida**: Use 1-2 páginas
2. **Para pesquisa completa**: Use 5-10 páginas
3. **Para encontrar projetos novos**: Use o filtro de dias (7-30 dias)
4. **Para projetos consolidados**: Use filtro de estrelas mínimas (100+)
5. **Sempre exporte para CSV**: Facilita a análise no Excel!

## 🆘 Problemas Comuns

### "comando não encontrado"
- Certifique-se de que Python está instalado
- Tente `python3 app.py` em vez de `python app.py`

### "ModuleNotFoundError"
- Execute: `pip install -r requirements.txt`

### "API rate limit"
- Aguarde alguns minutos
- Use o cache para evitar chamadas repetidas

## 📞 Suporte

Se tiver dúvidas, abra uma issue no GitHub ou consulte o README.md completo.

---

**Feito com ❤️ para facilitar a vida de desenvolvedores e recrutadores!**
