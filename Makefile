all: build upload

.PHONY: test
test:
	cd docs/ && make doctest

.PHOHNY: clean
clean:
	rm -rf dist

.PHONY: build
build: clean test
	python3 setup.py sdist
	python3 setup.py bdist_wheel

.PHONY: upload
upload: build
	twine upload dist/*
