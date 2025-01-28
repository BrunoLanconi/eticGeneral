help: ## Show help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n",$$1,$$2}'

.PHONY: up
up:  ## Run Mongo on port 27017 and Mongo Express on port 8081
	docker compose up --build

connect: ## Connect to the Mongo container
	docker compose exec -it mongo mongosh --username root --password example --host localhost:27017 --authenticationDatabase admin db

clean: ## Stop and remove containers
	docker compose down --volumes

restart: clean up ## Restart the containers