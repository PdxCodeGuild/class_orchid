'''
CRUD REPL: 

These are database operations, but we can perform them on our local data stores too
Create 
Read / Retrieve
Update
Delete / Destroy

This is a user interface where the user can give text commands to a program
Your terminal is an example of a REPL
Read
Evaluate
Print
Loop
'''

to_do = [
    'walk the cat',
    'clean the lawn',
    'water the gremlin'
]

options = '''
Please select from the following actions:
    1. Read the list
    2. Add an item to the list
    3. Remove an item from the list
    4. Update an item on the list
    5. Quit
'''

while True: 
    user_action = input(options)

    if user_action == '1':
        # read
        print('\n'.join(to_do))
    elif user_action == '2':
        # create
        new_item = input("What should we add? ")
        to_do.append(new_item)
        print(f"Successfully added '{new_item}' to the list")
    elif user_action == '3':
        # delete
        remove_item = input("What should we remove? ")
        # lowered_list = [td.lower() for td in to_do] // list comprehension we didn't wind up using
        for td in to_do:
            if td.lower() == remove_item.lower():
                to_do.remove(td)
        print(f"Successfully removed '{remove_item}' from the list")
    elif user_action == '4':
        # update
        change_item = input("What item should we change? ")
        new_item = input('What should we change it to? ')
        item_index = to_do.index(change_item)
        to_do[item_index] = new_item
        print(f"Successfully changed '{change_item}' to '{new_item}'")
    elif user_action == '5':
        print("Goodbye")
        break
    else:
        print("That is not a valid option")
