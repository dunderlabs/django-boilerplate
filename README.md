# Turbo Send Email #

Web application to send mails in a turbo speed.


## Instructions

### Requirements

- Linux/MacOS
- Git
- Python 3.6

### Instalation

Run the following commands on your terminal:

```bash
$ git clone git@github.com:mazulo/turbo_send_mail.git
$ cd turbo_send_mail
$ pip install -r requirements.txt
$ python manage.py migrate
```

and then...

### Run the server

```bash
$ ./manage.py runserver
Performing system checks...

System check identified no issues (0 silenced).
Django version 1.10.5, using settings 'settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

### How to use

You can use it by access `http://127.0.0.1:8000/`

### Tests

To run the tests:

```bash
python manage.py test backend
```
