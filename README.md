#EAP APPLICATION

##INSTALATION

###Docker
**TESTED ON:** Ubuntu 16.04

####1.) Install newest versions of docker and docker compose
For installation procedure for docker please visit
[docker website](https://docs.docker.com/engine/installation/)

For installation procedure for docker compose please visit
[docker website](https://docs.docker.com/compose/install/)

####2.) Build image and container
Run a command:

`make build`

####3.) Start services
Run a command to start the containers in the background and leave them running:

`make app`

####4.) Create tables, superuser and update rates
First create db tables with a command:

`make migrate`

Then run a command to create a superuser:

`make createsuperuser`

Then run a command to get exchange rates:

`make updaterates`

####5.) Access application
Test out application:

- frontend: [http://localhost:8080/](http://localhost:8080/)
- backend: [http://localhost:8080/admin/](http://localhost:8080/admin/)


##OTHER

#### Manage database with adminer
Access adminer on the following url:
[http://localhost:9000/?pgsql=postgres&username=eap&db=eap&ns=public](http://localhost:9000/?pgsql=postgres&username=eap&db=eap&ns=public)

-  enter as password `eap`
- login and manage your database :)

#### Docker-Django documentation
Here is official tutorial that we followed for setting up project structure:
https://realpython.com/blog/python/django-development-with-docker-compose-and-machine/
