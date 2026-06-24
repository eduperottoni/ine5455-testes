from behave import *

import contract_client


@given(u'Oblig{number:d} não foi cumprida')
@when(u'Oblig{number:d} não foi cumprida')
def step_impl(context, number):
    contract_client.send_transaction(contract_client.smart_contract.functions.unfulfillOblig(number))
