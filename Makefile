.PHONY: pdf setup
pdf:
	python3 scripts/build.py
setup:
	python3 scripts/build.py --install-compiler
