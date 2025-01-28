help: ## Show help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

jupyter: ## Run Jupyter notebook
	poetry run jupyter notebook

generate-csv: ## Generate CSV file
	poetry run python src/utils/files.py

sample: ## Run sample
	poetry run python src/sample.py

transform: ## Run transform
	poetry run python src/transform.py