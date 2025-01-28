help: ## Show help
	# From https://marmelab.com/blog/2016/02/29/auto-documented-makefile.html
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

install: ## Creates new environment
	poetry install

activate: install ## Activates environment
	poetry shell

test: install ## Runs unit tests with pytest
	poetry run pytest -vvv -s

docs: install ## Creates technical documentation in docs folder
	poetry run pdoc src tests -o docs

release: install test docs ## Creates release in dist folder
	poetry build -f wheel
