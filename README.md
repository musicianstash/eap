#EAP APPLICATION

##INSTALATION

###Docker
Currently not supported, but will come soon.

###Manual (Tested on ubuntu 16.04)
####1.) Install redis, solr nosql db, ...
Install "mysql-server" server and "libmysqlclient-dev" library through terminal with following
command (if you don't care what is password for mysql, then write password `admin` and in that
way you will avoid setting up env variable in latter process):

`sudo apt-get install mysql-server libmysqlclient-dev`

Install **_redis server_** through terminal with following command:

`sudo apt-get install redis-server`

Install **_nosql databae solr_** through terminal with following command:

`sudo apt-get -y install solr-tomcat`

Install **_libjpeg-dev_** (required py Pillow python lib) through terminal with following command:

`sudo apt-get install libjpeg-dev`

####2.) Create mysql eap database and set encoding
Open terminal and run `mysql` so that mysql console is started.

In mysql console write following command so that database is created and encoding set (if not utf-8
 application won't work):
`CREATE DATABASE eap CHARACTER SET utf8 COLLATE utf8_general_ci`

**_GO THROUGH THIS IF ENCODING WAS NOT SET WITH A PREVIOUS COMMAND (in case command in previous
section was not run or database was created with some third party database tool while wrong
encoding was set)_**

_Open terminal and run `mysql` so that mysql console is started._

`_ALTER DATABASE eap CHARACTER SET utf8 COLLATE utf8_general_ci_`

####3.) Install python libraries
Make sure that you are using python 3.5, because any lower version won't work.

Open terminal and open project directory (root of the project). Then run following command:
`pip install -r requirements.txt`

####4.) Run django commands to finish application installation
Create database tables through following command:

`python manage.py migrate`

Create super user through following command:

`python manage.py createsuperuser`

Get currency exchange rates through following command:

`python manage.py update_rates`

####5.) Start development server
Test out application. Run following command:

`python manage.py runserver`

_EAP application should be available through the following url: `http://127.0.0.1:8000/` or
to enter admin enter this url: `http://127.0.0.1:8000/admin`_
