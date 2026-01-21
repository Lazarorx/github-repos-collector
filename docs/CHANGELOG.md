# 📝 Changelog

Todas as mudanças notáveis neste projeto serão documentadas neste arquivo.

## [2.0.0] - 2026-01-20

### ✨ Novas Funcionalidades

#### 📊 Exportação de Dados
- **Exportação para CSV**: Arquivos compatíveis com Excel (encoding UTF-8 com BOM)
- **Exportação para JSON**: Formato estruturado para análise programática
- **Exportação combinada**: Opção de exportar para ambos os formatos simultaneamente
- **Nomenclatura automática**: Arquivos nomeados com timestamp (ex: `repos_Python_20260120_143022.csv`)
- **Diretório organizado**: Todos os exports salvos em `exports/`

#### 🔍 Filtros Avançados
- **Filtro por data**: Buscar apenas repositórios criados nos últimos X dias
  - Útil para encontrar projetos novos e tendências emergentes
  - Exemplo: `--dias=7` para repositórios da última semana
- **Filtro por estrelas**: Definir número mínimo de estrelas
  - Filtrar por popularidade e qualidade
  - Exemplo: `--min-estrelas=100` para projetos consolidados
- **Filtros combinados**: Usar ambos os filtros simultaneamente
  - Exemplo: Projetos novos E populares

#### 🎨 Interface Amigável
- **Menu interativo completo**: Guia passo a passo para usuários não-técnicos
- **Interface colorida**: Uso de cores para melhor visualização
  - Cyan para títulos e separadores
  - Yellow para passos e perguntas
  - Green para confirmações e sucessos
  - White/Bold para destaques
- **Emojis informativos**: Ícones visuais para facilitar navegação
- **Confirmações inteligentes**: Valores padrão sugeridos
- **Modo interativo automático**: Ativa quando nenhum parâmetro é fornecido

#### 💾 Sistema de Cache Melhorado
- **Cache por linguagem**: Arquivos separados para cada linguagem
- **Metadados de cache**: Inclui data/hora da coleta
- **Diretório organizado**: Cache salvo em `cache/`
- **Opção de usar cache**: Flag `--usar-cache` para reutilizar dados
- **Cache automático**: Salva automaticamente após cada coleta

#### 🚀 Facilidades de Uso
- **Scripts de instalação**: `instalar.bat` para Windows
- **Scripts de execução**: `iniciar.bat` para iniciar rapidamente
- **Documentação expandida**: 
  - README.md atualizado com exemplos
  - GUIA_RAPIDO.md para iniciantes
  - EXEMPLOS.md com casos de uso reais
  - CHANGELOG.md (este arquivo)
- **Suporte a múltiplas páginas melhorado**: Indicador de progresso

### 🔧 Melhorias

#### Interface de Linha de Comando
- Novos parâmetros opcionais:
  - `--interativo` ou `-i`: Força modo interativo
  - `--dias`: Filtro por data
  - `--min-estrelas`: Filtro por popularidade
  - `--exportar`: Formato de exportação (csv/json/ambos)
  - `--usar-cache`: Usar dados em cache
- Parâmetros originais mantidos para compatibilidade
- Help text melhorado para cada opção

#### Logging e Feedback
- Mensagens mais informativas durante a coleta
- Indicador de progresso por página
- Feedback sobre filtros aplicados
- Confirmação de exportação com caminho do arquivo
- Contagem de repositórios em cada etapa

#### Organização de Código
- Funções modulares e bem documentadas
- Docstrings completas em todas as funções
- Separação clara de responsabilidades
- Tratamento de erros melhorado

### 📦 Arquivos Adicionados

```
github-repos-collector/
├── requirements.txt          # Dependências do projeto
├── .gitignore               # Arquivos a ignorar no Git
├── GUIA_RAPIDO.md          # Guia para iniciantes
├── EXEMPLOS.md             # Casos de uso reais
├── CHANGELOG.md            # Este arquivo
├── instalar.bat            # Script de instalação (Windows)
├── iniciar.bat             # Script de execução (Windows)
├── cache/                  # Diretório de cache (criado automaticamente)
└── exports/                # Diretório de exportações (criado automaticamente)
```

### 🐛 Correções
- Encoding UTF-8 com BOM para CSV (compatibilidade com Excel)
- Tratamento de erros HTTP melhorado
- Validação de entrada do usuário
- Criação automática de diretórios necessários

### 📚 Documentação
- README.md completamente reescrito
- Exemplos práticos para diferentes perfis de usuário
- Guia rápido para iniciantes
- Casos de uso detalhados
- FAQ expandido

### 🔄 Compatibilidade
- **Mantém compatibilidade total com versão anterior**
- Todos os comandos antigos continuam funcionando
- Novos recursos são opcionais
- Modo interativo não interfere com uso programático

---

## [1.0.0] - Data Original

### Funcionalidades Originais
- Coleta de repositórios do GitHub via API
- Busca por linguagem de programação
- Ordenação por estrelas, forks ou atualização
- Suporte a múltiplas páginas
- Exibição formatada no console
- Logging básico
- Tratamento de erros HTTP

---

## 🔮 Próximas Versões (Planejado)

### [2.1.0] - Futuro
- [ ] Exportação para Excel (.xlsx) nativo
- [ ] Gráficos automáticos nos exports
- [ ] Filtro por linguagem secundária
- [ ] Busca por tópicos/tags
- [ ] Interface web (opcional)
- [ ] Suporte a autenticação GitHub (rate limit maior)
- [ ] Comparação entre linguagens
- [ ] Relatórios automáticos em PDF

### [2.2.0] - Futuro
- [ ] Análise de tendências temporais
- [ ] Detecção de projetos em crescimento
- [ ] Recomendações personalizadas
- [ ] Integração com outras plataformas (GitLab, Bitbucket)
- [ ] Dashboard interativo
- [ ] Notificações de novos projetos

---

## 📊 Estatísticas da Versão 2.0

- **Linhas de código**: ~450 (vs ~150 na v1.0)
- **Funções**: 12 (vs 4 na v1.0)
- **Opções CLI**: 9 (vs 4 na v1.0)
- **Arquivos de documentação**: 5 novos
- **Formatos de exportação**: 2 (CSV e JSON)
- **Tipos de filtro**: 2 (data e estrelas)

---

**Desenvolvido com ❤️ para a comunidade de desenvolvedores**
