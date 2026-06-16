import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestCalculadoraDuckDuckGo(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(15)

    def tearDown(self):
        self.driver.quit()

    def abrir_calculadora(self):
        self.driver.get("https://duckduckgo.com/?q=calculator")
        self.driver.find_element(By.ID, "zci-calculator")

    def clicar_botao(self, valor):
        xpath = f"//button[@value='{valor}']"
        botao = self.driver.find_element(By.XPATH, xpath)
        botao.click()

    def obter_resultado(self):
        display = self.driver.find_element(
            By.ID,
            "display"
        )
        return display.text.strip()

    def obter_operacoes_historico(self):

        itens = self.driver.find_elements(
            By.CLASS_NAME,
            "tile__past-calc"
        )
        operacoes = []
        for item in itens:
            formula = item.find_element(
                By.CLASS_NAME,
                "tile__past-formula"
            ).text.strip()
            resultado = item.find_element(
                By.CLASS_NAME,
                "tile__past-result"
            ).text.strip()
            operacoes.append((formula, resultado))
        return operacoes

    def teste_a_somar_dois_numeros(self):
        self.abrir_calculadora()

        self.clicar_botao("1")
        self.clicar_botao("5")
        self.clicar_botao("+")
        self.clicar_botao("8")
        self.clicar_botao("=")

        resultado = self.obter_resultado()
        msg = f"Esperado 23, obteve {resultado}"
        self.assertIn("23", resultado, msg)

    def teste_b_multiplicar_e_dividir(self):
        self.abrir_calculadora()

        self.clicar_botao("1")
        self.clicar_botao("2")
        self.clicar_botao("×")
        self.clicar_botao("5")
        self.clicar_botao("÷")
        self.clicar_botao("1")
        self.clicar_botao("0")
        self.clicar_botao("=")

        resultado = self.obter_resultado()
        msg = f"Esperado 6, obteve {resultado}"
        self.assertIn("6", resultado, msg)

    def teste_c_duas_operacoes_com_subtracao(self):
        self.abrir_calculadora()

        self.clicar_botao("2")
        self.clicar_botao("0")
        self.clicar_botao("-")
        self.clicar_botao("7")
        self.clicar_botao("=")

        resultado = self.obter_resultado()
        msg = f"Esperado 13, obteve {resultado}"
        self.assertIn("13", resultado, msg)

    def teste_d_tres_operacoes_e_historico(self):
        self.abrir_calculadora()

        self.clicar_botao("2")
        self.clicar_botao("5")
        self.clicar_botao("+")
        self.clicar_botao("1")
        self.clicar_botao("0")
        self.clicar_botao("=")

        resultado1 = self.obter_resultado()
        msg1 = f"Operação 1: Esperado 35, obteve {resultado1}"
        self.assertIn("35", resultado1, msg1)

        self.clicar_botao("5")
        self.clicar_botao("0")
        self.clicar_botao("×")
        self.clicar_botao("3")
        self.clicar_botao("=")

        resultado2 = self.obter_resultado()
        msg2 = f"Operação 2: Esperado 150, obteve {resultado2}"
        self.assertIn("150", resultado2, msg2)

        self.clicar_botao("1")
        self.clicar_botao("0")
        self.clicar_botao("0")
        self.clicar_botao("÷")
        self.clicar_botao("4")
        self.clicar_botao("=")

        resultado3 = self.obter_resultado()
        msg3 = f"Operação 3: Esperado 25, obteve {resultado3}"
        self.assertIn("25", resultado3, msg3)

        operacoes = self.obter_operacoes_historico()
        count = len(operacoes)
        msg = f"Esperado 3+ itens no histórico, obteve {count}"
        self.assertGreaterEqual(count, 3, msg)

        historico_formulas = [op[0] for op in operacoes]
        self.assertIn("25 + 10", historico_formulas,
                      "Operação '25 + 10' não encontrada no histórico")
        self.assertIn("50 × 3", historico_formulas,
                      "Operação '50 × 3' não encontrada no histórico")
        self.assertIn("100 ÷ 4", historico_formulas,
                      "Operação '100 ÷ 4' não encontrada no histórico")


if __name__ == "__main__":
    unittest.main()
