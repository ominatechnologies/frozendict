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
	@python3.9 -m pip install -U pip setuptools wheel tox pre-commit
	@python3.9 -m venv venv
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

# -- Testing --------------- --- --  -

## Run CI pipeline locally
ci: mypy pytest pre-commit
	@git diff --name-only origin/main HEAD | grep CHANGELOG.rst || (echo unchanged CHANGELOG && exit 1)

## Run mypy
mypy:
	@echo "\n\n\033[1;45m FrozenDict Type-Checking \033[0m\n"
ifeq ($(PLATFORM), $(filter $(PLATFORM),MacM1 MacIntel))
	@venv/bin/mypy src tests
else
	@mypy src tests
endif

## Run pre-commit
pre-commit:
	@echo "\n\n\033[1;45m Run pre-commit on FrozenDict \033[0m\n"
	@pre-commit run --all-files

k = "."

## Run pytest
pytest:
	@echo "\n\n\033[1;45m FrozenDict Unit-Testing \033[0m\n"
ifeq ($(PLATFORM), $(filter $(PLATFORM),MacM1 MacIntel))
	@venv/bin/pytest --maxfail=1 -k $(k)
else
	@pytest --maxfail=1 -k $(k)
endif

## Run all tests
test: mypy pytest pre-commit

## Run pytest-watch
watch:
	@echo "\n\n\033[1;45m FrozenDict Unit-Testing in Watch-Mode \033[0m\n"
ifeq ($(PLATFORM), $(filter $(PLATFORM),MacM1 MacIntel))
	@venv/bin/pytest-watch --runner venv/bin/pytest -- --failed-first --maxfail=1 --new-first -k $(k)
else
	@pytest-watch -- --failed-first --maxfail=1 --new-first -k $(k)
endif

## Check the test coverage:
cov:
	@echo "\n\n\033[1;45m FrozenDict Unit-Test Coverage \033[0m\n"
ifeq ($(PLATFORM), $(filter $(PLATFORM),MacM1 MacIntel))
	@venv/bin/coverage run -m pytest --verbosity=0
	@venv/bin/coverage report
else
	@coverage run -m pytest --verbosity=0
	@coverage report
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
	pre-commit \
	pytest \
	reinstall \
	test \
	watch
