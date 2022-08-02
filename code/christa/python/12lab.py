# Lab 12V1: Contact List
# csv file is a data table with rows and columns

# 1. Build a CSV ('comma separated values') 
# 2. Open the CSV, 
# 3. Convert the lines of text into a list of dictionaries 
# 4. one dictionary for each row. 
# 5. The text in the header represents the keys, 
# 6. The text in the other lines represent the values.

filepath = 'code/christa/python/cities.csv'

with open(filepath, 'r') as f:
    contents = f.read()
#print(contents)
#print(type(contents))
# Line 0 are the headers, or keys for each dictionary
lines = contents.split('\n')   #splitting the lines by the rows
headers = lines[0]             #naming which row are the headers
keys = headers.split(',')     #separating each header by comma - list
values= lines[1:]          #name which rows will be dictionaries - each row is a list
#values = row_lines.split(',')
#print(type(values))
cities_final = []

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



