#EAP APPLICATION

##INSTALATION

###Docker
**TESTED ON:** Ubuntu 16.04

####1.) Install docker and docker compose (if it's not already installed)
For installation procedure for docker please visit [docker website](https://docs.docker.com/engine/installation/)

For installation procedure for docker compose please visit [docker website](https://docs.docker.com/compose/install/)

####2.) Build image and container
Run a command:

`make build`

####3.) Create tables, superuser and update rates
First create db tables with a command:

`make migrate`

Then run a command to create a superuser:

`make createsuperuser`

Then run a command to get exchange rates:

`make updaterates`

####4.) Start development server
Test out application. Run following command:

`make dev`

_EAP application should be available through the following url: `http://localhost:8080/` or
to enter admin enter this url: `http://localhost:8080/admin`_


##OTHER

#### Manage database with adminer
Run following command:

`make adminer`

Now you can access adminer on the following url and enter as password `eap`:

`http://localhost:9000/?pgsql=postgres&username=eap&db=eap&ns=public`

#### Docker-Django documentation
Here is official tutorial that we followed for setting up project structure: `https://realpython.com/blog/python/django-development-with-docker-compose-and-machine/`