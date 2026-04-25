PYTHONPATH=src python3 -m unittest discover -s tests
PYTHONPATH=src mutmut run

mutmut results | grep survived

mutmut browse