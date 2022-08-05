filepath = '../data/contacts.csv'

#make the data in the file readable
with open(filepath, 'r') as f:
    contents = f.read()


#creates a list of the lines
lines = contents.split('\n')


#creates headers as the first line
header = lines[0]

header = header.split(',')

#blank list which will hold the list of contacts without the header
list_of_contacts = []

#the final list that will hold the dictionaries we will create later
list_of_dicts = []

#took the lines in contents and removed the header line so it is only the names and attributes
contacts = lines[1:]

#for loop that is saying for each lines in all the lines of contacts, so it will iterate after every line
for contact in contacts:
    #we want to take the line we are iterating through and turn it into a list
    contact = contact.split(",")
    #we want to append the blank list of contacts with each new list created every iteration
    list_of_contacts.append(contact)

#for loop that iterates through every new list we created and appended to the list of contacts   
for list in list_of_contacts:
    
    dict = {}
    #for loop that iterated through list 
    for i,thing in enumerate(list):
        #creating values to made the keys in header
        dict[header[i]] = thing
    #appending the new dictionaries to the list of dictionaries
    list_of_dicts.append(dict)

#while loop for that runs the crud repl 
while True:
    print(f'''

    - Enter 1 to see the list of contacts
    - Enter 2 to add a contact
    - Enter 3 to remove a contact
    - Enter 4 to make changes to a contact
    - Enter 5 to exit the program and see the most current list of contacts

    ''')
    #user input thats asks the user what they want to do
    user_input = input(f"\nWhat would you like to do?: ")

    #if statements that prints the current list of dictionaries
    if user_input == '1':
        print(list_of_dicts)
    
    #user input that asks for input to create a new contact
    elif user_input == '2':
        #blank list that will hold new list
        new_list = []
        #user input for new contact
        name = input("\nwhat is your name? ")
        new_list.append(name)
        food = input("What is your favorite food? ")
        new_list.append(food)
        color = input("what is your favorite color? ")
        new_list.append(color)
        season = input("what is your favorite season? ")
        new_list.append(season)
        language = input("what language do you speak?")
        new_list.append(language)
        #used to create new dictionary holding new user contact information
        new_dict = {}

        #for loop that will make each header the key and new user info as value 
        for i,thing in enumerate(new_list):
            new_dict[header[i]] = thing
        #appends the current list of dictionaries with the new user dictionary that was created 
        list_of_dicts.append(new_dict)
        print(new_dict)

    #user input that will remove contact
    elif user_input == '3':
        print(list_of_dicts)
        #user entered name for contact to be deleted
        remove_contact = input("\nwhich contact should we remove? ")
        remove_contact.lower()

        #for loop that covers the range of the list of dicts looking for the index holding the name the user entered
        for index in range(len(list_of_dicts)):
            if list_of_dicts[index]['name'] == remove_contact:
                #the index holding the contact
                remove_index = index
                #contact removed
                list_of_dicts.pop(remove_index)
                print(list_of_dicts)
                break
    #option 4 which can change an attribute about a contact
    elif user_input == '4':
        #contact name that will have an attribute changed
        choose_contact = input("type a contact you are looking to change: ")
        choose_contact.lower()

        #finds the contacts index based on the user input
        for index in range(len(list_of_dicts)):
            if list_of_dicts[index]['name'] == choose_contact:
                change_contact = index
                #converts the index into the dictionary stored in that index
                selected = list_of_dicts[change_contact]
                print(selected)
                #informs user on what to press to change which particular attribute.
                what_to_change = input('''             
                - Enter 1 to change the name of the contact
                - Enter 2 to change the favorite food of the contact
                - Enter 3 to change the favorite color of the contact
                - Enter 4 to change the favorite season of the contact
                - Enter 5 to change the language the contact speaks

                Enter a number
                ''')
                #converts user input string into an integer
                what_to_change = int(what_to_change)

                #based on user inputs they are send to an if or elif statement that handles the input change
                if what_to_change == 1:
                    change_name = input('what to change name too? ')
                    selected['name'] = change_name
                    print(selected)

                elif what_to_change == 2:
                    change_food = input('what to change food too? ')
                    selected['food'] = change_food
                    print(selected)

                elif what_to_change == 3:
                    can_change_color = input('what to change color too? ')
                    selected['color'] = can_change_color
                    print(selected)

                elif what_to_change == 4:
                    change_season = input('what to change season too? ')
                    selected['season'] = change_season
                    print(selected)

                elif what_to_change == 5:
                    change_language = input('what to change language too? ')
                    selected['language'] = change_language
                    print(selected)
                
                else:
                    print("invalid input")
    #breaks us out of the while look
    elif user_input == '5':
        break

#variable that represents the strings that dictionaries will be converted too
new_csv = ''
#writing the new information to a csv file
with open('../data/contacts.csv', 'w') as f:
    #converts the headers list into a string of each item separated by a ','
    header = ','.join(header)
    #for loop that iterates through each contact in dictionary
    for contact in list_of_dicts:
        #extracts the values and not the keys of each contact
        contact = contact.values()
        #joins the values into a string that is separated by a ','
        contact = ','.join(contact)
        #adds the contact to the new_csv blank string and ends the line
        new_csv += contact + '\n'
    #takes the header and ends the line at the end of the string
    new_header = header + '\n'
    #takes the header first and follows its with the strings added in new csv later
    final_csv = new_header + new_csv
    print(final_csv)
    f.write(final_csv.strip())


