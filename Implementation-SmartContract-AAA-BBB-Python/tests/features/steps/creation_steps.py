from behave import *
from unittest import TestCase

import contract_client

# getObligN retorna uma tupla com (descrição, status)
oblig_getters = {
    1: lambda: contract_client.smart_contract.functions.getOblig1().call(),
    2: lambda: contract_client.smart_contract.functions.getOblig2().call(),
    3: lambda: contract_client.smart_contract.functions.getOblig3().call(),
    4: lambda: contract_client.smart_contract.functions.getOblig4().call(),
    5: lambda: contract_client.smart_contract.functions.getOblig5().call(),
    6: lambda: contract_client.smart_contract.functions.getOblig6().call(),
    7: lambda: contract_client.smart_contract.functions.getOblig7().call(),
}


@given(u'contratante {client} criada')
def step_impl(context, client):
    context.client = client


@given(u'contratada {contractor} criada')
def step_impl(context, contractor):
    context.contractor = contractor


@given(u'data de criação é {date}')
def step_impl(context, date):
    context.creation_date = int(date)


@given(u'contrato foi criado')
def step_impl(context):
    contract_client.deploy_contract(context.client, context.contractor, context.creation_date)


@when(u'contrato é criado')
def step_impl(context):
    contract_client.deploy_contract(context.client, context.contractor, context.creation_date)


@given(u'o contrato é ativado')
@when(u'o contrato é ativado')
def step_impl(context):
    contract_client.send_transaction(contract_client.smart_contract.functions.activate())


@then(u'contrato deve ter status {created_status}')
def step_impl(context, created_status):
    status = contract_client.smart_contract.functions.getStatus().call()
    TestCase.assertEqual(TestCase(), int(created_status), status)


@then(u'data de criação é {date}')
def step_impl(context, date):
    creation_date = contract_client.smart_contract.functions.getCreationDate().call()
    TestCase.assertEqual(TestCase(), int(date), creation_date)


@then(u'data de inicio é {date}')
def step_impl(context, date):
    start_date = contract_client.smart_contract.functions.getActivationDate().call()
    TestCase.assertEqual(TestCase(), int(date), start_date)


@then(u'data de término é {date}')
def step_impl(context, date):
    termination_date = contract_client.smart_contract.functions.getTerminationDate().call()
    TestCase.assertEqual(TestCase(), int(date), termination_date)


@then(u'Oblig{number:d} deve ter status {expected_oblig_status}')
def step_impl(context, number, expected_oblig_status):
    oblig_status = oblig_getters[number]()
    TestCase.assertEqual(TestCase(), int(expected_oblig_status), oblig_status[1])
