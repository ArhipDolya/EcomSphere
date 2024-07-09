DC = docker compose
EXEC = docker-compose exec
APP_FILE = user_service/docker-compose/app.yaml
APP_CONTAINER = user_service

.PHONY: app
app:
	${DC} -f ${APP_FILE} up --build

.PHONY: app-down
app-down:
	${DC} -f ${APP_FILE} down
