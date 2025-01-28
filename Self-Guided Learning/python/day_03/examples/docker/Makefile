help: ## Show help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

build: ## Build the Docker image
	docker build -t my-python-app .

bash: build ## Run a bash shell in the Docker container
	docker run -it --rm my-python-app bash

run: build ## Run the Docker container
	docker run -it --rm -v ${shell pwd}:/app -p 8000:8000 my-python-app