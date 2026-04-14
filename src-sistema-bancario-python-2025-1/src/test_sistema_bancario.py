import unittest
from sistema_bancario import SistemaBancario
from banco import Banco
from dinheiro import Dinheiro, ValorMonetario, Moeda
from operacao import EstadosDeOperacao


class TestHelper:

    @staticmethod
    def criar_banco(sistema_bancario: SistemaBancario, nome_banco: str, moeda: Moeda):
        sistema_bancario.criar_banco(nome_banco, moeda)

    @staticmethod
    def criar_conta(sistema_bancario: SistemaBancario, banco: str, conta: str):
        agencia = sistema_bancario.obter_banco(banco).criar_agencia("Agencia Central")
        conta_criada = agencia.criar_conta(conta)
        return conta_criada


class TestSistemaBancarioCriarEObterBancos(unittest.TestCase):

    def setUp(self):
        self.sistema_bancario = SistemaBancario()

    def test_criar_banco(self):
        # Fixture setup (IMPLICIT)
        # Exercise SUT
        banco = self.sistema_bancario.criar_banco("Banco do Brasil", Moeda.BRL)
        # Result verification
        assert isinstance(banco, Banco)
        self.assertEqual(banco.nome, "Banco do Brasil")
        self.assertEqual(banco.moeda, Moeda.BRL)
        # Teardown

    def test_criar_banco_com_nome_duplicado(self):
        # Fixture setup (IMPLICIT + DELEGATED)
        TestHelper.criar_banco(self.sistema_bancario, "Banco do Brasil", Moeda.BRL)
        # Exercise SUT
        banco = self.sistema_bancario.criar_banco("Banco do Brasil", Moeda.USD)
        # Result verification
        assert isinstance(banco, Banco)
        self.assertEqual(banco.nome, "Banco do Brasil")
        self.assertEqual(banco.moeda, Moeda.USD)
        # Teardown

    def test_obter_bancos_com_multiplos_bancos(self):
        # Fixture setup (IMPLICIT + DELEGATED)
        TestHelper.criar_banco(self.sistema_bancario, "Banco do Brasil", Moeda.BRL)
        TestHelper.criar_banco(self.sistema_bancario, "Banco Santander", Moeda.USD)

        # Exercise SUT
        bancos = self.sistema_bancario.obter_bancos()
        # Result verification
        self.assertEqual(len(bancos), 2)
        self.assertEqual(bancos[0].nome, "Banco do Brasil")
        self.assertEqual(bancos[0].moeda, Moeda.BRL)
        self.assertEqual(bancos[1].nome, "Banco Santander")
        self.assertEqual(bancos[1].moeda, Moeda.USD)
        # Teardown

    def test_obter_bancos_sem_bancos_criados(self):
        # Fixture setup (IMPLICIT)
        # Exercise SUT
        bancos = self.sistema_bancario.obter_bancos()
        # Result verification
        self.assertEqual(len(bancos), 0)
        # Teardown

    def test_obter_banco_sem_banco_criado(self):
        # Fixture setup (IMPLICIT)
        # Exercise SUT
        banco = self.sistema_bancario.obter_banco("Banco do Brasil")
        # Result verification
        self.assertIsNone(banco)
        # Teardown

    def test_obter_banco_com_multiplo_bancos(self):
        # Fixture setup (IMPLICIT + DELEGATED)
        TestHelper.criar_banco(self.sistema_bancario, "Banco do Brasil", Moeda.BRL)
        TestHelper.criar_banco(self.sistema_bancario, "Banco Santander", Moeda.USD)

        # Exercise SUT
        banco = self.sistema_bancario.obter_banco("Banco do Brasil")
        # Result verification
        self.assertIsNotNone(banco)
        self.assertEqual(banco.nome, "Banco do Brasil")
        self.assertEqual(banco.moeda, Moeda.BRL)
        # Teardown

    def test_obter_banco_com_banco_unico(self):
        # Fixture setup (IMPLICIT + DELEGATED)
        TestHelper.criar_banco(self.sistema_bancario, "Banco do Brasil", Moeda.BRL)
        TestHelper.criar_banco(self.sistema_bancario, "Banco do Brasil", Moeda.BRL)

        # Exercise SUT
        banco = self.sistema_bancario.obter_banco("Banco do Brasil")
        # Result verification
        self.assertIsNotNone(banco)
        self.assertEqual(banco.nome, "Banco do Brasil")
        self.assertEqual(banco.moeda, Moeda.BRL)
        # Teardown


class TestSistemaBancarioHelpers(unittest.TestCase):

    def setUp(self):
        self.sistema_bancario = SistemaBancario()

    def test_saldo_ficara_negativo_com_saldo_insuficiente(self):
        # Fixture setup (IMPLICIT + INLINE)
        saldo = ValorMonetario(Moeda.BRL, 100)
        quantia = Dinheiro(Moeda.BRL, 0, 150)
        # Exercise SUT
        resultado = self.sistema_bancario.saldo_ficara_negativo(saldo, quantia)
        # Result verification
        self.assertTrue(resultado)
        # Teardown

    def test_saldo_ficara_negativo_com_saldo_suficiente(self):
        # Fixture setup (IMPLICIT + INLINE)
        saldo = ValorMonetario(Moeda.BRL, 200)
        quantia = Dinheiro(Moeda.BRL, 0, 150)
        # Exercise SUT
        resultado = self.sistema_bancario.saldo_ficara_negativo(saldo, quantia)
        # Result verification
        self.assertFalse(resultado)
        # Teardown

    def test_saldo_ficara_negativo_com_saldo_exatamente_igual(self):
        # Fixture setup (IMPLICIT + INLINE)
        saldo = ValorMonetario(Moeda.BRL, 150)
        quantia = Dinheiro(Moeda.BRL, 0, 150)
        # Exercise SUT
        resultado = self.sistema_bancario.saldo_ficara_negativo(saldo, quantia)
        # Result verification
        self.assertFalse(resultado)
        # Teardown

    def test_saldo_ficara_negativo_com_moeda_diferente(self):
        # Fixture setup (IMPLICIT + INLINE)
        saldo = ValorMonetario(Moeda.BRL, 100)
        quantia = Dinheiro(Moeda.USD, 0, 150)
        # Exercise SUT
        resultado = self.sistema_bancario.saldo_ficara_negativo(saldo, quantia)
        # Result verification
        self.assertTrue(resultado)
        # Teardown


class TestSistemaBancarioOperacoes(unittest.TestCase):

    def setUp(self):
        self.sistema_bancario = SistemaBancario()

    def test_depositar_com_moeda_invalida(self):
        # Fixture setup (IMPLICIT + INLINE + DELEGATED)
        TestHelper.criar_banco(self.sistema_bancario, "Banco do Brasil", Moeda.BRL)
        conta = TestHelper.criar_conta(
            self.sistema_bancario, "Banco do Brasil", "12345-6"
        )
        quantia = Dinheiro(Moeda.USD, 0, 100)
        # Exercise SUT
        operacao = self.sistema_bancario.depositar(conta, quantia)
        # Result verification
        self.assertEqual(operacao.obter_estado(), EstadosDeOperacao.MOEDA_INVALIDA)
        # Teardown

    def test_depositar_com_quantia_invalida(self):
        # Fixture setup (IMPLICIT + INLINE + DELEGATED)
        TestHelper.criar_banco(self.sistema_bancario, "Banco do Brasil", Moeda.BRL)
        conta = TestHelper.criar_conta(
            self.sistema_bancario, "Banco do Brasil", "12345-6"
        )
        quantia = Dinheiro(Moeda.BRL, 0, 0)
        # Exercise SUT
        operacao = self.sistema_bancario.depositar(conta, quantia)
        # Result verification
        self.assertEqual(operacao.obter_estado(), EstadosDeOperacao.SALDO_INSUFICIENTE)
        # Teardown

    def test_depositar_com_sucesso(self):
        # Fixture setup (IMPLICIT + INLINE + DELEGATED)
        TestHelper.criar_banco(self.sistema_bancario, "Banco do Brasil", Moeda.BRL)
        conta = TestHelper.criar_conta(
            self.sistema_bancario, "Banco do Brasil", "12345-6"
        )
        quantia = Dinheiro(Moeda.BRL, 0, 100)
        # Exercise SUT
        operacao = self.sistema_bancario.depositar(conta, quantia)
        # Result verification
        self.assertEqual(operacao.obter_estado(), EstadosDeOperacao.SUCESSO)
        # Teardown

    def test_sacar_com_saldo_insuficiente(self):
        # Fixture setup (IMPLICIT + INLINE + DELEGATED)
        TestHelper.criar_banco(self.sistema_bancario, "Banco do Brasil", Moeda.BRL)
        conta = TestHelper.criar_conta(
            self.sistema_bancario, "Banco do Brasil", "12345-6"
        )
        quantia = Dinheiro(Moeda.BRL, 0, 100)
        # Exercise SUT
        operacao = self.sistema_bancario.sacar(conta, quantia)
        # Result verification
        self.assertEqual(operacao.obter_estado(), EstadosDeOperacao.SALDO_INSUFICIENTE)
        # Teardown

    def test_sacar_com_moeda_invalida(self):
        # Fixture setup (IMPLICIT + INLINE + DELEGATED)
        TestHelper.criar_banco(self.sistema_bancario, "Banco do Brasil", Moeda.BRL)
        conta = TestHelper.criar_conta(
            self.sistema_bancario, "Banco do Brasil", "12345-6"
        )
        quantia = Dinheiro(Moeda.USD, 0, 100)
        # Exercise SUT
        operacao = self.sistema_bancario.sacar(conta, quantia)
        # Result verification
        self.assertEqual(operacao.obter_estado(), EstadosDeOperacao.MOEDA_INVALIDA)
        # Teardown

    def test_sacar_com_sucesso(self):
        # Fixture setup (IMPLICIT + INLINE + DELEGATED)
        TestHelper.criar_banco(self.sistema_bancario, "Banco do Brasil", Moeda.BRL)
        conta = TestHelper.criar_conta(
            self.sistema_bancario, "Banco do Brasil", "12345-6"
        )
        quantia_deposito = Dinheiro(Moeda.BRL, 0, 100)
        self.sistema_bancario.depositar(conta, quantia_deposito)

        quantia_saque = Dinheiro(Moeda.BRL, 0, 50)
        # Exercise SUT
        operacao = self.sistema_bancario.sacar(conta, quantia_saque)
        # Result verification
        self.assertEqual(operacao.obter_estado(), EstadosDeOperacao.SUCESSO)
        # Teardown

    def test_transferir_com_moeda_invalida(self):
        # Fixture setup (IMPLICIT + INLINE + DELEGATED)
        TestHelper.criar_banco(self.sistema_bancario, "Banco do Brasil", Moeda.BRL)
        TestHelper.criar_banco(self.sistema_bancario, "Banco Santander", Moeda.USD)
        conta_origem = TestHelper.criar_conta(
            self.sistema_bancario, "Banco do Brasil", "12345-6"
        )
        conta_destino = TestHelper.criar_conta(
            self.sistema_bancario, "Banco Santander", "65432-1"
        )

        quantia = Dinheiro(Moeda.CHF, 0, 100)
        # Exercise SUT
        operacao = self.sistema_bancario.transferir(
            conta_origem, conta_destino, quantia
        )
        # Result verification
        self.assertEqual(operacao.obter_estado(), EstadosDeOperacao.MOEDA_INVALIDA)
        # Teardown

    def test_transferir_com_saldo_insuficiente(self):
        # Fixture setup (IMPLICIT + INLINE + DELEGATED)
        TestHelper.criar_banco(self.sistema_bancario, "Banco do Brasil", Moeda.BRL)
        TestHelper.criar_banco(self.sistema_bancario, "Banco Santander", Moeda.BRL)
        conta_origem = TestHelper.criar_conta(
            self.sistema_bancario, "Banco do Brasil", "12345-6"
        )
        conta_destino = TestHelper.criar_conta(
            self.sistema_bancario, "Banco Santander", "65432-1"
        )

        quantia = Dinheiro(Moeda.BRL, 0, 100)
        # Exercise SUT
        operacao = self.sistema_bancario.transferir(
            conta_origem, conta_destino, quantia
        )
        # Result verification
        self.assertEqual(operacao.obter_estado(), EstadosDeOperacao.SALDO_INSUFICIENTE)
        # Teardown

    def test_transferir_com_sucesso(self):
        # Fixture setup (IMPLICIT + INLINE + DELEGATED)
        TestHelper.criar_banco(self.sistema_bancario, "Banco do Brasil", Moeda.BRL)
        TestHelper.criar_banco(self.sistema_bancario, "Banco Santander", Moeda.BRL)
        conta_origem = TestHelper.criar_conta(
            self.sistema_bancario, "Banco do Brasil", "12345-6"
        )
        conta_destino = TestHelper.criar_conta(
            self.sistema_bancario, "Banco Santander", "65432-1"
        )

        quantia_deposito = Dinheiro(Moeda.BRL, 0, 100)
        self.sistema_bancario.depositar(conta_origem, quantia_deposito)

        quantia_transferencia = Dinheiro(Moeda.BRL, 0, 50)
        # Exercise SUT
        operacao = self.sistema_bancario.transferir(
            conta_origem, conta_destino, quantia_transferencia
        )
        # Result verification
        self.assertEqual(operacao.obter_estado(), EstadosDeOperacao.SUCESSO)

    def test_transferir_todo_saldo(self):
        # Fixture setup (IMPLICIT + INLINE + DELEGATED)
        TestHelper.criar_banco(self.sistema_bancario, "Banco Santander", Moeda.BRL)
        TestHelper.criar_banco(self.sistema_bancario, "Banco do Brasil", Moeda.BRL)
        conta_origem = TestHelper.criar_conta(
            self.sistema_bancario, "Banco do Brasil", "12345-6"
        )
        conta_destino = TestHelper.criar_conta(
            self.sistema_bancario, "Banco Santander", "65432-1"
        )

        quantia_deposito = Dinheiro(Moeda.BRL, 0, 100)
        self.sistema_bancario.depositar(conta_origem, quantia_deposito)

        quantia_transferencia = Dinheiro(Moeda.BRL, 0, 100)
        # Exercise SUT
        operacao = self.sistema_bancario.transferir(
            conta_origem, conta_destino, quantia_transferencia
        )
        # Result verification
        self.assertEqual(operacao.obter_estado(), EstadosDeOperacao.SUCESSO)
        self.assertEqual(conta_origem.calcular_saldo(), ValorMonetario(Moeda.BRL, 0))


if __name__ == "__main__":
    unittest.main()
