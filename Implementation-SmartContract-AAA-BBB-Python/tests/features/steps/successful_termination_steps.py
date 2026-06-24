from behave import *

import contract_client


@given(u'Oblig{number:d} foi cumprida')
@when(u'Oblig{number:d} foi cumprida')
def step_impl(context, number):
    contract_client.send_transaction(contract_client.smart_contract.functions.fulfillOblig(number))


@when(u'o contrato é encerrado')
def step_impl(context):
    contract_client.send_transaction(contract_client.smart_contract.functions.terminate())
