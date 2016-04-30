.PHONY: build startb start remove status dev migrate makemigrations createsuperuser updaterates \
		bash syncindex testindex collectstatic elasticsearch adminer

build:
	docker-compose build app

startb:
	docker-compose up -d

start:
	docker-compose up

remove:
	docker-compose stop && docker-compose rm -f

status:
	docker-compose ps

dev:
	docker-compose run --service-ports app /usr/local/bin/python manage.py runserver 0.0.0.0:8080

migrate:
	docker-compose run app /usr/local/bin/python manage.py migrate

makemigrations:
	docker-compose run app /usr/local/bin/python manage.py makemigrations

createsuperuser:
	docker-compose run app /usr/local/bin/python manage.py createsuperuser

updaterates:
	docker-compose run app /usr/local/bin/python manage.py update_rates

bash:
	docker-compose run --service-ports app /bin/bash

syncindex:
	docker-compose run --service-ports app /usr/local/bin/python manage.py sync_index

testindex:
	docker-compose run --service-ports app /usr/local/bin/python manage.py test_index

collectstatic:
	docker-compose run --service-ports app /usr/local/bin/python manage.py collectstatic

elasticsearch:
	docker-compose run --service-ports elasticsearch

adminer:
	docker-compose run --service-ports adminer
