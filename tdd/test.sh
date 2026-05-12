
PYTHONPATH=src:tests coverage run --branch -m unittest discover -s tests

coverage report

coverage html