build:
	docker-compose build app

dev:
	docker-compose run --service-ports app /usr/local/bin/python manage.py runserver 0.0.0.0:8080

migrate:
	docker-compose run app /usr/local/bin/python manage.py migrate

createsuperuser:
	docker-compose run app /usr/local/bin/python manage.py createsuperuser

adminer:
	docker-compose run --service-ports adminer
