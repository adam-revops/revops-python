all:

twine: 
	. .venv/bin/activate;  twine upload dist/*
