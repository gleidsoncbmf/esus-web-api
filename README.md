# esus-web-api
- Docker Api Flask Restfull + Postgres para consulta de dados de Saúde 
## Requisitos para Inicialização da Aplicação
- É necessário ter o Docker e Docker-Compose instalados na sua máquina.

## Verifique se você os têm instalados em sua máquina com os seguintes comandos:

-     docker --version

-     docker-compose --version

## Para este projeto foram utilizadas as seguintes versões:

- `Docker version 26.0.0, build 2ae903e`

- `Docker Compose version v2.26.1-desktop.1`

   - É nessário ter atenção as versões para evitar erros durante a execução, por exemplo, em versões mais antigas é necessário definir a 'version' no arquivo docker-compose.yml, além de não aceitar algumas defnições como 'name'. Dessa forma, se possível, obter as mesmas versões utilizadas nessa aplicação, ou ter uma atenção caso seja necessário definir a 'version' e remover o 'name' para versões mais antigas. Lembrando que nesse caso o nome do containner será alterado para outro padrão, sendo necessário o comando `docker ps` para verificar o nome e usar o nome ou id do containner na execução dos comandos para a Carga no Banco de Dados.      

## Verifique a instalação adequada para o seu Sistema seguindo a documentação oficial:

-     https://docs.docker.com/get-docker/ 

-     https://docs.docker.com/compose/install/

# Incializando a aplicação:

## Com o Docker e Docker-compose instalados, abra o terminal na pasta do projeto e execute o seguinte comando:

-     docker-compose up -d

Quando esse comando é executado, ele realiza o build da aplicação caso ainda não tenha sido construída e também sobe os containers em background. Após a finalização, a aplicação estará disponível em `http://localhost:8001/api/v1/`

# Carga no Banco de Dados(Primeira Inicialização)

### Caso seja a primeira inicialização da aplicação, será necessário realizar a carga no banco de dados, para isso execute os seguintes comandos:

-     docker exec esus-web-api-1 flask db init

-     docker exec esus-web-api-1 flask db migrate

-     docker exec esus-web-api-1 flask db upgrade

-     docker exec esus-web-api-1 flask api load-csv

   - Caso tenha utilizado versões mais antigas do docker e docker-compose, verificar o nome ou id do containner utilizando o comando `docker ps`. Substitua o nome ou o id no lugar de `esus-web-api-1 ` na execução dos comandos.
   - Por exemplo:
      -  `docker exec id-ou-nome-do-containner-aqui flask db init `

O docker exec faz com que os comandos sejam executados dentro do terminal do prórprio container, o "flask api load-csv" é um custom command para ler o arquivo csv, organizar os cabeçalho das colunas, formatar as datas para o padrão YYYY-mm-dd e em seguida injetar os dados formatados do csv na base de dados pgdata, do Postgres.

# Utilizando a Aplicação:

## Após isso, a aplicação estará disponível para ser utilizada com os filtros de busca. Aqui estão alguns exemplos de consultas que você pode utilizar:

- `http://localhost:8001/api/v1/atendimentos`

   - Retorna todos os atendimentos

- `http://localhost:8001/api/v1/atendimentos?data_atendimento=2023-12-19&condicao_saude=diabetes`
  
   - Retorna os atendimentos para diabetes na data 2023-12-19

- `http://localhost:8001/api/v1/atendimentos?condicao_saude=hipertensao&data_atendimento=2024-01-08&unidade=Daniela`
  
   - Retorna os atendimentos para hipertensao na data 2024-01-08, na unidade de saude Daniela

### Dessa forma, você pode combinar os filtros de acordo com a sua necessidade.



 
