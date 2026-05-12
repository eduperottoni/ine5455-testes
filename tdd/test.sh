
PYTHONPATH=src:tests coverage run --branch -m unittest tests.test_empresa

coverage report

coverage html