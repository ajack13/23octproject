interview Backend : 
=====
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
|       `-- email
|           |-- __init__.py
|           |-- serializers.py
|           |-- urls.py
|           |-- validators.py
|           |-- helpers.py
|           `-- views.py
|   |-- models
|   |-- migrations
|-- archive_files
|-- logs
|-- manage.py
|-- requirements
|   |-- base.txt
|   |-- dev.txt
|   |-- prod.txt
|-- interview
|   |-- __init__.py
|   |-- asgi.py
|   |-- base.py
|   |-- settings
|   |   |-- __init__.py
|   |   |-- dev.py
|   |   |-- prod.py
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


### Environment File

* ***.env*** file variable values can be changed based on the developer preference.
* Below have a look over the sample ***.env*** file used in the local development server.
* add your username and password in env file to setup email service

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

EMAIL_HOST_USER = <enter gmail email>
EMAIL_HOST_PASSWORD = <enter gmail password>

DJANGO_SECRET_KEY=n&(0k+j$2av*)r7htz(4g0@g18$u^+jgtdpwm-m_e71mvdf+yi
DJANGO_SETTINGS_MODULE=interview.settings.dev

SHARED_DRIVE_TYPE=LINUX
LINUX_SHARE_PATH=/home/interview/Downloads/custom_folder

ALLOWED_HOSTS=*, localhost


```


### Running Django Server
<br>

***Local Environment***
``` 
$ python manage.py runserver --settings=interview.settings.dev 8000
```

### Migrating DB Changes in Database

* This is recommended before starting the server for first time.
* Migration files alters database schema by creating/updating/removing tables.
* Note: We recommend MySQL/Postgres/Oracle for dev/production servers.

``` 
$ python manage.py migrate --settings=interview.settings.dev
```



* If you create new models then you need write this command:

```
$ python manage.py makemigrations --settings=interview.settings.dev
```


#### Setting Up New Users

* To create an **superuser account**, use this command::
```
$ python manage.py createsuperuser --settings=interview.settings.dev
```

MySQL Instructions
---------------------

- For working with MySQL you need to install system specific dependencies.
- Below given example works fine with Ubuntu 18.04 LTS

*** Setup ELK for logging
-------------------------
```
Setup filebeat to capture logs from files.

https://www.elastic.co/guide/en/beats/filebeat/7.9/filebeat-installation-configuration.html
```

*** Setup automated email
--------------------------
- Use cron to setup up automated Jobs every 10 mins
```
crontab -e
 m h  dom mon dow   command
 */10 * * * *      /home/laptop/.pyenv/shims/python /path_to_project/send_automated_email_cron.py
save and exit
sudo service cron reload

*** The alternative to this would be to use celery for scheduling tasks ***
```

API Docs
--------
 - Our API Docs gets updated frequently. Use this to test the API's 
 -  URL : http://localhost:8000/api/docs/
 
*** Port 8000 and localhost are just for reference. ***


