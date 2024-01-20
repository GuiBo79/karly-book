SHELL := /bin/bash

.PHONY: build-db up app run

build-db:
	docker-compose build db

build-php:
	docker-compose build phpmyadmin

app:
	docker-compose up app

install: build-db build-php app