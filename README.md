# Django boilerplate #

English version [here](README-EN.md)

Um template de projeto Django para ajudar você a iniciar novos projetos. Baseado no [7ws logfreak](https://github.com/7ws/logfreak).

Na era das aplicações web usando React/APIs RESTful, nós ainda acreditamos que um projeto Django "raiz" tem seu valor. Principalmente se você só precisa validar uma ideia, ou simplesmente prefere não usar aquelas ferramentas. Tendo isso em mente, nós criamos essa estrutura (vamos chamar de boilerplate) que vai servir de template para um novo projeto Django, adicionando algumas _melhorias_.

O que esse boilerplate está usando?
-------------------------------

- Python +3.6
- Django 3.0.8
- [Pytest](https://docs.pytest.org/en/stable/) - Vai nos ajudar a escrever testes (e rodá-los)
- [Bower](https://bower.io/) - Um gerenciador de pacotes para o frontend
- [Poetry](https://python-poetry.org/) - Gerenciador de pacotes Python
- [Bootstrap 4.5](https://getbootstrap.com/docs/4.5/getting-started/introduction/) -  Um dos mais populares frameworks CSS

O que vem por aí:
-----------------
- [ ] [mypy](http://mypy-lang.org/)
- [ ] Configurar ambiente Docker para produção
- [ ] Finalizar configuração do Heroku

Como utilizar - sem docker
---------------------------

Primeiro, você vai precisar instalar o `Django`, para que assim possamos utilizar o comando `django-admin`. Então ative seu ambiente virtual e rode `pip install Django==3.0.8`. Ao finalizar a instalação, dentro do diretório onde você quer que o projeto fique, rode o seguinte comando:

```bash
$ django-admin startproject nome_do_projeto --template=https://github.com/dunderlabs/django-boilerplate/archive/master.zip
```

Depois disso, todos os arquivos desse repositório estarão dentro do diretório que você criou antes e executou o comando anterior. Agora nós precisamos instalar as dependências Python do projeto. Para isso, você pode executar esse comando abaixo:

```bash
$ make install-requirements
```

Se em algum momento você quiser atualizar os pacotes Python, execute o seguinte:

```bash
$ make update-requirements
```

Agora por último mas não menos importante, vamos instalar as dependências do frontend:

```bash
$ make setup-frontend
```

Rodando os testes:
------------------

Pra rodar os testes vai ser tão simples quanto o seguinte:

```bash
$ make test
```

Como usar - com docker
------------------------

Primeiro certifique-se que tem [Docker](https://docs.docker.com/) e [Docker Compose](https://docs.docker.com/compose/) instalados na sua máquina. Depois disso, como primeiro passo vamos fazer o `build` do projeto, aonde ele vai baixar as imagens docker e executar todos os comandos necessários. Para isso, execute o comando:

```bash
docker-compose build
```

Nós também criamos um atalho para evitar que você sempre tenha que digitar `docker-compose run --rm backend` quando precisar executar algum comando dentro do container. Então, caso você queira executar um `python manage.py migrate` dentro do container, você roda o seguinte:
```bash
./bin/run python manage.py migrate
```

Se você rodar apenas `./bin/run` ele vai executar o servidor de desenvolvimento do Django.

Como contribuir?
----------------

Reporte os bugs nas nossas [issues](https://github.com/dunderlabs/django-boilerplate/issues) ou simplesmente faça um fork do projeto, contribua com o que achar necessário e mande um PR pra gente! :)