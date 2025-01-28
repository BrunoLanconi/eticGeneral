help: ## Show help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

main: ## Run main
	poetry run python src/main.py

init-migrations: ## Init alembic
	poetry run alembic init migrations

migrate: ## Migrate
	poetry run alembic revision --autogenerate -m "Add table"

upgrade: ## Upgrade
	poetry run alembic upgrade head