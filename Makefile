SHELL := /bin/bash

.PHONY: install app

install:
	docker-compose up

app:
	docker-compose up app
