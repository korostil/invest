check:
	isort --check-only --diff .
	black --check .
	flake8
	mypy .

format:
	isort .
	black .