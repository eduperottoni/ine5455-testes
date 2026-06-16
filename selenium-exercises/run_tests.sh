#!/bin/bash

echo "=========================================="
echo "Testes Selenium - INE5455"
echo "=========================================="
echo ""

cd "$(dirname "$0")"

if [ ! -d "exercicio2" ]; then
    echo "Erro: pasta exercicio2 não encontrada"
    exit 1
fi

case "${1:-all}" in
    all|"")
        echo "Executando todos os testes..."
        python -m unittest exercicio2.test_calculadora_duckduckgo -v
        ;;
    a)
        echo "Executando Teste A (Soma)..."
        python -m unittest \
          exercicio2.test_calculadora_duckduckgo.TestCalculadoraDuckDuckGo.teste_a_somar_dois_numeros -v
        ;;
    b)
        echo "Executando Teste B (Multiplicação e Divisão)..."
        python -m unittest \
          exercicio2.test_calculadora_duckduckgo.TestCalculadoraDuckDuckGo.teste_b_multiplicar_e_dividir -v
        ;;
    c)
        echo "Executando Teste C (Subtração)..."
        python -m unittest \
          exercicio2.test_calculadora_duckduckgo.TestCalculadoraDuckDuckGo.teste_c_duas_operacoes_com_subtracao -v
        ;;
    d)
        echo "Executando Teste D (Três Operações e Histórico)..."
        python -m unittest \
          exercicio2.test_calculadora_duckduckgo.TestCalculadoraDuckDuckGo.teste_d_tres_operacoes_e_historico -v
        ;;
    *)
        echo "Uso: $0 [all|a|b|c|d]"
        echo "  all (padrão) - Executar todos os testes"
        echo "  a - Teste A (Soma)"
        echo "  b - Teste B (Multiplicação e Divisão)"
        echo "  c - Teste C (Subtração)"
        echo "  d - Teste D (Três Operações e Histórico)"
        exit 1
        ;;
esac
