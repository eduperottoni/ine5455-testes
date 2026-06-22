from behave import *
from unittest import TestCase

from solcx import compile_standard, install_solc
import json
from web3 import Web3

address = "0x9C0BC888A04bc385f7F657295a68362D882a4987"
private_key = "0x3b834daa3aae15c06a1914027ff9de215247d3c23f3411aca8abbb1f6c2774c8"

smart_contract = None
w3 = None
chain_id = 1337


def __deploy_contract(seller, buyer, title, currency):
    global smart_contract
    global w3

    # Endereço do diretório onde está o smart contract ProductSaleContract
    with open("/home/edu/projects/ine5455-testes/Implementation-SmartContract-Example-ProductSale-Python/Implementation-SmartContract-Example-ProductSale-Python/src/resources/ProductSaleContract.sol", "r") as file:
        smart_contract_file = file.read()
    _solc_version = "0.8.0"
    install_solc(_solc_version)
    # Considerando o smart contract ProductSaleContract
    compiled_sol = compile_standard({"language": "Solidity", "sources": {"ProductSaleContract.sol": {"content": smart_contract_file}},
            "settings": {"outputSelection": {"*": {"*": ["abi", "metadata", "evm.bytecode", "evm.bytecode.sourceMap"]} } }, }, solc_version=_solc_version,)
    with open("compiled_code.json", "w") as file:
        json.dump(compiled_sol, file)
    bytecode = compiled_sol["contracts"]["ProductSaleContract.sol"]["ProductSaleContract"]["evm"]["bytecode"]["object"]
    abi = json.loads(compiled_sol["contracts"]["ProductSaleContract.sol"]["ProductSaleContract"]["metadata"])["output"]["abi"]
    # Rodando o ganache localmente...
    w3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:7545"))
    smart_contract = w3.eth.contract(abi=abi, bytecode=bytecode)
    nonce = w3.eth.get_transaction_count(address)
    # Parâmetros do construtor do smart contract
    transaction = smart_contract.constructor(seller, buyer, title, currency).build_transaction(
        {"chainId": chain_id, "gasPrice": w3.eth.gas_price, "from": address, "nonce": nonce})
    sign_transaction = w3.eth.account.sign_transaction(transaction, private_key=private_key)
    transaction_hash = w3.eth.send_raw_transaction(sign_transaction.raw_transaction)
    transaction_receipt = w3.eth.wait_for_transaction_receipt(transaction_hash)
    # Referência para o smart contract
    smart_contract = w3.eth.contract(address=transaction_receipt.contractAddress, abi=abi)


@given("the seller {contract_seller}")
def step_impl(context, contract_seller):
    context.contract_seller = contract_seller


@given("the buyer {contract_buyer}")
def step_impl(context, contract_buyer):
    context.contract_buyer = contract_buyer


@given("the effective date of the contract {contract_effective_date}")
def step_impl(context, contract_effective_date):
    context.contract_effective_date = contract_effective_date


@given("the contract title {contract_title}")
def step_impl(context, contract_title):
    context.contract_title = contract_title


@given("the currency {currency_name}")
def step_impl(context, currency_name):
    context.currency_name = currency_name


@when("the contract is created")
def step_impl(context):
    __deploy_contract(context.contract_seller, context.contract_buyer,
                      context.contract_title, context.currency_name)


@then("the contract seller must be {seller_name}")
def step_impl(context, seller_name):
    TestCase.assertEqual(TestCase(), seller_name, smart_contract.functions.getSeller().call())


@then("the contract buyer must be {buyer_name}")
def step_impl(context, buyer_name):
    TestCase.assertEqual(TestCase(), buyer_name, smart_contract.functions.getBuyer().call())


@then("the contract title must be {contract_title}")
def step_impl(context, contract_title):
    TestCase.assertEqual(TestCase(), contract_title, smart_contract.functions.getTitle().call())


@then("the currency must be {currency_name}")
def step_impl(context, currency_name):
    currency_value = smart_contract.functions.getCurrency().call()
    if (currency_name == 'USD'):
        TestCase.assertEqual(TestCase(), 0, currency_value)
    elif (currency_name == 'CAN'):
        TestCase.assertEqual(TestCase(), 1, currency_value)
    elif (currency_name == 'BRL'):
        TestCase.assertEqual(TestCase(), 2, currency_value)
    else:
        TestCase.fail("Unknown currency " + currency_name)


@then("the total price of the contract must be {total_price_value}")
def step_impl(context, total_price_value):
    TestCase.assertEqual(TestCase(), int(total_price_value), smart_contract.functions.getContractTotalPrice().call())
