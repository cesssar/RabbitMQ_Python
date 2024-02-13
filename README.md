# RabbitMQ com Python e Docker

> Utiliza Docker para executar uma instância do RabbitMQ e bibliotecas em Python para enviar e receber mensagens

<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
<img src="https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white" />

## 💻 Pré-requisitos

Python 3.10 (testado nesta versão)
Docker 

## 🚀 Preparando ambiente para execução

Preferencialmente criar um ambiente virtual para instalar as bibiliotecas isoladamente do resto do sistema operacional.

```
python -m venv venv
```
Consulte como criar e ativar em: https://docs.python.org/pt-br/3/tutorial/venv.html
Instalar as bibliotecas necessárias para execução do projeto:

```
pip install -r requirements.txt
```

## 🚀 Executando o RabbitMQ

```
docker-compose up -d 

```

## 🚀 Iniciando os robôs que recebem mensagens

```
python recebe.py

```

## 🚀 Enviando mensagem para todas as filas (queue)

```
python envia.py

```