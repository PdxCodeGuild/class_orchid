
filepath = 'one_piece/one_piece.csv'

with open('one_piece/one_piece.csv', 'r') as file:
    lines = file.read().split('\n')


contact_list = []

headers = lines[0].split(',')


for value in lines[1:]:
    item = value.split(',')
    contact_list.append(dict(zip(headers, item)))

def create():
    new_person = {}

    for item in headers:
        new_person[item] = input(f'Please enter your {item}: ')
    return new_person


selections = '''
What would you like to do today?
    1.Add a character to the list
    2.Read the list  
    3.Remove a character from the list
    4.Update an item on the list
    5.Quit
'''

while True: 
    user_action = input(selections)

    if user_action == '1':
        #create
        contact_list.append(create())
        print(f'You have successfully added \n"{contact_list[-1]}" to your list')
    elif user_action == '2':
        # print
        print(f'Here is your list \n{contact_list}')
    elif user_action == '3':
        # delete
        is_done = False
        remove_item = input(f"What would you like to remove? \n{contact_list} \n: ")
        for index, contact in enumerate(contact_list):
            if remove_item == contact['name']:
                is_done = True
                contact_list.pop(index)
                print(f"Successfully removed '{remove_item}' from the list")
        if not is_done: 
            print(f"'{remove_item}' is not an item in this list")
    elif user_action == '4':
        # update
        change_item = input(f"What item would you like to update? Start with entering a name: ")
        for contact in contact_list:
            if change_item == contact['name']:
                change_key = input('what should we change?: ')
                change_value = input('what are we changing it to?: ')
                contact[change_key] = change_value
                
        print(f'\nYou have successfully changed {change_item}\'s {change_key} to {change_value}')
            
    elif user_action == '5':
        print("\nGoodbye")
        break
    else:
        print("\nInvalid entry")


with open('one_piece/one_piece.csv', 'w') as f:
    f.write(','.join(headers))
    for i in range(len(contact_list)):
        f.write('\n')
        f.write(','.join(contact_list[i].values()))


