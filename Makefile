all: build upload

.PHONY: test
test:
	cd docs/ && make doctest

.PHOHNY: clean
clean:
	rm -rf dist

.PHONY: build
build: clean test
	python setup.py sdist
	python setup.py bdist_wheel

.PHONY: upload
upload: build
	twine upload dist/*
