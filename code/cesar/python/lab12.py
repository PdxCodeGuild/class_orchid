"""
Lab 12: Contacts 
Cesar Rebolledo
Using YouTube listed below to help with zip()

"""

import pprint


filepath = "contact.csv"
writepath = 'contact2.csv'

with open(filepath, 'r') as f:
    contents = f.read()

lines = contents.split('\n')
header = lines[0].split(',')

contacts = []

for line in lines[1:]:
    
    individual_lines = line.split(',')
    contacts.append(dict(zip(header, individual_lines))) # This line is typecasting to a dictionary and using the zip method to bring together my iterables. https://www.youtube.com/watch?v=auOkA4Ekh8M


choices = '''
Please select one of the following:
1. View the current list
2. Add a new pet to the list
3. Remove a pet from the list
4. Make a change to an existing pet on the list
5. Exit from this program
'''

while True:    
    user_input = input(choices)
    if user_input == '1':

        for line in contacts:
            print(line)

            

    elif user_input == '2':
            # empty dict to use for later. 
            new_pet_dict = {}
            # adding a new pet NAME to the dict. 
            add_pet_name = input(f'Please enter the name of your new pet: ').title()
            new_pet_dict['name'] = add_pet_name
            # adding a breed
            add_pet_breed = input(f'Please enter the pets breed: ').title()
            new_pet_dict['breed'] = add_pet_breed
            # adding a pet color
            add_pet_color = input(f'What is the color of the pet: ')
            new_pet_dict['color'] = add_pet_color
            # adding the pets favorite toy
            add_pet_toy = input(f'What is the pets favorite toy? ')
            new_pet_dict['favoritetoy'] = add_pet_toy
            # print(new_pet_dict)
            # break

            contacts.append(new_pet_dict) # this will add the new dict to the already existing contacts list. 

    elif user_input == '3':
        remove_pet = input('What pet name would you like to remove from the list? ') # make sure first letter is upper. 
        
        for i in range(len(contacts)):
            # print(contacts[i].get('name'))
            
            if contacts[i].get('name') == remove_pet:
                # https://www.geeksforgeeks.org/python-removing-dictionary-from-list-of-dictionaries/ - Resource to delete dictionary from list.
                del contacts[i]
                break
            
    elif user_input == '4':
        pet_to_change = input('What pet would you like to change? ').title()
        for i, dict in enumerate(contacts):
            if pet_to_change == contacts[i].get('name'):
                key_change = input("What would you like to change? Type: name, breed, color, or favoritetoys: ").lower()
                value_change = input('What are we changing that to? ')
                dict[key_change] = value_change

    elif user_input == '5':
        print('Thanks! Take care!')
        break

    else:
        print('Not a valid entry, here is the list again: ')




with open(writepath,'w') as f:
    
    for i in range(len(contacts)):
        f.write('\n')
        f.write((','.join(contacts[i].values())))
