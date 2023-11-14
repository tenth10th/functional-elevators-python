format:
	black .

test: format
	pytest .

typing:
	mypy .

build: format typing test