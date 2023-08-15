format:
	black .

test: format
	pytest .

typing:
	mypy .

build: typing test