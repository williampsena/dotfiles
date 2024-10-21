SHELL := /bin/bash

VENV_PATH := $(shell realpath ../.venv/bin/activate)

install:
	@source $(VENV_PATH) && pip install -r requirements.txt

check:
	@source $(VENV_PATH) && qtile check

test:
	@source $(VENV_PATH) && pytest -s -vv

format:
	@source $(VENV_PATH) && \
	autoflake --remove-all-unused-imports --in-place --recursive . && \
	isort . && \
	black .