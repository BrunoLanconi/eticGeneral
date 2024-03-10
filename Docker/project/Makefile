help: ## Show help
	# From https://marmelab.com/blog/2016/02/29/auto-documented-makefile.html
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n",$$1,$$2}'

.PHONY: web
web:  ## Run web container on port 8000
	docker compose up --build web 

.PHONY: api
api:  ## Run api container on port 8001
	docker compose up --build api

.PHONY: up
up:  ## Run web container on port 8000 and api container on port 8001
	docker compose up --build