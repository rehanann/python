blockchain = []

def get_last_block_chain():
    return blockchain[-1]

def add_value(transaction_amount, last_transaction=[1]):
    blockchain.append([last_transaction, transaction_amount])
    
def get_user_input():
    return float(input('Your transaction amount please: '))

tx_input = get_user_input()
add_value(tx_input)

tx_input = get_user_input()
add_value(last_transaction=get_last_block_chain(), transaction_amount=tx_input)

tx_input = get_user_input()
add_value(tx_input, get_last_block_chain())

print(blockchain)