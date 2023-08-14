test:
	pytest .

format:
	black .

typing:
	mypy .

build: format typing test