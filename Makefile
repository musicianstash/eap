.PHONY: build app start remove down status migrate makemigrations createsuperuser \
		updaterates bash syncindex testindex collectstatic elasticsearch adminer pyclean

build:
	docker-compose build eap

app:
	docker-compose up -d

start:
	docker-compose up

remove:
	docker-compose stop && docker-compose rm -f

down:
	docker-compose down

status:
	docker-compose ps

migrate:
	docker-compose run eap /usr/local/bin/python manage.py migrate

makemigrations:
	docker-compose run eap /usr/local/bin/python manage.py makemigrations

createsuperuser:
	docker-compose run eap /usr/local/bin/python manage.py createsuperuser

updaterates:
	docker-compose run eap /usr/local/bin/python manage.py update_rates

bash:
	docker-compose run eap /bin/bash

syncindex:
	docker-compose run eap /usr/local/bin/python manage.py sync_index

testindex:
	docker-compose run eap /usr/local/bin/python manage.py test_index

collectstatic:
	docker-compose run eap /usr/local/bin/python manage.py collectstatic

elasticsearch:
	docker-compose run elasticsearch

adminer:
	docker-compose run adminer

pyclean:
	find . -type f -name "*.py[co]" -delete
	find . -type d -name "__pycache__" -delete
