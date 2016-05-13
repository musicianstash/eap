.PHONY: build app start remove down status migrate makemigrations createsuperuser \
		updaterates worker bash syncindex testindex collectstatic elasticsearch \
		importcrawlertestitemsadminer pyclean

build:
	docker-compose build eap

app:
	docker-compose up -d

start:
	docker-compose up

dev:
	docker-compose run eap /usr/local/bin/python manage.py runserver 0.0.0.0:8080

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

importcrawlertestitems:
	docker-compose run eap /usr/local/bin/python manage.py import_test_crawler_items

worker:
	docker-compose run eap celery -A eap.celery worker -l info

bash:
	docker-compose run eap /bin/bash

shell:
	docker-compose run eap /usr/local/bin/python manage.py shell

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
