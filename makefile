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


k = "."

## Run CI pipeline locally
ci:
ifeq ($(PLATFORM), $(filter $(PLATFORM),MacM1 MacIntel))
	@echo mypy && venv/bin/mypy src/frozendict tests
	@echo pytest && venv/bin/pytest
	@echo pre-commit && pre-commit run --from-ref origin/main --to-ref HEAD
	@git diff --name-only origin/main HEAD | grep CHANGELOG.rst || (echo missing CHANGELOG && exit 1)
else
	@echo mypy && mypy src/frozendict tests
	@echo pytest && pytest
	@echo pre-commit && pre-commit run --from-ref origin/main --to-ref HEAD
	@git diff --name-only origin/main HEAD | grep CHANGELOG.rst || (echo missing CHANGELOG && exit 1)
endif

## Run mypy
mypy:
ifeq ($(PLATFORM), $(filter $(PLATFORM),MacM1 MacIntel))
	@venv/bin/mypy src tests
else
	@mypy src tests
endif

## Run pytest
pytest:
ifeq ($(PLATFORM), $(filter $(PLATFORM),MacM1 MacIntel))
	@venv/bin/pytest --maxfail=1 -k $(k)
else
	@pytest --maxfail=1 -k $(k)
endif

## Run pytest-watch
watch:
ifeq ($(PLATFORM), $(filter $(PLATFORM),MacM1 MacIntel))
	@venv/bin/pytest-watch -- --failed-first --maxfail=1 --new-first -k $(k)
else
	@pytest-watch -- --failed-first --maxfail=1 --new-first -k $(k)
endif

## Check outdated packages
outdated:
ifeq ($(PLATFORM), $(filter $(PLATFORM),MacM1 MacIntel))
	@venv/bin/pip list --outdated
else
	@pip list --outdated
endif

## Check dep-tree packages
dep-tree:
ifeq ($(PLATFORM), $(filter $(PLATFORM),MacM1 MacIntel))
	@venv/bin/pip install pipdeptree
	@venv/bin/pipdeptree -l | grep -v "@" > deptree.txt
else
	@pip install pipdeptree
	@pipdeptree -l | grep -v "@" > deptree.txt
endif

# -- Wrapup --------------- --- --  -

.DEFAULT: help

.PHONY: \
	ci \
	clean \
	clean-environment \
	dep-tree \
	help \
	install \
	install-pre-commit \
	mypy \
	outdated \
	pytest \
	reinstall \
	watch
