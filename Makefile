all: build upload

.PHOHNY: clean
clean:
	rm -rf dist

.PHONY: build
build: clean
	python setup.py sdist
	python setup.py bdist_wheel

.PHONY: upload
upload: build
	twine upload dist/*
