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

ci:
	$(PIPENV) run qtile check -c $(PWD)/config.py 

format:
	$(PIPENV) run autoflake --remove-all-unused-imports --in-place --recursive .
	$(PIPENV) run isort .
	$(PIPENV) run black .

truncate-logs:
	truncate -s0 ~/.local/share/qtile/qtile.log 

logs:
	 cat ~/.local/share/qtile/qtile.log

vm-iso:
	bash vm.sh download_iso $(type)

vm-create:
	bash vm.sh create $(type)

vm-start:
	bash vm.sh start $(type)

vm-stop:
	bash vm.sh stop $(type)

vm-ssh:
	bash vm.sh ssh $(type)

vm-sync:
	bash vm.sh sync $(type)

upgrade-deps:
	pipenv update qtile-ebenezer
