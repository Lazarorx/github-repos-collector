# 📝 Changelog

Todas as mudanças notáveis neste projeto serão documentadas neste arquivo.

## [2.5.0] - 2026-01-23

### ✨ Novas Funcionalidades

#### 📊 Gráfico de Distribuição de Estrelas
- **Visualização automática**: Gráfico de barras ASCII após o dashboard
  - Distribuição inteligente em faixas (0-10k, 10k-50k, 50k-100k, 100k+)
  - Faixas adaptativas baseadas no máximo de estrelas
  - Barras proporcionais ao número de repositórios
  - Percentual de cada faixa
  - Cores vibrantes (cyan para labels, yellow para barras)
- **Análise visual**: Entenda a distribuição de popularidade rapidamente
  - Identifique concentração de repositórios
  - Veja padrões de distribuição
  - Compare faixas de popularidade

#### 🔄 Comparação entre Linguagens
- **Novo comando `compare`**: Compare estatísticas de múltiplas linguagens
  - Sintaxe: `python app.py compare Python JavaScript Go`
  - Suporta 2 ou mais linguagens simultaneamente
  - Usa cache automaticamente para velocidade
- **Tabela comparativa**: Visão lado a lado
  - Total de repositórios por linguagem
  - Total de estrelas acumuladas
  - Média de estrelas por repositório
  - Total de forks
  - Média de forks
  - Repositório mais popular de cada linguagem
- **Gráfico de comparação**: Barras horizontais
  - Visualização de estrelas totais
  - Barras proporcionais entre linguagens
  - Ordenação automática (mais popular primeiro)
- **Resumo inteligente**: Destaques da comparação
  - 🏆 Linguagem com mais estrelas totais
  - 📊 Linguagem com mais repositórios
  - 📈 Linguagem com maior média de estrelas

#### 🎨 Melhorias Visuais
- **Painéis coloridos**: Cada seção com cor específica
  - Magenta para distribuição
  - Yellow para comparação de estrelas
  - Green para resumo
- **Formatação consistente**: Números com separador de milhares
- **Emojis contextuais**: Ícones para cada métrica
- **Layout responsivo**: Adapta ao tamanho do terminal

### 🔧 Melhorias Técnicas
- **Função exibir_grafico_distribuicao()**: Gráfico de distribuição
  - Cálculo automático de faixas
  - Adaptação baseada em max_estrelas
  - Barras ASCII proporcionais
- **Comando compare**: Comparação entre linguagens
  - Coleta paralela de dados
  - Reutilização de cache
  - Ordenação por popularidade
  - Cálculos agregados automáticos
- **Integração automática**: Gráfico exibido após dashboard
- **Validação de entrada**: Mínimo 2 linguagens para comparar

### 📚 Melhorias de UX
- **Insights visuais**: Entenda dados em segundos
- **Comparação facilitada**: Veja diferenças entre linguagens
- **Análise de distribuição**: Identifique padrões
- **Feedback completo**: Tabela + Dashboard + Gráfico + Comparação
- **Uso intuitivo**: Comandos simples e diretos

### 🐛 Correções
- Tratamento de listas com menos de 5 repositórios
- Validação de entrada no comando compare
- Melhor formatação de números grandes

### 📖 Exemplos de Uso

```bash
# Ver distribuição de estrelas
python app.py search --linguagem Python --num-paginas 1

# Comparar 3 linguagens
python app.py compare Python JavaScript Go

# Comparar com mais páginas
python app.py compare Rust TypeScript --num-paginas 2
```

---

## [2.4.0] - 2026-01-23

### ✨ Novas Funcionalidades

#### 📊 Dashboard de Estatísticas
- **Dashboard automático**: Exibido após a tabela de repositórios
  - **Estatísticas Gerais**: Painel com métricas agregadas
    - Total de repositórios encontrados
    - Total de estrelas acumuladas
    - Total de forks acumulados
    - Média de estrelas por repositório
    - Média de forks por repositório
  - **Destaques**: Painel com repositórios notáveis
    - 🏆 Mais Popular: Repositório com mais estrelas
    - 🔥 Mais Forks: Repositório mais copiado
    - 🆕 Mais Recente: Repositório criado mais recentemente
- **Layout lado a lado**: Dois painéis exibidos horizontalmente
- **Formatação elegante**: Números com separador de milhares
- **Cores contextuais**: Cada métrica com cor específica
  - Cyan para totais
  - Yellow para estrelas
  - Green para forks
  - Blue para datas
  - Magenta para médias

#### 🎨 Melhorias Visuais
- **Painéis Rich**: Uso de `Panel` e `Columns` da biblioteca Rich
- **Emojis informativos**: Ícones para cada métrica
- **Bordas coloridas**: Cyan para estatísticas, Yellow para destaques
- **Espaçamento inteligente**: Padding para melhor legibilidade
- **Informações condensadas**: Máximo de informação em espaço mínimo

### 🔧 Melhorias Técnicas
- **Função exibir_dashboard_estatisticas()**: Nova função dedicada
- **Cálculos automáticos**: Estatísticas calculadas dinamicamente
- **Integração com tabelas**: Dashboard exibido após tabela
- **Parâmetro mostrar_dashboard**: Controle opcional de exibição
- **Ordenação inteligente**: Encontra destaques automaticamente

### 📚 Melhorias de UX
- **Visão geral instantânea**: Entenda os dados em segundos
- **Comparação facilitada**: Médias ajudam a contextualizar
- **Destaques automáticos**: Não precisa procurar manualmente
- **Informação completa**: Estatísticas + Tabela + Dashboard
- **Profissionalismo**: Aparência de ferramenta analytics

### 🐛 Correções
- Formatação consistente de números grandes
- Tratamento de listas vazias
- Melhor alinhamento de painéis

---

## [2.3.0] - 2026-01-23

### ✨ Novas Funcionalidades

#### 🌈 Tabelas Formatadas com Rich
- **Exibição em tabela**: Repositórios exibidos em tabelas bonitas e legíveis
  - Bordas arredondadas e cores vibrantes
  - Colunas organizadas: Nº, Nome, Estrelas, Forks, Data
  - Números formatados com separador de milhares
  - Cores contextuais baseadas em popularidade
- **Resumo automático**: Painel com estatísticas
  - Total de repositórios
  - Média de estrelas
  - Formatação elegante
- **Cores inteligentes**: Destaque baseado em estrelas
  - Amarelo bold: > 50k estrelas
  - Amarelo: > 10k estrelas
  - Amarelo dim: < 10k estrelas

#### 🎨 Melhorias Visuais
- **Biblioteca Rich**: Interface moderna e profissional
- **Tabelas responsivas**: Ajustam ao tamanho do terminal
- **Emojis nas colunas**: ⭐ Estrelas, 🔀 Forks, 📅 Data
- **Limite inteligente**: Mostra top 20 no modo interativo, todos no CLI

### 🔧 Melhorias Técnicas
- **Dependência rich>=13.7.0**: Adicionada para formatação
- **Console global**: Instância única para output consistente
- **Função exibir_repositorios_tabela()**: Nova função para tabelas
- **Função legada mantida**: exibir_info_repositorio() para compatibilidade

### 📚 Melhorias de UX
- **Legibilidade 10x melhor**: Tabelas vs logs
- **Escaneamento visual**: Fácil comparar repositórios
- **Informações condensadas**: Mais dados em menos espaço
- **Profissionalismo**: Aparência de ferramenta enterprise

### 🐛 Correções
- Melhor formatação de números grandes
- Truncamento inteligente de nomes longos

---

## [2.2.0] - 2026-01-23

### ✨ Novas Funcionalidades

#### 🔑 Autenticação GitHub
- **Suporte a Personal Access Token**: Configure token para aumentar rate limit
  - Rate limit: 60 → 5000 requisições/hora (83x mais!)
  - Suporte via variável de ambiente `GITHUB_TOKEN`
  - Suporte via arquivo de configuração `~/.grc/config.json`
- **Comandos de configuração**:
  - `python app.py config set-token` - Configurar token
  - `python app.py config show-token` - Mostrar token (mascarado)
  - `python app.py config remove-token` - Remover token
  - `python app.py config status` - Ver status de autenticação
  - `python app.py auth-status` - Atalho para ver status
- **Feedback visual**: Mostra status de autenticação durante busca
  - 🔑 Autenticado: Sim (5000 req/hora)
  - ⚠️ Autenticado: Não (60 req/hora)
- **Armazenamento seguro**: Token salvo com permissões restritas (0600)

#### 🎨 Melhorias de UX
- **Estrutura de comandos**: Migrado para Click groups
  - `python app.py search` - Buscar repositórios
  - `python app.py config` - Gerenciar configurações
  - `python app.py auth-status` - Ver autenticação
- **Mensagens informativas**: Dicas sobre como configurar token
- **Validação de token**: Aviso se token não parece válido

### 🔧 Melhorias Técnicas
- **Headers de autenticação**: Requisições incluem token quando disponível
- **Detecção automática**: Busca token em múltiplas fontes (env, config)
- **Ordem de prioridade**: Variável de ambiente > Arquivo de configuração
- **Diretório de configuração**: `~/.grc/` criado automaticamente
- **Rate limit expandido**: Captura `X-RateLimit-Limit` dos headers

### 📚 Documentação
- **docs/AUTHENTICATION.md**: Guia completo sobre autenticação
  - Como criar token no GitHub
  - Métodos de configuração
  - Comandos disponíveis
  - Troubleshooting
  - Casos de uso (CI/CD, scripts, etc.)

### 🐛 Correções
- Melhor tratamento de erros de autenticação
- Mensagens mais claras sobre rate limit

---

## [2.1.0] - 2026-01-22

### ✨ Novas Funcionalidades

#### 📊 Progress Bars e Feedback Visual
- **Progress bar na coleta**: Barra de progresso visual durante a busca de repositórios
  - Mostra página atual / total
  - Tempo decorrido e estimado
  - Número de repositórios coletados
  - Tempo de resposta da API
- **Monitoramento de Rate Limit**: Exibe requisições restantes do GitHub API
  - Alerta quando poucas requisições restam (< 10)
  - Mostra quando rate limit é atingido
  - Exibe horário de reset do limite
- **Feedback de Cache**: Indicação visual ao carregar/salvar cache
  - Mensagem de sucesso ao encontrar cache
  - Indicação quando cache não existe
  - Contador de repositórios carregados
- **Feedback de Filtros**: Estatísticas de filtragem
  - Mostra quantidade antes/depois/removidos
  - Feedback visual para cada filtro aplicado
- **Feedback de Exportação**: Detalhes dos arquivos exportados
  - Nome do arquivo gerado
  - Número de repositórios exportados
  - Tamanho do arquivo em KB
- **Progress bar na escrita**: Para grandes volumes de dados
  - Barra de progresso ao escrever CSV
  - Indicação visual de conclusão

#### 🎨 Melhorias de UX
- **Informações iniciais**: Resumo da busca antes de iniciar
  - Linguagem selecionada
  - Número de páginas
  - Repositórios esperados (~30 por página)
- **Emojis contextuais**: Ícones para cada tipo de operação
  - 🔄 Coleta em andamento
  - ✅ Operação concluída
  - ⚠️ Avisos importantes
  - 💾 Operações de cache
  - 📄 Operações de arquivo
- **Cores organizadas**: Output colorido e estruturado
  - Verde para sucessos
  - Amarelo para avisos
  - Vermelho para erros
  - Cyan para informações

### 🔧 Melhorias Técnicas
- **Dependência tqdm**: Adicionada biblioteca para progress bars
- **Monitoramento de API**: Captura headers de rate limit
- **Delay entre requisições**: Pequeno delay (0.5s) para não sobrecarregar API
- **Tratamento de erros melhorado**: Mensagens mais claras para rate limit

### 📚 Documentação
- **docs/PROGRESS_BAR.md**: Guia completo sobre progress bars
  - Exemplos de uso
  - Detalhes técnicos
  - Comparação antes/depois
  - Troubleshooting

### 🐛 Correções
- Melhor tratamento de erro 403 (rate limit)
- Feedback mais claro quando não há repositórios para exportar

---

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
