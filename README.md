interview Backend : Boilerplate 
=====

[![Python 3.7](https://img.shields.io/badge/python-3.7-blue.svg)](https://www.python.org/downloads/release/python-370/)
[![Django 3.0](https://img.shields.io/badge/django%20versions-3.0-blue.svg)](https://docs.djangoproject.com/en/3.0/releases/2.7/)

All developers need to follow this project structure whenever they are working on existing or a new project
from scratch. 


Project Layout
------------

```
|-- README.md
|-- api
|   |-- __init__.py
|   |-- urls.py
|   `-- v1
|       |-- __init__.py
|       |-- urls.py
|       `-- user
|           |-- __init__.py
|           |-- serializers.py
|           |-- urls.py
|           |-- validators.py
|           `-- views.py
|-- archive_files
|   `-- zips
|-- core
|   |-- __init__.py
|   |-- admin.py
|   |-- apps.py
|   |-- management
|   |   |-- __init__.py
|   |   `-- commands
|   |       |-- __init__.py
|   |       `-- create_new_users.py
|   |-- migrations
|   |   `-- __init__.py
|   |-- models.py
|   |-- tests.py
|   `-- views.py
|-- logs
|-- manage.py
|-- requirements
|   |-- base.txt
|   |-- dev.txt
|   |-- prod.txt
|   `-- stage.txt
|-- interview
|   |-- __init__.py
|   |-- asgi.py
|   |-- base.py
|   |-- settings
|   |   |-- __init__.py
|   |   |-- dev.py
|   |   |-- prod.py
|   |   `-- stage.py
|   |-- urls.py
|   |-- utilities
|   |   |-- __init__.py
|   |   `-- env_config.py
|   `-- wsgi.py
`-- templates

```

Dependencies
------------

* [Python] - Python is an interpreted, high-level, general-purpose programming language.
   
   [Python]: <https://www.python.org/>
   
   
* [PyEnv] - (***Optional***) pyenv lets you easily switch between multiple versions of Python. It's simple, unobtrusive, and follows the UNIX tradition of single-purpose tools that do one thing well.
   
   [PyEnv]: <https://github.com/pyenv/pyenv>
   

Installing Project Dependencies
--------------------------

After successfully installing Python 3.7 and activating your virutal environment.

- Move inside the project
- Run the command given below

-  ***Dev*** : ```pip install -r requirements/dev.txt```
- ***Production*** : ```pip install -r requirements/production.txt```
 
<br>

### Environment File

After project setup create a  ***.env*** file inside the project root. 
* Make sure ***.env*** file should not be tracked by ***Git*** or any other ***version control***.

* ***.env*** file variable values can be changed based on the developer preference.
* Below have a look over the sample ***.env*** file used in the local development server.

<br>

```
DEBUG=True

DB_NAME=interview
DB_USERNAME=root
DB_PASSWORD=interview123
DB_HOST=localhost
DB_PORT=3306


REDIS_HOST=localhost
REDIS_DB=1
REDIS_PORT=6379

RQ_TIMEOUT=3600
RQ_RESULT_TTL=3600
RQ_DEFAULT_JOB_EXEC_TIMEOUT=1h
RQ_WORKER_TTL=50


DJANGO_SECRET_KEY=n&(0k+j$2av*)r7htz(4g0@g18$u^+jgtdpwm-m_e71mvdf+yi
DJANGO_SETTINGS_MODULE=interview.settings.dev

SHARED_DRIVE_TYPE=LINUX
LINUX_SHARE_PATH=/home/interview/Downloads/custom_folder


SAMBA_SHARE_NAME=interview
SAMBA_USER_NAME=interview
SAMBA_PASSWORD=interviewai
SAMBA_LOCAL_MACHINE_NAME=laptop
SAMBA_SERVER_MACHINE_NAME=DESKTOP-E721EDG
SAMBA_SERVER_IP=192.168.0.100


ALLOWED_HOSTS=*, interview.ai, localhost
```


### Running Django Server
<br>

***Local Environment***
``` 
$ python manage.py runserver --settings=interview.settings.dev <port_number>
```

***Staging Environment***

``` 
$ python manage.py runserver --settings=interview.settings.stage <port_number>
```

***Production Environment***
``` 
$ python manage.py runserver --settings=interview.settings.prod <port_number>
```
<br>

### Migrating DB Changes in Database

* This is recommended before starting the server for first time.
* Migration files alters database schema by creating/updating/removing tables.
* Note: We recommend MySQL/Postgres/Oracle for dev/production servers.

``` 
$ python manage.py migrate --settings=interview.settings.(dev|stage|prod)
```



* If you create new models then you need write this command:

```
$ python manage.py makemigrations --settings=interview.settings.(dev|stage|prod)
```


#### Setting Up New Users

* This command will create dummy users.

```
$ python manage.py create_new_users --settings=interview.settings.(dev|stage|prod)
```

* To create an **superuser account**, use this command::

```
$ python manage.py createsuperuser --settings=interview.settings.(dev|stage|prod)
```

### Deployment Information

* This information is for the DevOps Team.

* Change the ***SECRET_KEY*** while deploying in production/staging servers.
* To generate a new ***SECRET_KEY*** run the below given command.

```
$ python manage.py djecrety --settings=interview.settings.(dev|stage|prod)
```

* ***Recommendation***:
	1. Keep it safe.
	2. Change the secret key on your deploy to prod servers.
	3. If you lost the secret key for any reason or
	   the server got compromised change it as soon as possible.
	   
<br>

MySQL Instructions
---------------------

- For working with MySQL you need to install system specific dependencies.
- Below given example works fine with Ubuntu 18.04 LTS
```
# Debian / Ubuntu

sudo apt-get install python3-dev
sudo apt-get install libmysqlclient-dev 
sudo apt-get install libssl-dev

```
- Python Package
```
pip install mysqlclient
```

API Docs
--------
 - Our API Docs gets updated frequently. 
 -  URL : http://localhost:8000/api/docs/
 
*** Port 8000 and localhost are just for reference. ***


