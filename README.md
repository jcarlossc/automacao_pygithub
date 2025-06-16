# AUTOMAÇÃO COM MÓDULO PYGITHUB.
Estudo sobre automação com uso do módulo pyGithub da linguagem de programação Python.

Este é um projeto simples que, com a utilização do módulo pyGithub, implementa uma classe com métodos para manipulação da plataforma Github através de um token:
* Listar repositórios
* Criar repositório
* Criar um arquivo README
* Criar arquivo gitignore
* Excluir repositório



Venv: ambiente virtual em Python isola dependências do projeto, evitando conflitos com pacotes globais do sistema. Ele permite que cada projeto tenha suas próprias bibliotecas e versões específicas.

## Ferramentas utilizadas:
* Linguagem de programação Python 3.9.13
* Ambiente virtual VENV
* Módulo pyGithub
* Git/GitHub
* Visual studio code
* Windows 10

## Requisitos:
* Python 3.x
* Módulo pyGithub
* Token da plataforma Github

## Modo de utilizar: 
* Clonar repositório.
* Acessar o diretório ```'cd automacao_pygithub```.
* Executar ```python -m venv venv``` para instalar o ambiente virtual.
* Executar, caso esteja no Windows, ```venv\Scripts\activate``` para iniciar o ambiente. Caso Linux ou MacOS, ```source venv/bin/activate```.
* Executar ```pip install -r requirements.txt``` para instalar a dependência.
* ```python app.py``` - Executa o algoritmo.
* Para sair do ambiente virtual ```deactivate```.

## Contribuição:
Se quiser contribuir para este projeto, fique à vontade para enviar um pull request ou relatar problemas na seção de issues.

## Licença:
Este projeto é licenciado sob a Licença MIT.

## Comandos importantes
* ```python -m venv venv``` - Cria um ambiente virtual chamado venv. Observação: o primeiro venv é o comando, o segundo, o nome do diretório.
* No Windows, ```venv\Scripts\activate``` e no Linux, ```source venv/bin/activate``` - Inicializa o ambiente.
* ```deactivate``` - Encerra o ambiente.
* ```pip freeze > requirements.txt``` - Gera o arquivo para instalação de dependências. Esse mesmo comando atualiza o arquivo quando uma dependência for instalada.
* ```pip list``` - Lista as dependências do projeto.
* ```pip show``` - Inserindo o nome da dependência após o comando, lista informações da dependência.
* ```pip install -r requirements.txt``` - Instala dependências que estão no arquivo 'requirements.txt'.
* ```pip install``` - Inserindo o nome da dependência após o comando, instala dependências.
* ```pip uninstall``` - Inserindo o nome da dependência após o comando, desinstala dependências.