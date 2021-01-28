# BPGL

Django based website

## Requirements
Python 2.7.19

Packages from *requirements.txt*: `pip install -r requirements.txt`

## Virtualenv

Install virtualenv: `pip install virtualenvwrapper-win`

Create virtualenv: `mkvirtualenv bpgl_env`

Run env: `workon bpgl_env`

## Run project

Run `python manage.py runserver` inside virtualenv (*bpgl_env*)

Go to: `http://127.0.0.1:8000/`

## Database

Export: `pg_dump -Fc -v --host=host --username=prodname --dbname=prodname -f dump.sql`

Import: `pg_restore -v --no-owner --host=host --port=port --username=devname --dbname=devname dump.sql`

## Other info
**Dev environement**: *dev* branch connected to dev database

**Production environement**: *master* branch connected to production database

**SSL:** set `SECURE_SSL_REDIRECT = False` in *settings.py* for local development

**Encoding issues in python 2**:

import: `from django.utils.encoding import python_2_unicode_compatible`

and use decorators before classes in *models.py*: `@python_2_unicode_compatible`

