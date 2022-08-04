with open('contact.csv', 'r') as file:
    lines = file.read().split('\n')
# print(lines)

# splitting list into w list of lists
split_list = []
for line in lines:
    split_list.append(line.split(','))

# print(split_list)

keys = split_list[0]
# print(keys)


contact_list = []
for value in split_list[1:]:
    contact_list.append(dict(zip(keys,value)))

# print(contact_list)

# version 1 complete

user_options = '''
Hello, please selcet from the following:
1-Create contact
2-Read list
3-Update list
4-Delete contact
5-Exit
'''
# print(user_options)

while True:
    user_input = input(user_options)

    if user_input == '2':
        print(contact_list)

    elif user_input == '1':
        # new_dict = dict()
        contact_name = input('What is the name?: ')
        favorite_fruit = input('What is their favorite fruit?: ')
        location = input('Where do they live?: ')
        favorite_food = input('What is their favorite food?: ')
        favorite_color = input('What is there favorite color?: ')
        new_dict = {
            'name':contact_name,
            'favorite fruit':favorite_fruit,
            'location':location,
            'favortie food':favorite_food,
            'favorite color':favorite_color}
        contact_list.append(new_dict)
        print(f"Successfully added '{contact_name}' to the list")

    elif user_input == '4':
        remove_contact = input('Who should we remove?: ')
        is_complete = False
        for contact in contact_list:
            if remove_contact == contact['name']:
                contact_list.remove(contact)
                print('Complete')


    elif user_input == '3':
        person = input('Who would you like to change?: ')
        for i, contact in enumerate(contact_list):
            if person == contact['name']:
                attribute = input(f'What would you like to change?: {keys} ')
                print(contact_list[i][attribute])
                new_attribute = input(f'What would you like to change the {attribute} to?: ')
                contact[attribute] = new_attribute
                print(f'{attribute} is now {new_attribute}')

    
    elif user_input == '5':
            print('Goodbye')
            break
        
with open('contact.csv', 'w') as w:
    w.write(str(contact_list))




