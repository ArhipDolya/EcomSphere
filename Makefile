DC = docker compose
EXEC = docker-compose exec
APP_FILE = docker-compose/app.yaml
STORAGES_FILE = docker-compose/storages.yaml
APP_CONTAINER = user_service

.PHONY: app
app:
	${DC} -f ${APP_FILE} -f ${STORAGES_FILE} up --build

.PHONY: app-down
app-down:
	${DC} -f ${APP_FILE} -f ${STORAGES_FILE} down
