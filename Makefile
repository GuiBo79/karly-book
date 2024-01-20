SHELL := /bin/bash

.PHONY: build-db up app run

build-db:
	docker-compose build db

up:
	docker-compose up --build

app:
	docker-compose up app

run: build-db up app