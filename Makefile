format:
	isort .
	black .

clean:
	rm -rf dist *.egg-info

dist:
	python -m build

twine-upload: dist
	twine upload 'dist/*'

.PHONY: format clean twine-upload
