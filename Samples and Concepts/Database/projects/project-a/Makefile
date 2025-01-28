help: ## Show help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n",$$1,$$2}'

clean: ## Stop and remove containers
	docker compose down
	docker rm -f postgres-db-1
	docker volume rm postgres_data

dev-build: ## Build the dev container
	docker build -t poetry-dev -f ops/poetry.Dockerfile .

dev-bash: ## Run bash in the dev container
	docker compose run -it --rm poetry bash

dev-init: ## Initialize a new poetry project
	docker compose run -it --rm poetry poetry init

dev-add: ## Add a package to the poetry project
	docker compose run -it --rm poetry poetry add $(package)

dev-main: ## Run the main.py file
	docker compose run -it --rm poetry python src/main.py

dev-up: ## Start the dev container
	docker-compose -f docker-compose.yaml up

lint: ## Run the linter
	poetry run black .
	poetry run ruff format .
	poetry run ruff check .