help: ## Show help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

build: ## Build the Docker image
	docker build -t my-python-app .

bash: build ## Run a bash shell in the Docker container
	docker run -it --rm -p 5000:5000 my-python-app bash

run: build ## Run the Django app
	docker run -it --rm -p 5000:5000 my-python-app