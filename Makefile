.PHONY: help setup_env setup_docker clean run_docker lint test coverage

VENV_NAME?=env
MIGRATION_FOLDER?=migrations
PYTHON_LOCAL=python
PYTHON_ENV=${VENV_NAME}/bin/python

.DEFAULT: help
help: ## Show this help.
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

setup_env: $(VENV_NAME)/bin/activate ## Prepare virtual environment.
$(VENV_NAME)/bin/activate: requirements.txt | clean
	test -d $(VENV_NAME) || ${PYTHON_LOCAL} -m virtualenv $(VENV_NAME)
	${PYTHON_ENV} -m pip install -U pip
	${PYTHON_ENV} -m pip install -r requirements.txt

setup_docker: clean ## Prepare service in Docker container.
	${PYTHON_LOCAL} -m pip install -U pip
	${PYTHON_LOCAL} -m pip install -r requirements.txt

clean: ## Delete virtual environment and migration folders.
	rm -rf $(VENV_NAME)

run_docker: ## Run service in Docker container.
	${PYTHON_LOCAL} run.py

lint: ## Check code using pylint.
	${PYTHON_ENV} -m pylint file_service
