help: ## Show help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

build: ## Build the project
	docker build -t app app
	docker build -t postgres postgres

up: ## Start the project
	docker-compose up --build

create-network: ## Create a network
	docker network create --driver bridge app-network

no-compose: ## Start the project without docker-compose
	make create-network || true
	make build
	docker run -d --rm --name postgres --network app-network -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=postgres -e POSTGRES_DB=postgres -p 5432:5432 postgres
	docker run -it --rm --name app --network app-network -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=postgres -e POSTGRES_HOST=postgres -e POSTGRES_DB=postgres -v ${PWD}/app:/app -p 8000:8000 app poetry run uvicorn src.app:app --host 0.0.0.0 --port 8000
