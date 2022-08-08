# Lab 12V2: CRUD REPL
from pprint import pprint

filepath = 'code/christa/python/cities.csv'

with open(filepath, 'r') as f:
    contents = f.read()
lines = contents.split('\n')   #splitting the lines by the rows
headers = lines[0]             #naming which row are the headers
keys = headers.split(',')     #separating each header by comma - list
values= lines[1:]          #name which rows will be dictionaries - each row is a list
#values = row_lines.split(',') -- this step is the second in the loop, not outside the loop
#print(type(values))



def format_final_list():
    cities_final = []
    for row_strng in values:  #each row is a string
        row_list = row_strng.split(',')   # now each row is a list
        vacation_data = {}   #bring the dictionary into the loop
        for item in row_list:    #loop through each item in each list
            item_index = row_list.index(item)
            vacation_data[keys[item_index]] = item
        cities_final.append(vacation_data)    
        
#print(vacation_data)
    return cities_final
#print(format_final_list())

options = '''
1. View dictionary
2. Create a record
3. Retrieve a record
4. Update a record
5. Delete a record
6. Quit
'''

while True:
    user_input = input(options)

    if user_input == '1':
        print(format_final_list())
   
   #can clean up spaces later
    elif user_input == '2':
        to_add = input("What vacation destination would you like to add? \n Please enter the name,weather,landmark,cuisine: ")
        values.append(to_add)
        format_final_list()
        print(f'This is the new list: {format_final_list()}')
    
    elif user_input == '3':
        place_options = []
        for place_dict in format_final_list():
            place_options.append(place_dict['name'])   
            #print(place_options)
        to_retrieve = input(f"""
        What place would you like info about? 
        Here are your options: 
        {place_options} 
        """)
        for place_dict in format_final_list():
            if to_retrieve.lower() == place_dict['name'].lower():
                pprint(place_dict)
        #going to have to find matching index list-dictionary
        #print(retrieve_index)
        #print entire row for that match
    
    
    elif user_input == '4':
        place_options = []
        for place_dict in format_final_list():
            place_options.append(place_dict['name'])
        to_update = input(f"""
        'Here are your options:
        {place_options}
        What place would you like to view for updates? """)
                #if to_update.lower() == place_dict[i].lower():
        for place_dict in format_final_list():    
            if to_update.lower() == place_dict['name'].lower():
                print(place_dict)
    
            to_replace = input (f""""
            To update the name of the place enter 1.
            To update the weather enter 2.
            To update the landmark enter 3.
            To update the cuisine enter 4.
            To exit enter 5.
            """)
        
            while True:
                if to_replace == '1':
                    replace_to = input("What would you like to change the place to? ")
                    place_dict['name'] = replace_to
                    print(place_dict)

                elif to_replace == '2':
                    replace_to = input("What would you like to change the weather to? ")
                    place_dict['weather'] = replace_to
                    print(place_dict)

                elif to_replace == '3':
                    replace_to = input("What would you like to change the landmark to? ")
                    place_dict['landmark'] = replace_to
                    print(place_dict)

                elif to_replace == '4':
                    replace_to = input("What would you like to change the cuisine to? ")
                    place_dict['cuisine'] = replace_to
                    print(place_dict)
                
                elif to_replace == '5':
                    print('Thanks for your changes!')
                    break

                else:
                    print(f'Not a valid Command.')
       
        #need to find a matching index
        #ask what information to update - list/dictionary
        #update index for matching information

        #""".key find the keys if input == key """

    elif user_input == '5':
        place_options = []
        for place_dict in format_final_list():
            place_options.append(place_dict['name'])
        to_delete = input(f"""
        'Here are your options:
        {place_options}
        What place would you like to delete? """)
                #if to_update.lower() == place_dict[i].lower():
        for i, place_dict in enumerate(format_final_list()):    
            if to_delete.lower() == place_dict['name'].lower():
                confirm_delete = input(f'Are you sure you want to delete {place_dict}?')
                if confirm_delete == 'yes':
                    values.pop(i)
                    pprint(format_final_list())     
                else:
                    break

        #find the index of the location to remove - list
        #remove all items associated with that index - list
    
    elif user_input == '6':
        print("Thanks! See you later, alligator!")
        break

    else:
        print("That is not a valid input. Please select from the list.")


       
#Example for inspiration
"""cat_columns = ['name', 'weather', 'landmark', 'cuisine']
for column in cat_columns:
    print(cities_final[column].value.counts())
    print('-' * 50)   """
        


"""
Create a record: ask the user for each attribute, add a 
new contact to your contact list with the attributes that the user entered.

Retrieve / Read: Retrieve a record: ask the user for the contact's name, 
find the user with the given name, and display their information

Update: Update a record: ask the user for the contact's name,
 then for which attribute of the user they'd like to update 
and the value of the attribute they'd like to set.

Delete / Destroy: Delete a record: ask the user for the contact's name, 
remove the contact with the given name from the contact list.

Read
Evaluate
Print
Loop
"""






    




