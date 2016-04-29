build:
	docker-compose build app

start-b:
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

createsuperuser:
	docker-compose run app /usr/local/bin/python manage.py createsuperuser

updaterates:
	docker-compose run app /usr/local/bin/python manage.py update_rates

adminer:
	docker-compose run --service-ports adminer
