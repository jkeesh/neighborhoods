# neighborhoods




### Setup

mkvirtualenv neighborhoods

to start using

workon neighborhoods


upgraded pip, virtualenv, virtualenvwrapper


pip install Django==1.11.16
pip install django-extensions

## on server

install pip 

did virtualenv setup on server
was in ~/.local dir

mkvirtualenv neighborhoods

added requirements file 

istalled on server from reqs.
(neighborhoods) jkeesh@localhost:~/sites/neighborhoods$ pip install -r requirements.txt 

virtual env location

(neighborhoods) jkeesh@localhost:~/.local/bin$ ls
pbr  virtualenv  virtualenv-clone  virtualenvwrapper_lazy.sh  virtualenvwrapper.sh
(neighborhoods) jkeesh@localhost:~/.local/bin$ pwd
/home/jkeesh/.local/bin

virtual env home /home/jkeesh/.virtualenvs

virtual env directory: /home/jkeesh/.virtualenvs/neighborhoods

restarting server
$ systemctl reload apache2
https://modwsgi.readthedocs.io/en/develop/user-guides/virtual-environments.html
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/modwsgi/
https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

(neighborhoods) jkeesh@localhost:~/sites/neighborhoods$ sudo chown www-data:www-data neighborhoods/
(neighborhoods) jkeesh@localhost:~/sites/neighborhoods/neighborhoods$ sudo chown www-data:www-data db.sqlite3 
https://stackoverflow.com/questions/21054245/attempt-to-write-a-readonly-database-django-w-selinux-error

needed to run migrations on web server


<Directory /home/jkeesh/sites/neighborhoods/neighborhoods/static>
Require all granted
</Directory>



Trying to run collect static on web server

### Helpful commands

Collect static files

    ./manage.py collectstatic

Restart server

    $ systemctl reload apache2


DEPLOYMENT

    On local machine

    $ git push origin master; git push web master

    On server

    $ systemctl reload apache2


### TODOS

- Set up bootstrap
- add comments , disquss
