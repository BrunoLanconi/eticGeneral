help:  ## Show help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n",$$1,$$2}'

# Docker commands

bash:  ## Open a bash shell in the running Docker container
	 docker compose -f docker-compose.yaml run --rm --remove-orphans little_lab bash


# JavaScript commands

init:  ## Initialize npm in the project
	docker compose -f docker-compose.yaml run --rm --remove-orphans little_lab npm init

start:  ## Start the JavaScript application
	docker compose -f docker-compose.yaml run --rm --remove-orphans little_lab npm start

test:  ## Run tests for the JavaScript application
	docker compose -f docker-compose.yaml run --rm --remove-orphans little_lab npm test
