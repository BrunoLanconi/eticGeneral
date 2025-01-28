help: ## Show help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

build: ## Build the Docker image
	docker build -t my-nginx .

bash: build ## Run a bash shell in the container
	docker run -it --rm my-nginx /bin/sh

run: build ## Run the container
	docker run --name my-nginx -p 8080:80 my-nginx

up:  ## Run the container as service with Docker Compose
	docker compose up