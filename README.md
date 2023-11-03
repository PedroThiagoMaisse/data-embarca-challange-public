---

# Desafio AWS Step Functions com Serverless Framework e S3

Bem-vindo(a) ao desafio de orquestração de microserviços usando AWS Step Functions, Lambdas e S3. Aqui, você usará o Serverless Framework e Python para criar e gerenciar seus recursos AWS.



## Objetivo

O desafio envolve a criação de um fluxo orquestrado por uma state machine no qual:

1. **Lambda 1:** Esta função deve buscar um arquivo JSON de um bucket S3, ler seu conteúdo e realizar alguma transformação ou tratamento nos dados.
2. **Lambda 2:** Esta função deve pegar o resultado tratado pelo Lambda 1 e salvar em formato CSV no mesmo bucket S3 (ou em um diferente, se preferir).

O `serverless.yml` fornecido já estabelece a estrutura da state machine e das lambdas. Seu desafio é implementar a lógica dentro de cada lambda e garantir a passagem de dados entre elas através da state machine.

### Requisitos

1. **Lambda 1**:
   - Deve ser capaz de receber um identificador de arquivo (por exemplo, o nome do arquivo) como entrada.
   - Busque o arquivo JSON no bucket S3 utilizando o identificador.
   - Transforme ou trate os dados conforme necessário.
   - Retorne os dados tratados.

2. **Lambda 2**:
   - Receba os dados tratados do Lambda 1.
   - Salve os dados em formato CSV no bucket S3.

### Formato de Saída

Para a saída gerada pela segunda lambda, esperamos um arquivo CSV que cumpra as seguintes especificações:

1. **Nome do Arquivo**:
   - O arquivo deve ter o nome no formato `processed_data_NOME_DO_CANDIDATO.csv`, onde `NOME_DO_CANDIDATO` deve ser substituído pelo seu nome completo sem espaços (por exemplo, `processed_data_JoaoSilva.csv`).

2. **Colunas**:
   - 'created_at', 'origin_id', 'destination_id', 'date', 'operator_id', 'white_label_request', 'channel', 'operator_name', 'is_mobile', 'numberOfOptions', 'origin_name', 'destination_name'

3. **Dados**:
   - Todos os dados do CSV devem ser extraídos de um arquivo `.json` cujo nome será fornecido junto com as credenciais e identificação dos recursos.



#### **Desenvolvimento**:

1. Baseado no `serverless.yml` fornecido, escreva o código Python para ambas as lambdas seguindo os requisitos.
2. Certifique-se de que a state machine esteja corretamente

 configurada para passar os dados entre os Lambdas.

#### **Deploy**:

1. Use o Serverless Framework para realizar o deploy dos recursos na AWS.

#### **Testes**:

1. Crie e carregue um arquivo JSON teste no bucket S3.
2. Use a função Python fornecida para iniciar a state machine.
3. Verifique se o CSV foi gerado corretamente no bucket.

### Envio

1. Crie um novo repositório em sua conta GitHub.
2. Faça push do seu código para este repositório.
3. Envie o link do repositório para a equipe avaliadora.

## Critérios de Avaliação

1. **Código**: Qualidade, clareza e eficiência.
2. **Integração com S3**: As lambdas devem interagir corretamente com o S3.
3. **Fluxo Orquestrado**: A state machine deve garantir a passagem correta de dados entre os Lambdas.
4. **Documentação**: Quaisquer suposições ou alterações feitas devem ser bem documentadas.



## Bônus de Avaliação

A implementação de um pipeline de integração contínua e entrega contínua (CI/CD) utilizando o GitHub Actions **não é obrigatória**, mas será considerada um extra positivo na avaliação. Se decidir implementar este aspecto, assegure-se de documentar o fluxo do pipeline, as ações tomadas em cada etapa e qualquer outro detalhe relevante que possa facilitar a compreensão e revisão do seu trabalho.

