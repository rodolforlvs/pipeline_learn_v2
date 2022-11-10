# Projeto de pipeline no Airflow
O projeto pipeline_learn_v2 foi feito com intuito de prover aprendizado sobre as técnicas de tratamento, manipulação e elaboração 
de tarefas com Python no Airflow dentro de um Docker compose.

# Criação das Tasks
Aplicadas técnicas de web scraping com python. Foram criadas funções para realizar a raspagem de dados referentes ao "Saldo de crédito pessoa jurídica por região", no 
site do Banco Central, retornando arquivos csv

As tasks foram divididas em camadas utilizando o conceito de data lake, onde ocorreram análises dos dados, tratamentos e manipulação, para que os 
mesmos fossem ajustados para estrutura do Airflow. 


## task_get_file
Objetivo -> Essa task possui duas funções específicas, criadas para acessar e baixar os dados no site. 

Funções -> baixar_csv | get_files

Bibliotecas utilizadas -> OS e REQUESTS

## task_bronze
Objetivo -> Realizar o primeiro tratamento dos dados sem alteração em sua estrutura. Feita normalização dos nomes das colunas existentes ('data': 'DATA', 
'valor': 'VALOR') utilizando o pandas e feita preparação para a próxima camada receber os arquivos em formato adequado para utilização no airflow.

Função -> move_bronze

Bibliotecas utilizadas -> OS e PANDAS

## task_silver
Objetivo -> Recebe os dados da camada bronze em formato (.parquet). Feita concatenação dos arquivos da camada bronze em um único arquivo. 
Criadas as colunas NR_ANO, NR_MES, NM_INDICADOR. Feita nova normalização dos nomes das colunas DATA e VALOR para DT_LANCAMENTO e VL_INDICADOR.

Função -> move_silver

Bibliotecas utilizadas -> OS, PANDAS e DATETIME

## task_gold
Objetivo -> Recebe o arquivo da camada silver em formato (.parquet). Criada a coluna NM_TRIMESTRE. Será feita
uma verificação na coluna NR_MES, nos meses 01, 04, 07 e 10 para que seja associado a cada um deles, um trimestre específico, de acordo com a regra do negócio.

Função -> move_gold

Bibliotecas utilizadas -> OS e PANDAS

# Subindo a aplicação no Docker compose e colocando as tasks no Airflow
## Subindo o airflow no docker-compose

Feita configuração com base na documentação do Airflow: 

https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html

## Configurando o Docker compose
![dc1](https://user-images.githubusercontent.com/108907292/201009319-f0a573ae-bdc5-4dcc-81ba-82b7153310e0.jpg)
![dc2](https://user-images.githubusercontent.com/108907292/201009329-1613eb99-ddf9-4bb2-869a-f4405a304506.jpg)

## Subindo o docker-compose

![image](https://user-images.githubusercontent.com/108907292/201006180-6bb8f810-40fe-4557-8b01-08b12ab5cc3d.png)

## Configurando a DAG
![dag1](https://user-images.githubusercontent.com/108907292/201008797-04119c0e-141c-46a5-965e-427ffc0caf33.jpg)
![dag2](https://user-images.githubusercontent.com/108907292/201008822-07c12454-a220-4703-949d-7fc95eab4c98.jpg)
![image](https://user-images.githubusercontent.com/108907292/201010011-973b63b8-d5f4-4070-accd-13f02b4a11d3.png)

## DAG no Airflow

IMAGEM
