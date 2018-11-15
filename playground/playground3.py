
# Initialze blockchain empty array
blockchain = []


def get_last_blockchain_value():
    if len(blockchain) < 1:
        return None

    '''print the last blockchain value from the list with [-1]'''
    return blockchain[-1]


def add_transaction(transaction_amount, last_transaction=[1]):
    '''
    1. transaction_amount = ask user to input the amount in the array.
    2. last_transaction = this value starts with default amount of [1], and in the user input command 
        it is always included for the reference. 
    '''
    if last_transaction == None:
        last_transaction = [1]
    blockchain.append([last_transaction, transaction_amount])

# ask user to add the transaction amount values.
def get_transaction_value():
    user_input =  float(input('Please enter transaction amount: '))
    return user_input

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
    print('2: Output blockchain values: ')
    print('h: Manipulate blockchain value: ')
    print('q: Quit')

    user_choice = get_user_choice()
    if user_choice == '1':
        tx_amount = get_transaction_value()
        add_transaction(tx_amount, last_transaction=get_last_blockchain_value())
    elif user_choice == '2':
        print_blockchain()
    elif user_choice == 'q':
        waiting_for_input = False
    elif user_choice == 'h':
        if len(blockchain) >= 1:
            blockchain[0] = [2]
    else:
        print('This is invalid option please select one')
    if not verify_chain():
        print('Invalid blockchain!')
        break
else:
    print('User left!')    

print('Done!')