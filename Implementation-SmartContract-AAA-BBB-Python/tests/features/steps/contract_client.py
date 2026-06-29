from solcx import compile_standard, install_solc
import json
from web3 import Web3

address = "0x9A4B680d31F235DDBDDACdbDB29ffaf918C0E78a"
private_key = "0x3a81c05d07183a928973de7c484981a699ef5e538c50bba6d223cb0e40ce6cc9"
chain_id = 1337

smart_contract = None
w3 = None


def deploy_contract(client, contractor, creation_date):
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


def send_transaction(function_call):
    nonce = w3.eth.get_transaction_count(address)
    transaction = function_call.build_transaction(
        {"chainId": chain_id, "gasPrice": w3.eth.gas_price, "from": address, "nonce": nonce})
    sign_transaction = w3.eth.account.sign_transaction(transaction, private_key=private_key)
    transaction_hash = w3.eth.send_raw_transaction(sign_transaction.raw_transaction)
    return w3.eth.wait_for_transaction_receipt(transaction_hash)
