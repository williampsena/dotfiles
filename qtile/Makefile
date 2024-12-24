SHELL := /bin/bash
PIPENV=pipenv
PIPFILE=Pipfile
PYTHON=$(PIPENV) run python

install:
	$(PIPENV) install

activate:
	$(PIPENV) shell

check:
	$(PIPENV) run qtile check

format:
	$(PIPENV) run autoflake --remove-all-unused-imports --in-place --recursive .
	$(PIPENV) run isort .
	$(PIPENV) run black .

truncate-logs:
	truncate -s0 ~/.local/share/qtile/qtile.log 

logs:
	 cat ~/.local/share/qtile/qtile.log

vm-iso:
	bash vm.sh download_iso

vm-create:
	bash vm.sh create

vm-start:
	bash vm.sh start

vm-stop:
	bash vm.sh stop

vm-ssh:
	bash vm.sh ssh
