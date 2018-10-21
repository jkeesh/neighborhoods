# neighborhoods

### Overview

This site lets people enter mappings from neighborhoods in one city to their comparable neighborhood in another city. The the votes are added up to create a city/neighbhoord mapping. 

View the site at http://neighborhood.thekeesh.com


### Local Development Notes


    # Set up virtual environment
    workon neighborhoods


### Deployment Notes

    # on local machine, push to both github and the web server
    $ git push origin master; git push web master


    # on the server, restart apache
    $ systemctl reload apache2

    # if there are new static files, run on the webserver
    $ cd /home/jkeesh/sites/neighborhoods/neighborhoods
    $ workon neighborhoods
    $ ./manage.py collectstatic



### TODOS


    - add some direct city comparison cards
    - make view page responsive
    - make compare page responsive
    - automate post receive hook for migrations, static files and server
    - add comments , disquss


### Other random notes

#### Setup

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



