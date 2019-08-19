all:

twine: 
	. .venv/bin/activate; python setup.py sdist;  twine upload dist/*
