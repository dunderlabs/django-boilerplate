# Django boilerplate #

Django boilerplate to start new projects. Based on [7ws logfreak project](https://github.com/7ws/logfreak).

In the age of web application using React and stuff, we still believe that there is good use cases for a "bare metal" Django project. So with that in mind, we created this boilerplate which uses a basic Django structure with some _tweaks_.

What this boilerplate is using?
-------------------------------

- Python +3.6
- Django 3.0.8
- [Pytest](https://docs.pytest.org/en/stable/) - Helps you write better programs
- [Bower](https://bower.io/) - A package manager for the frontend
- [Poetry](https://python-poetry.org/) - Python packaging and dependency management
- [Bootstrap 4.5](https://getbootstrap.com/docs/4.5/getting-started/introduction/) -  the world’s most popular framework

What is next?
-------------
- [ ] [mypy](http://mypy-lang.org/)
- [ ] [Black](https://black.readthedocs.io/en/stable/)
- [ ] Set up Docker for production
- [ ] Finish Heroku setup

How to use - without docker
---------------------------

First you will need to install `Django` so that you have the `django-admin` command available. Activate your virtual env and run `pip install Django==3.0.8`. Now inside the directory where your project will live, run the following command:

```bash
$ django-admin startproject project_name --template=https://github.com/dunderlabs/django-boilerplate/archive/master.zip
```

After that, all the files from this repo will be inside the directory you created previously. Now to fully install all the requirements, you can just run:

```bash
$ make install-requirements
```

If you want to update your requirements, this is the command:

```bash
$ make update-requirements
```

Now las but not least, install the frontend dependencies with:

```bash
$ make setup-frontend
```

Running the tests
------------------

It's as easy as just:

```bash
$ make test
```

How to use - with docker
------------------------
Firstly make sure you have [Docker](https://docs.docker.com/) and [Docker Compose](https://docs.docker.com/compose/) installed on your machine. To build it run `docker-compose build` and when it is finished, you will be ready to run the project. We also created a shortcut in `bin/run` that you can use to run commands. For example:

- To run `migrate`: `./bin/run python manage.py migrate`

If you just run `./bin/run` it will start the development project server.

How to contribute?
----------------

Report bugs in our [issues](https://github.com/dunderlabs/django-boilerplate/issues) or just fork this project and submit a PR with improvements! :smiley: