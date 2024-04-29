# esus-web-api
Docker Api Flask Restfull + Postgres para consulta de dados de Saúde 
## Requisitos para Inicialização da Aplicação
A Aplicação utiliza Docker e Docker-Compose:

## Verifique se você os têm istalados em sua máquina com os seguintes comandos:

docker --version

docker-compose --version

## Para este projeto foram utilizadas as seguintes versões:

Docker version 26.0.0, build 2ae903e

Docker Compose version v2.26.1-desktop.1

## Verifique a instalação adequada para o seu Sistema seguindo a documentação oficial:

https://docs.docker.com/get-docker/ 

https://docs.docker.com/compose/install/

# Incializando a aplicação:

## Com o Docker e Docker-compose instalados, abra o terminal na pasta do projeto e execute o seguinte comando:

docker-compose up -d

Quando esse comando é executado, ele realiza o build da aplicação caso ainda não tenha sido construída e também sobe os containers em background. Após a finalização, a aplicação estará disponível em http://localhost:8001/api/v1/

## Carga no Banco de Dados(Primeira Inicialização)

### Caso seja a primeira inicialização da aplicação, será necessário realizar a carga no banco de dados, para isso execute os seguintes comandos:

docker exec esus-web-api-1 flask db init

docker exec esus-web-api-1 flask db migrate

docker exec esus-web-api-1 flask db upgrade

docker exec esus-web-api-1 flask atendimento load-csv

O docker exec faz com que os comandos sejam executados dentro do terminal do prórprio container, o "flask atendimento load-csv" é um custom command para ler o arquivo csv, organizar cabeçalho das duas primeiras colunas, formatar as datas para o padrão YYYY-mm-dd e em seguida injetar os dados formatados do csv no banco de dados pgdata, do Postgres.

# Utilizando a Aplicação:

## Após isso, a aplicação estará disponível para ser utilizada com os filtros de busca. Aqui estão alguns exemplos de consultas que você pode utilizar:

http://localhost:8001/api/v1/atendimentos  :  retorna todos os atendimentos

http://localhost:8001/api/v1/atendimentos?data_atendimento=2023-12-19&condicao_saude=diabetes  :  retorna os atendimentos para diabetes na data de 2023-12-19

http://localhost:8001/api/v1/atendimentos?condicao_saude=hipertensao&data_atendimento=2024-01-08&unidade=Daniela  :  retorna os atendimentos para hipertensao na data de 2024-01-08, na unidade de saude Daniela.

Dessa forma, você pode combinar os filtros de acordo com a sua necessidade.



 
