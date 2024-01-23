# Aplicativo de Lista de Tarefas com Django e htmx 

![To-Do List Screenshot](screenshot.png)

Este é um aplicativo simples de Lista de Tarefas construído usando o framework web Django e a biblioteca htmx para uma interação dinâmica entre cliente e servidor. O aplicativo permite aos usuários gerenciar suas tarefas de forma dinâmica, sem a necessidade de código JavaScript complexo.

## Teste o código usando esse link.
https://web-wine-iota.vercel.app/
* Hospedagem de aplicação na **Vercel** e banco de dados **ElephantSQL**.
* Para instação na sua maquina via LocalHost siga o Tutorial abaixo.

## Preparando o Ambiente e Rodando o Aplicativo
Siga as instruções abaixo para configurar o ambiente e executar o aplicativo Lista de Tarefas em sua máquina local.

## Pré-requisitos
Certifique-se de ter os seguintes pré-requisitos instalados em sua máquina:

- Python (versão 3.6 ou superior)
- pip (gerenciador de pacotes do Python)

- Compreensão básica de Python e do Framework Django.
- Familiaridade com o Django e seus conceitos.
[Nota: Use um ambiente virtual para a melhor prática. 👍]

## Passos
### 1. Instalação do Python
Baixe o instalador do Python para Windows no site oficial: Python Downloads.
Execute o instalador e certifique-se de marcar a opção "Add Python to PATH" durante a instalação.
Clique em "Install Now" para iniciar a instalação.

### 2. Instalação do pip
O pip é o gerenciador de pacotes do Python e geralmente é instalado automaticamente com o Python. Para verificar se você o tem instalado, execute:
``` python
pip --version
```
### 3. Instalação do Django
Com o Python e o pip instalados, você pode instalar o Django usando o seguinte comando:
``` python
pip install django
```
Certifique-se de verificar a versão do Django instalada:
``` python
django-admin --version
```
## Configurando o Ambiente e Executando o Aplicativo
1. Clone o Repositório:
   
```
git clone <https://github.com/stephenbarreto/WEB.git>
```
2. Abra o Projeto no VSCode:
 ``` python
cd myproject
```
3. Crie um Ambiente Virtual:
 ``` python
python -m venv venv
```
4. Ative o Ambiente Virtual:
 ``` python
.\venv\Scripts\Activate
```
5. Instale as Dependências:
 ``` python
pip install -r requirements.txt
```
6. Aplique as Migrações:
 ``` python
python manage.py makemigrations
```
 ``` python
python manage.py migrate
```
7. Execute o Servidor de Desenvolvimento:
   
 ``` python
python manage.py runserver
```

8. Acesse o Aplicativo:
   
```
Abra seu navegador e visite http://127.0.0.1:8000/ para interagir com o aplicativo Lista de Tarefas.
```

## Importante caso for usar ele em localhost altere as configuções do DATABASE em settings.py como no print logo a seguir.

![To-Do List Screenshot](screenshot-DataBase.png)

- após fazer a edição não esqueça de dar o comando
  
  ```python
python manage.py migrate
```
Para atualizar o projeto com o novo banco de dados



## Contribuição
Contribuições são bem-vindas! Siga as diretrizes de contribuição do projeto.

## Licença
Este projeto está licenciado sob a Licença MIT. Consulte o arquivo LICENSE para obter detalhes.

##Contato
Se você tiver dúvidas ou precisar de ajuda, entre em contato conosco em stephendias@hotmail.com.br.

Referências
- Livro
  **Django de A a Z**.
  
Crie aplicações web rápidas, seguras e escaláveis com Python.

https://www.casadocodigo.com.br/products/livro-django-a-z
https://markdown.net.br/sintaxe-basica/
https://medium.com/@devsumitg/simple-todo-list-app-in-django-framework-htmx-bootstrap-5-8b68cbd47a1a
https://youtu.be/I5x8lAVQ8QQ?si=z2IKMTVuMOeAjH3d

  






