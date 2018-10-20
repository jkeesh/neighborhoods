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


(neighborhoods) jkeesh@localhost:~/sites/neighborhoods$ chown www-data:www-data neighborhoods/
chown: changing ownership of 'neighborhoods/': Operation not permitted
(neighborhoods) jkeesh@localhost:~/sites/neighborhoods$ sudo chown www-data:www-data neighborhoods/
(neighborhoods) jkeesh@localhost:~/sites/neighborhoods$ ls -al
total 32
drwxrwxr-x 3 jkeesh   jkeesh   4096 Oct 20 20:41 .
drwxr-xr-x 8 jkeesh   jkeesh   4096 Oct 20 17:46 ..
-rw-rw-r-- 1 jkeesh   jkeesh   6148 Oct 20 20:05 .DS_Store
-rw-rw-r-- 1 jkeesh   jkeesh     15 Oct 20 19:57 .gitignore
drwxrwxr-x 4 www-data www-data 4096 Oct 20 20:47 neighborhoods
-rw-rw-r-- 1 jkeesh   jkeesh    849 Oct 20 20:41 README.md
-rw-rw-r-- 1 jkeesh   jkeesh     80 Oct 20 20:25 requirements.txt
(neighborhoods) jkeesh@localhost:~/sites/neighborhoods$ cd neighborhoods/
(neighborhoods) jkeesh@localhost:~/sites/neighborhoods/neighborhoods$ ls
compare  db.sqlite3  manage.py  neighborhoods
(neighborhoods) jkeesh@localhost:~/sites/neighborhoods/neighborhoods$ sudo chown www-data:www-data db.sqlite3 
(neighborhoods) jkeesh@localhost:~/sites/neighborhoods/neighborhoods$ ls
compare  db.sqlite3  manage.py  neighborhoods



### TODOS

- deploy to live site
- Set up bootstrap
