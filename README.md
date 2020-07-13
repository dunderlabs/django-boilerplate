# Django boilerplate #

Django boilerplate to start new projects. Based on [7ws logfreak project](https://github.com/7ws/logfreak).

What this boilerplate is using?
-------------------------------

- Python +3.6
- Django 3.0.8
- Pytest
- Bower
- Poetry

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
