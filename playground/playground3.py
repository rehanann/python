
# Initialze blockchain empty array
genesis_block = {
        'previous_hash' : '',
        'index' : 0,
        'transactions' : []
    }


blockchain = [genesis_block]
open_transactions = []
owner = 'Rehan'


def get_last_blockchain_value():
    if len(blockchain) < 1:
        return None

    '''print the last blockchain value from the list with [-1]'''
    return blockchain[-1]


def add_transaction(recipient, sender=owner, amount=1.0):
    '''
    1. sender: sender of the coin.
    2. reciepient: beneficiary of coin.
    3. amount: coin amount sent and default(1.0).
    '''
    transaction = {
        'sender' : sender,
        'recipient' : recipient,
        'amount' : amount
    }
    
    open_transactions.append(transaction)


def mine_block():
    last_block = blockchain[-1]
    hashed_block = '-'.join([str(last_block[key]) for key in last_block])
    print(hashed_block)
    for key in last_block:
        value = last_block[key]
        hashed_block = hashed_block + str(value)

    print(hashed_block)

    block = {
        'previous_hash' : hashed_block,
        'index' : len(blockchain),
        'transactions' : open_transactions
    }
    blockchain.append(block)


# ask user to add the transaction amount values.
def get_transaction_value():
    tx_recipient = input('Please enter recipient name: ')
    tx_amount =  float(input('Please enter transaction amount: '))
    return tx_recipient, tx_amount

def get_user_choice():
    user_input = input('Your Choice: ')
    return user_input


def print_blockchain():
    # print output for blockchain transactions.
        for block in blockchain:
            print('Outputting the values')
            print(block)

# Learn Blockchain array and confirm all transactions are truly entered by user.
def verify_chain():
    block_index = 0
    is_valid = True
    for block in blockchain:
        if block_index == 0:
            block_index += 1
            continue
        elif block[0] == blockchain[block_index -1]:
            is_valid = True
        else:
            is_valid = False
            break
        block_index += 1
    return is_valid


# Main Menu
waiting_for_input = True

while waiting_for_input:
    print('Please select your options:')
    print('1: Get transaction amount: ')
    print('2: Mine new block: ')
    print('3: Output blockchain values: ')
    print('h: Manipulate blockchain value: ')
    print('q: Quit')

    user_choice = get_user_choice()
    if user_choice == '1':
        tx_data = get_transaction_value()
        recipient, amount = tx_data
        print(tx_data)
        add_transaction(recipient, amount=amount)
        print(open_transactions)
    elif user_choice == '2':
        mine_block()
    elif user_choice == '3':
        print_blockchain()
    elif user_choice == 'q':
        waiting_for_input = False
    elif user_choice == 'h':
        if len(blockchain) >= 1:
            blockchain[0] = [2]
    else:
        print('This is invalid option please select one')
    # if not verify_chain():
    #     print('Invalid blockchain!')
    #     break
else:
    print('User left!')    

print('Done!')