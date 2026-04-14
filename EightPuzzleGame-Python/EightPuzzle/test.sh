# tests.testes_cobertura.TestBranchsMoveTile
# tests.testes_cobertura.TestComandosMoveTile
# tests.testes_cobertura_dados.TestCoberturaDadosLine
# tests.testes_cobertura_dados.TestCoberturaDadosColumn

PYTHONPATH=src:tests coverage run --branch -m unittest tests.testes_cobertura_dados.TestCoberturaDadosLine

coverage report

coverage html