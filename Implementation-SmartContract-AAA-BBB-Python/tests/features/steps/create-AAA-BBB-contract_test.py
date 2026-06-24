from behave import *
from unittest import TestCase

from solcx import compile_standard, install_solc
import json
from web3 import Web3

address = "0x2389011e574f9dF0F34eEc9f39BbE2C400CFE31f"
private_key = "0x6950316a16ba968518ed79620c274792a5c7083dd15a45d4eddf9897db2b0417"

smart_contract = None
w3 = None
chain_id = 1337


def __deploy_contract(client, contractor, creation_date):
    global smart_contract
    global w3

    # Endereço do diretório onde está o smart contract AAABBBContract
    with open("src/resources/ClientContractorContract.sol", "r") as file:
        smart_contract_file = file.read()
    _solc_version = "0.8.0"
    install_solc(_solc_version)
    # Considerando o smart contract ProductSaleContract
    compiled_sol = compile_standard({"language": "Solidity", "sources": {"ClientContractorContract.sol": {"content": smart_contract_file}},
            "settings": {"outputSelection": {"*": {"*": ["abi", "metadata", "evm.bytecode", "evm.bytecode.sourceMap"]} } }, }, solc_version=_solc_version,)
    with open("compiled_code.json", "w") as file:
        json.dump(compiled_sol, file)
    bytecode = compiled_sol["contracts"]["ClientContractorContract.sol"]["ClientContractorContract"]["evm"]["bytecode"]["object"]
    abi = json.loads(compiled_sol["contracts"]["ClientContractorContract.sol"]["ClientContractorContract"]["metadata"])["output"]["abi"]
    # Rodando o ganache localmente...
    w3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:7545"))
    smart_contract = w3.eth.contract(abi=abi, bytecode=bytecode)
    nonce = w3.eth.get_transaction_count(address)
    # Parâmetros do construtor do smart contract
    transaction = smart_contract.constructor(client, contractor, creation_date).build_transaction(
        {"chainId": chain_id, "gasPrice": w3.eth.gas_price, "from": address, "nonce": nonce})
    sign_transaction = w3.eth.account.sign_transaction(transaction, private_key=private_key)
    transaction_hash = w3.eth.send_raw_transaction(sign_transaction.raw_transaction)
    transaction_receipt = w3.eth.wait_for_transaction_receipt(transaction_hash)
    # Referência para o smart contract
    smart_contract = w3.eth.contract(address=transaction_receipt.contractAddress, abi=abi)


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
    __deploy_contract(context.client, context.contractor, context.creation_date)

@when(u'contrato é criado')
def step_impl(context):
    __deploy_contract(context.client, context.contractor, context.creation_date)


@then(u'contrato deve ter status {created_status}')
def step_impl(context, created_status):
    status = smart_contract.functions.getStatus().call()
    TestCase.assertEqual(TestCase(), int(created_status), status)


@then(u'data de criação é {date}')
def step_impl(context, date):
    creation_date = smart_contract.functions.getCreationDate().call()
    TestCase.assertEqual(TestCase(), int(date), creation_date)


@then(u'data de inicio é {date}')
def step_impl(context, date):
    start_date = smart_contract.functions.getActivationDate().call()
    TestCase.assertEqual(TestCase(), int(date), start_date)


@then(u'data de término é {date}')
def step_impl(context, date):
    termination_date = smart_contract.functions.getTerminationDate().call()
    TestCase.assertEqual(TestCase(), int(date), termination_date)

# getObligN retorna uma tupla com (descrição, status)

@then(u'Oblig1 deve ter status {expected_oblig_status}')
def step_impl(context, expected_oblig_status):
    oblig_status = smart_contract.functions.getOblig1().call()
    TestCase.assertEqual(TestCase(), int(expected_oblig_status), oblig_status[1])

@then(u'Oblig2 deve ter status {expected_oblig_status}')
def step_impl(context, expected_oblig_status):
    oblig_status = smart_contract.functions.getOblig2().call()
    TestCase.assertEqual(TestCase(), int(expected_oblig_status), oblig_status[1])

@then(u'Oblig3 deve ter status {expected_oblig_status}')
def step_impl(context, expected_oblig_status):
    oblig_status = smart_contract.functions.getOblig3().call()
    TestCase.assertEqual(TestCase(), int(expected_oblig_status), oblig_status[1])

@then(u'Oblig4 deve ter status {expected_oblig_status}')
def step_impl(context, expected_oblig_status):
    oblig_status = smart_contract.functions.getOblig4().call()
    TestCase.assertEqual(TestCase(), int(expected_oblig_status), oblig_status[1])

@then(u'Oblig5 deve ter status {expected_oblig_status}')
def step_impl(context, expected_oblig_status):
    oblig_status = smart_contract.functions.getOblig5().call()
    TestCase.assertEqual(TestCase(), int(expected_oblig_status), oblig_status[1])

@then(u'Oblig6 deve ter status {expected_oblig_status}')
def step_impl(context, expected_oblig_status):
    oblig_status = smart_contract.functions.getOblig6().call()
    TestCase.assertEqual(TestCase(), int(expected_oblig_status), oblig_status[1])

@then(u'Oblig7 deve ter status {expected_oblig_status}')
def step_impl(context, expected_oblig_status):
    oblig_status = smart_contract.functions.getOblig7().call()
    TestCase.assertEqual(TestCase(), int(expected_oblig_status), oblig_status[1])



# @then(u'the smart contract is activated')
# def step_impl(context):
#     status = smart_contract.functions.getStatus().call()
#     TestCase.assertEqual(TestCase(), 1, status)


# @given(u'smart contract deployado')
# def step_impl(context):
#     __deploy_contract(context.client, context.contractor, context.creation_date)


# @when(u'o contrato é ativado')
# def step_impl(context):
#     transaction = smart_contract.functions.activate().build_transaction({"chainId": chain_id,
#                                                                          "gasPrice": w3.eth.gas_price,
#                                                                          "from": address,
#                                                                          "nonce": w3.eth.get_transaction_count(address)})
#     sign_transaction = w3.eth.account.sign_transaction(transaction, private_key=private_key)
#     transaction_hash = w3.eth.send_raw_transaction(sign_transaction.raw_transaction)
    




# @then(u'creation date is {date}')
# def step_impl(context, date):
#     TestCase.assertEqual(TestCase(), int(date), smart_contract.functions.getCreationDate().call())