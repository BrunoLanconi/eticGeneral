help: ## Show help
	# From https://marmelab.com/blog/2016/02/29/auto-documented-makefile.html
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

run: ## Run the Django server
	poetry run python manage.py runserver

makemigrations: ## Create the Django migrations
	poetry run python manage.py makemigrations

migrate: makemigrations ## Run the Django migrations
	poetry run python manage.py migrate

createsuperuser: ## Create a Django superuser
	poetry run python manage.py createsuperuser

collectstatic: ## Collect the Django static files
	poetry run python manage.py collectstatic