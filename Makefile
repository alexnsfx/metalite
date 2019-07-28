#!/usr/bin/env make

PYTHON=python

.PHONY: default
default: patch

.PHONY: release
release:
	$(PYTHON) setup.py sdist bdist_wheel

.PHONY: major
major:
	$(PYTHON) release.py major

.PHONY: minor
minor:
	$(PYTHON) release.py minor

.PHONY: patch
patch:
	$(PYTHON) release.py patch
