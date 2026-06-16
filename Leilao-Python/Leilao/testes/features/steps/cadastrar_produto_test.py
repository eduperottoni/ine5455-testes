from behave import *
from mercado_leilao import MercadoLeilao


@given('o cadastro do usuario Ernani Cesar foi realizado')
def step_impl(context):
    context.mercado = MercadoLeilao()
    context.mercado.cadastra_usuario('Ernani Cesar', 'Campus Universitario',
                                     'ernani.santos@posgrad.ufsc.br', '055.761.919-00')


@given('o nome do produto {nome_produto}')
def step_impl(context, nome_produto):
    context.nome_produto = nome_produto


@given('a descricao do produto {descricao_produto}')
def step_impl(context, descricao_produto):
    context.descricao_produto = descricao_produto


@given('e o lance {lance}')
def step_impl(context, lance):
    context.lance = int(lance)


@given('e o cpf do leiloador {cpf_leiloador}')
def step_impl(context, cpf_leiloador):
    context.cpf_leiloador = cpf_leiloador


@given('sofa amarelo ja foi cadastrado')
def step_impl(context):
    context.mercado.cadastra_produto('sofa', 'amarelo', 100, '055.761.919-00', 99999)


@when('cadastrar o produto')
def step_impl(context):
    try:
        context.mercado.cadastra_produto(context.nome_produto, context.descricao_produto,
                                         context.lance, context.cpf_leiloador, 99999)
        context.msg = 'sucesso'
    except Exception as e:
        context.msg = e.__str__()


@then('o sistema cadastra com sucesso')
def step_impl(context):
    assert context.msg == 'sucesso'
    assert context.mercado.possui_produto() == True


@then('o sistema mostra a mensagem {mensagem}')
def step_impl(context, mensagem):
    assert mensagem == context.msg
