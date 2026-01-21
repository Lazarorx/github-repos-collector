# 📚 Exemplos de Uso - GitHub Repos Collector

## 🎯 Cenários Reais de Uso

### 1. Recrutador Procurando Desenvolvedores Python

**Objetivo**: Encontrar projetos Python populares para identificar desenvolvedores talentosos.

**Modo Interativo**:
```bash
python app.py
```
- Linguagem: `Python`
- Ordenação: `1` (por estrelas)
- Páginas: `3` (aproximadamente 90 repositórios)
- Filtros: `n` (não aplicar)
- Cache: `s` (sim)
- Exportar: `2` (CSV para abrir no Excel)

**Resultado**: Arquivo CSV com 90 projetos Python mais populares, pronto para análise no Excel!

---

### 2. Desenvolvedor Buscando Projetos JavaScript Recentes

**Objetivo**: Descobrir projetos JavaScript criados recentemente com boa popularidade.

**Linha de Comando**:
```bash
python app.py --linguagem=JavaScript --dias=30 --min-estrelas=50 --exportar=csv
```

**Resultado**: Projetos JavaScript criados nos últimos 30 dias com pelo menos 50 estrelas.

---

### 3. Pesquisador Analisando Tendências em Rust

**Objetivo**: Coletar dados sobre projetos Rust para análise acadêmica.

**Linha de Comando**:
```bash
python app.py --linguagem=Rust --num-paginas=10 --exportar=ambos --usar-cache
```

**Resultado**: 
- ~300 repositórios Rust
- Exportado em CSV (para Excel) e JSON (para análise programática)
- Salvo em cache para consultas futuras

---

### 4. Gerente de Projeto Buscando Bibliotecas TypeScript

**Objetivo**: Encontrar bibliotecas TypeScript atualizadas recentemente.

**Modo Interativo**:
```bash
python app.py
```
- Linguagem: `TypeScript`
- Ordenação: `3` (por atualização)
- Páginas: `2`
- Filtros: `s` (sim)
  - Data: `s` → `60` dias
  - Estrelas: `s` → `200` estrelas mínimas
- Exportar: `2` (CSV)

**Resultado**: Bibliotecas TypeScript ativas (atualizadas nos últimos 60 dias) e populares (200+ estrelas).

---

### 5. Estudante Aprendendo Go

**Objetivo**: Encontrar projetos Go para estudar e contribuir.

**Linha de Comando**:
```bash
python app.py --linguagem=Go --ordenacao=stars --num-paginas=2 --min-estrelas=100 --exportar=json
```

**Resultado**: Projetos Go populares (100+ estrelas) em formato JSON para análise.

---

### 6. Tech Lead Avaliando Frameworks Java

**Objetivo**: Comparar frameworks Java mais populares.

**Modo Interativo**:
```bash
python app.py
```
- Linguagem: `Java`
- Ordenação: `1` (estrelas)
- Páginas: `5`
- Filtros: `s`
  - Data: `n`
  - Estrelas: `s` → `1000` estrelas mínimas
- Cache: `s`
- Exportar: `4` (CSV + JSON)

**Resultado**: Top frameworks Java (1000+ estrelas) em ambos os formatos.

---

### 7. Analista de Dados Coletando Informações

**Objetivo**: Coletar dados de múltiplas linguagens para análise comparativa.

**Script Bash/Batch**:
```bash
# Coletar dados de várias linguagens
python app.py --linguagem=Python --num-paginas=5 --exportar=csv --usar-cache
python app.py --linguagem=JavaScript --num-paginas=5 --exportar=csv --usar-cache
python app.py --linguagem=Java --num-paginas=5 --exportar=csv --usar-cache
python app.py --linguagem=Go --num-paginas=5 --exportar=csv --usar-cache
python app.py --linguagem=Rust --num-paginas=5 --exportar=csv --usar-cache
```

**Resultado**: 5 arquivos CSV, um para cada linguagem, prontos para análise comparativa.

---

### 8. Startup Buscando Projetos de IA

**Objetivo**: Identificar projetos de IA/ML em Python para inspiração.

**Linha de Comando**:
```bash
python app.py --linguagem=Python --dias=90 --min-estrelas=500 --num-paginas=3 --exportar=ambos
```

**Resultado**: Projetos Python recentes (últimos 3 meses) e populares (500+ estrelas), ideal para identificar tendências em IA.

---

### 9. Desenvolvedor Freelancer Buscando Projetos para Contribuir

**Objetivo**: Encontrar projetos ativos que precisam de contribuidores.

**Modo Interativo**:
```bash
python app.py
```
- Linguagem: `JavaScript`
- Ordenação: `3` (atualização recente)
- Páginas: `3`
- Filtros: `s`
  - Data: `s` → `14` dias
  - Estrelas: `s` → `50` estrelas mínimas
- Exportar: `2` (CSV)

**Resultado**: Projetos JavaScript ativos (atualizados nas últimas 2 semanas) com comunidade ativa (50+ estrelas).

---

### 10. Professor Preparando Material Didático

**Objetivo**: Encontrar exemplos de código para ensinar aos alunos.

**Linha de Comando**:
```bash
python app.py --linguagem=C++ --ordenacao=stars --num-paginas=2 --min-estrelas=100 --exportar=csv
```

**Resultado**: Projetos C++ bem estruturados e populares para usar como exemplos em aula.

---

## 💡 Dicas Avançadas

### Combinando Filtros
```bash
# Projetos Python novos E populares
python app.py --linguagem=Python --dias=7 --min-estrelas=1000 --exportar=csv

# Projetos JavaScript atualizados recentemente
python app.py --linguagem=JavaScript --ordenacao=updated --num-paginas=5 --exportar=json
```

### Usando Cache Eficientemente
```bash
# Primeira busca (sem cache)
python app.py --linguagem=Python --num-paginas=10 --exportar=csv

# Buscas subsequentes (com cache - muito mais rápido!)
python app.py --linguagem=Python --usar-cache --min-estrelas=500 --exportar=csv
python app.py --linguagem=Python --usar-cache --dias=30 --exportar=json
```

### Exportação Estratégica
- **CSV**: Para análise no Excel, compartilhar com não-programadores
- **JSON**: Para processamento programático, integração com outras ferramentas
- **Ambos**: Para máxima flexibilidade

---

## 📊 Análise dos Dados Exportados

### No Excel (CSV)
1. Abra o arquivo CSV
2. Use "Filtros" para ordenar por estrelas/forks
3. Crie gráficos de popularidade
4. Identifique tendências

### Programaticamente (JSON)
```python
import json

with open('exports/repos_Python_20260120_143022.json', 'r') as f:
    repos = json.load(f)
    
# Análise
total_estrelas = sum(r['estrelas'] for r in repos)
media_estrelas = total_estrelas / len(repos)
print(f"Média de estrelas: {media_estrelas}")
```

---

## 🎓 Casos de Uso por Perfil

| Perfil | Caso de Uso | Comando Recomendado |
|--------|-------------|---------------------|
| Recrutador | Encontrar talentos | `python app.py` (modo interativo) |
| Desenvolvedor | Aprender novas tecnologias | `--linguagem=X --ordenacao=stars` |
| Pesquisador | Coletar dados | `--num-paginas=10 --exportar=ambos` |
| Estudante | Projetos para estudar | `--min-estrelas=100 --exportar=csv` |
| Tech Lead | Avaliar ferramentas | `--min-estrelas=1000 --dias=180` |
| Freelancer | Projetos para contribuir | `--ordenacao=updated --dias=14` |

---

**Experimente e adapte esses exemplos às suas necessidades!** 🚀
