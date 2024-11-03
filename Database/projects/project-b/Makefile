help: ## Show help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n",$$1,$$2}'

migrate:  ## Run migrations
	docker compose run -it django-app poetry run python manage.py makemigrations

build: migrate  ## Build the project
	docker build -t django-app -f ops/django-app.Dockerfile ./django-app

bash:  ## Run bash in the django-app container
	docker compose exec -it django-app bash

up:  ## Run the project
	docker compose up --build

dump:  ## Dump the database
	docker compose exec -it django-app poetry run python manage.py dumpdata -o data.json
	docker cp django-postgres-django-app-1:/app/data.json ./data.json

load:  ## Load the database
	docker compose exec -it django-app poetry run python manage.py loaddata /app/data.json
