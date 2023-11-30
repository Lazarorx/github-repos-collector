# github-repos-collector

Este código coleta informações sobre repositórios no GitHub. Ele pode ser usado para coletar repositórios de qualquer tipo, incluindo repositórios de linguagem, IA, machine learning, back-end, front-end e outros.

O código é dividido em quatro módulos principais:

* converter_data() e formatar_data(): Esses módulos convertem strings de data para objetos datetime e vice-versa.
* exibir_info_repositorio(): Esse módulo exibe informações formatadas de um repositório.
* coletar_repositorios(): Esse módulo coleta informações sobre repositórios.
* main(): Esse módulo é o ponto de entrada do código. Ele coleta informações sobre repositórios e exibe essas informações.

**Configuração do logging**

O código usa o módulo `logging` para registrar mensagens de log. O nível de registro padrão é `INFO`, o que significa que apenas mensagens informativas serão registradas.

**Função `converter_data()`**

A função `converter_data()` converte uma string de data para um objeto datetime. A string de data deve estar no formato `YYYY-MM-DDTHH:mm:ssZ`.

**Função `formatar_data()`**

A função `formatar_data()` converte um objeto datetime em uma string mais legível. A string retornada está no formato `YYYY-MM-DD HH:mm:ss`.

**Função `exibir_info_repositorio()`**

A função `exibir_info_repositorio()` exibe informações formatadas de um repositório. As informações exibidas são:

* Nome do repositório
* Número de estrelas
* Número de forks
* Link para o repositório
* Data de criação
* Data de atualização

**Função `coletar_repositorios()`**

A função `coletar_repositorios()` coleta informações sobre repositórios. A função recebe dois parâmetros:

* `config`: Um dicionário que contém configurações específicas para o tipo de repositório.
* `num_paginas`: O número de páginas a serem consultadas.

A função faz uma solicitação HTTP para a API do GitHub. A resposta da API é convertida para formato JSON. A função itera sobre os repositórios no JSON e armazena as informações de cada repositório em uma lista.

**Função `main()`**

A função `main()` é o ponto de entrada do código. Ela recebe quatro parâmetros:

* `tipo_repositorio`: O tipo de repositório no GitHub.
* `ordenacao`: O critério de ordenação dos repositórios.
* `linguagem`: A linguagem de programação desejada.
* `num_paginas`: O número de páginas a serem consultadas.

A função configura as opções de acordo com os parâmetros recebidos. Em seguida, ela chama a função `coletar_repositorios()` para coletar informações sobre os repositórios. Por fim, ela chama a função `exibir_info_repositorio()` para exibir as informações dos repositórios.

**Exemplo de uso**

Para usar o código, você pode executar o seguinte comando:

```
python coletar_repositorios.py --tipo-repositorio=linguagem --ordenacao=stars --linguagem=python
```

Este comando coletará informações sobre os repositórios Python mais populares no GitHub. As informações serão exibidas no console.

**Outras opções**

O código pode ser modificado para coletar informações sobre outros tipos de repositórios. Para isso, você precisará alterar o valor do parâmetro `tipo_repositorio`.

O código também pode ser modificado para personalizar a ordenação dos repositórios. Para isso, você precisará alterar o valor do parâmetro `ordenacao`. As opções disponíveis são:

* `stars`: Ordena os repositórios pelo número de estrelas.
* `forks`: Ordena os repositórios pelo número de forks.
* `updated`: Ordena os repositórios pela data de atualização.

Você também pode alterar o número de páginas a serem consultadas. Para isso, você precisará alterar o valor do parâmetro `num_paginas`.

**Cache**
Os resultados da busca são armazenados em cache no arquivo cache_repositorios.json para evitar chamadas frequentes à API do GitHub.

**Contribuição**
Contribuições são bem-vindas! Sinta-se à vontade para abrir (issues) e enviar pull requests para melhorar este projeto.

