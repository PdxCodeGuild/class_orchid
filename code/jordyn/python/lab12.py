import sys
import csv
from csv import writer

options = '''
Please select from the following actions:
    1. Add a person to the Contact List
    2. View a person from the Contact List
    3. Remove a person from the Contact List
    4. Update a person on the Contact List
    5. Quit
'''
contacts = []

def main(contacts):
    contacts = refresh_list()
    user_input = int(input(options))
    if user_input == 1:
        add_member()
    elif user_input == 2:
        access_member(contacts)
    elif user_input == 3:
        remove_member(contacts)
    elif user_input == 4:
        update_member(contacts)
    elif user_input == 5:
        end()

def add_member():
    '''adds a new member to the contact list'''
    new_member = input("What is the name of the new member?\n ").title()
    new_fruit = input(f"What is {new_member}'s favorite fruit?\n ").title()
    new_color = input(f"What is {new_member}'s favorite color?\n ").title()
    added_member = [new_member, new_fruit, new_color]
    append_list_as_row('lab12_contacts_main.csv', added_member)
    print(f"{new_member} has been added. Their favorite fruit is {new_fruit}'s, and their favorite color is {new_color}.")
    main(contacts)

def access_member(contacts):
    '''displays member details'''
    accessed = input("Who are you looking for?\n> ").title()
    for x in range(len(contacts)):
        if contacts[x]['name'] == accessed:
            print(f"{accessed} found. Their favorite fruits are {contacts[x]['favorite fruit']}'s and their favorite color is {contacts[x]['favorite color']}.")
        elif x != len(contacts) - 1:
            continue
        else:
            print(f"No one by the name of {accessed} was found.")
            break
    main(contacts)

def remove_member(contacts):
    '''removes contact information of an existing member'''
    accessed = input("Who are you removing?\n> ").title()
    for x in range(len(contacts)):
        if contacts[x]['name'] == accessed:
            print(f"{accessed} found. Removing from Contact List.")
            del contacts[x]
            break
        elif x != len(contacts) - 1:
            continue
        else:
            print(f"No one by the name of {accessed} was found.")
            break
    dic_to_csv_list(contacts)

def update_member(contacts):
    '''updates information of an existing member'''
    update_options = '''
    Please select from the following actions:
        1. Change Name
        2. Change Favorite Fruit
        3. Change Favorite Color
        4. Back to Main Menu
    '''
    accessed = input("Who are you looking for?\n> ").title()
    for x in range(len(contacts)):
        if contacts[x]['name'] == accessed:
            update_what = int(input(update_options))
            if update_what == 1:
                contacts[x]['name'] = input("What is their new name?\n")
            elif update_what == 2:
                contacts[x]['favorite fruit'] = input("What is their new Favorite Fruit?\n")
            elif update_what == 3:
                contacts[x]['favorite color'] = input("What is their new favorite color?\n")
            elif update_what == 4:
                main(contacts)
            else:
                print("Only characters 1-4 accepted.")
                update_member(contacts)
        elif x != len(contacts) - 1:
            continue
        else:
            print(f"No one by the name of {accessed} was found.")
            break
    dic_to_csv_list(contacts)

def dic_to_csv_list(contacts):
    '''Changes list of dictionaries to a list of CSV rows'''
    new_list = [['name', 'favorite fruit', 'favorite color']]
    for row in contacts:
        new_row = [row['name'] , row['favorite fruit'] , row['favorite color']]
        new_list.append(new_row)
    csv_file_rewrite(new_list)

def csv_file_rewrite(new_list):
    '''rewrites the CSV file entirely to update information cuz its just that inefficient...'''
    with open('lab12_contacts_main.csv', 'w', newline='') as write_obj:
        csv_rewriter = writer(write_obj, escapechar=',', quoting=csv.QUOTE_NONE)
        for index in range(len(new_list)):
            csv_rewriter.writerow(new_list[index])
    main(contacts)

def append_list_as_row(file_name, list_of_elem): #This is stolen cuz I was struggling to get a new line, but I understand it and I wrote all the rest
    '''adds new row to CSV with readable information'''
    with open(file_name, 'a', newline='') as write_obj:
        csv_writer = writer(write_obj)
        csv_writer.writerow(list_of_elem)

def refresh_list():
    contacts = []
    with open('lab12_contacts_main.csv', 'r') as file:
        lines = file.read().split('\n')
    del lines[-1]
    for x in range(len(lines)):
        lines[x] = lines[x].split(',')
    element1 = lines[0][0]
    element2 = lines[0][1]
    element3 = lines[0][2]
    for index in range(1, len(lines)):
        new_dic = {
            element1:lines[index][0],
            element2:lines[index][1],
            element3:lines[index][2]
        }
        contacts.append(new_dic)
    return contacts

def end():
    print("Thank you!")
    sys.exit()

main(contacts)