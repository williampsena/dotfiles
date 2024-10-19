SHELL := /bin/bash

VENV_PATH := $(shell realpath ../.venv/bin/activate)

install:
	@source $(VENV_PATH) && pip install -r requirements.txt

check:
	@source $(VENV_PATH) && qtile check

test:
	@source $(VENV_PATH) && pytest -s

format:
	@source $(VENV_PATH) && black .