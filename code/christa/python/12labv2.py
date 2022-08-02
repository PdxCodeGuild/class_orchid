# Lab 12V2: CRUD REPL

filepath = 'code/christa/python/cities.csv'

with open(filepath, 'r') as f:
    contents = f.read()
lines = contents.split('\n')   #splitting the lines by the rows
headers = lines[0]             #naming which row are the headers
keys = headers.split(',')     #separating each header by comma - list
values= lines[1:]          #name which rows will be dictionaries - each row is a list
#values = row_lines.split(',') -- this step is the second in the loop, not outside the loop
#print(type(values))



#def format_final_list():
    
cities_final = []

for row_strng in values:  #each row is a string
    row_list = row_strng.split(',')   # now each row is a list
    vacation_data = {}   #bring the dictionary into the loop
    for item in row_list:    #loop through each item in each list
        item_index = row_list.index(item)
        vacation_data[keys[item_index]] = item
    cities_final.append(vacation_data)    
        
#print(vacation_data)
#return cities_final
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
        print(cities_final)
   
    elif user_input == '2':
        to_add = input("What vacation destination would you like to add? \n Please enter the name,weather,landmark,cuisine: ")
        values.append(to_add)
        print(values)
    
    elif user_input == '3':
        to_retrieve = input("What place would you like info about? ")
        #going to have to find matching index list-dictionary
        retrieve_index = cities_final.index(to_retrieve)
        print(retrieve_index)
        #print entire row for that match


    elif user_input == '4':
        to_update = input("What info would you like to update? ")
        #need to find a matching index
        #ask what information to update - list/dictionary
        #update index for matching information

    elif user_input == '5':
        to_delete = input("What location would you like to delete? ")
        #find the index of the location to remove - list
        #remove all items associated with that index - list
    
    elif user_input == '6':
        print("Thanks! See you later, alligator!")
        break

    else:
        print("That is not a valid input. Please select from the list.")


       


        
        


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






    



