# Initialze blockchain empty array
blockchain = []


def get_last_blockchain_value():
    '''add last blockchain value in the list with [-1]'''
    return blockchain[-1]


def add_value(transaction_amount, last_transaction=[1]):
    '''
    1. transaction_amount = ask user to input the amount in the array.
    2. last_transaction = this value starts with default amount of [1], and in the user input command 
        it is always included for the reference. 
    '''
    blockchain.append([last_transaction, transaction_amount])

def get_user_input():
    return float(input('Please enter transaction amount: '))

tx_amount = get_user_input()
add_value(tx_amount)

tx_amount = get_user_input()
add_value(last_transaction=get_last_blockchain_value(), transaction_amount=tx_amount)

tx_amount = get_user_input()
add_value(tx_amount, last_transaction=get_last_blockchain_value())

print(blockchain)