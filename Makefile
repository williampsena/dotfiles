SHELL := /bin/bash

precommit: leaks

leaks-history:
	docker run --rm \
    -v $(PWD):/repo \
    zricethezav/gitleaks:latest \
    detect --source /repo --config /repo/.gitleaks.toml --report-format json --report-path /repo/gitleaks_report.json

leaks:
	docker run --rm \
    -v $(PWD):/repo \
    zricethezav/gitleaks:latest \
    detect --log-opts="HEAD^..HEAD" --source /repo --config /repo/.gitleaks.toml --report-format json --report-path /repo/gitleaks_report.json