#!make

SHELL = /bin/sh

# COLORS
GREEN  := $(shell tput -Txterm setaf 2)
YELLOW := $(shell tput -Txterm setaf 3)
WHITE  := $(shell tput -Txterm setaf 7)
RESET  := $(shell tput -Txterm sgr0)


TARGET_MAX_CHAR_NUM=20
## Show help
help:
	@echo ''
	@echo 'Usage:'
	@echo '  ${YELLOW}make${RESET} ${GREEN}<target>${RESET}'
	@echo ''
	@echo 'Targets:'
	@awk '/^[a-zA-Z\-\_0-9]+:/ { \
		helpMessage = match(lastLine, /^## (.*)/); \
		if (helpMessage) { \
			helpCommand = $$1; sub(/:$$/, "", helpCommand); \
			helpMessage = substr(lastLine, RSTART + 3, RLENGTH); \
			printf "  ${YELLOW}%-$(TARGET_MAX_CHAR_NUM)s${RESET} ${GREEN}%s${RESET}\n", helpCommand, helpMessage; \
		} \
	} \
	{ lastLine = $$0 }' $(MAKEFILE_LIST)

# -- Setup Commands --------------- --- --  -

## Initialize environment.
install: install-tools install-pre-commit

install-tools:
	@python3.8 -m pip install -U pip setuptools wheel tox pre-commit
	@python3.8 -m venv venv
	@venv/bin/pip install -U pip setuptools wheel
	@venv/bin/pip install -r requirements.dev.txt -e .

## Reinstall environment
reinstall: clean-environment install

## Clean environment
clean-environment:
	@venv/bin/pip freeze | grep -v "@" | xargs venv/bin/pip uninstall -y
	@venv/bin/pip uninstall -y frozendict pytest-watch

## Install git hooks that run Flake8 before accepting commits.
install-pre-commit:
	@pre-commit install -f --install-hook && \
	git config --bool flake8.strict true && \
	git config --bool flake8.lazy true
	@pre-commit autoupdate

## Clean
clean:
	@find . -path "./venv" ! -prune \
	-o -type d -name "__pycache__" \
	-o -type d -name "build" \
	-o -type d -name "dist" \
	-o -type d -name "*.egg-info" \
	-o -type d -name ".eggs" \
	-o -type d -name ".mypy_cache" \
	-o -type d -name ".pytest_cache" \
	| xargs rm -rf
	@rm -rf ~/.tox_frozendict

# -- Wrapup --------------- --- --  -

.DEFAULT: help

.PHONY: \
	install \
	reinstall \
	clean-environment \
	clean \
	help \
