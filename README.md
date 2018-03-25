# Django boilerplate #

Django boilerplate to start new projects. Based on [7ws logfreak project](https://github.com/7ws/logfreak).

## Requirements

- Python +3.5
- Django 1.1x
- bower

## How to use

Inside the directory your project will live, run the following command:

```shell
$ django-admin startproject project_name --template=https://github.com/dunderlabs/django-boilerplate/archive/master.zip
```

After that the following command will update requirements/\*.txt with latest packages from requirements/\*.in:

```shell
$ make pip-compile
```

The next command will install requirements for a local development environment:

```shell
$ make install-dev-requirements
```

After all, just install the frontend dependencies with:

```shell
$ make setup-frontend
```

## Running the tests

Make sure that you have the Firefox and the [geckodriver](https://github.com/mozilla/geckodriver/releases) installed on your machine.

To execute the default tests, enter on the project root and run the following command:

```shell
$ python manage.py test/backend/core/tests
```
