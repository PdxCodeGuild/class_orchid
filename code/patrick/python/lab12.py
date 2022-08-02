with open('data/contacts.csv', 'r') as file:
    lines = file.read().split('\n')
    

    
    #print(lines)

headers = lines[0]

#print(headers)

headers = headers.split(" , ")

#print(headers)

header = headers[0]

header = header.split(",")
#header = dict(header)

#print(header)

first_line = lines[1]
first_line = first_line.split(" , ")
second_line = lines[2]
second_line = second_line.split(" , ")
third_line = lines[3]
third_line = third_line.split(" , ")
fourth_line = lines[4]
fourth_line = fourth_line.split(" , ")

#print("\n".join(headers))
#def convert(lst):
    #dict = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)}
    #return dict


#print(convert(lines))



for i, item in enumerate(header):
    if i == 1:

    
    #print(i)
    #print(item)
        dict = {}
        dict.update(enumerate(header))
    #print(new_item)
    #dict[header]
        #print(dict)
        new_dict = {}
        for k, v in dict.items():
            new_dict[v] = k
        #print(new_dict)    

#print(new_dict.update(first_line))
#print(dict[1])
for i, item in enumerate(first_line):
    
   
    item = item.split(",")
    
    for i, item in enumerate(item):
        print(i, item)
        if i == 0:
            #print(item)
            new_dict["name"] = item
            print(new_dict)
        if i == 1:
            #print(item)
            new_dict["city"] = item
            print(new_dict)                   
        if i == 2:
            #print(item)
            new_dict["food"] = item
            print(new_dict)
        if i == 3:
            #print(item)
            new_dict["relation"] = item
            #print(new_dict)

new_dict2 = {}
for i, item in enumerate(second_line):
    
   
    item = item.split(",")
    
    for i, item in enumerate(item):
        print(i, item)
        if i == 0:
            #print(item)
            new_dict2["name"] = item
            #print(new_dict)
        if i == 1:
            #print(item)
            new_dict2["city"] = item
            #print(new_dict)                   
        if i == 2:
            #print(item)
            new_dict2["food"] = item
            #print(new_dict)
        if i == 3:
            #print(item)
            new_dict2["relation"] = item
            #print(new_dict2)
new_dict3 = {}
for i, item in enumerate(third_line):
    
   
    item = item.split(",")
    
    for i, item in enumerate(item):
        #print(i, item)
        if i == 0:
            #print(item)
            new_dict3["name"] = item
            #print(new_dict)
        if i == 1:
            #print(item)
            new_dict3["city"] = item
            #print(new_dict)                   
        if i == 2:
            #print(item)
            new_dict3["food"] = item
            #print(new_dict)
        if i == 3:
            #print(item)
            new_dict3["relation"] = item
            #print(new_dict)



new_dict4 = {}
for i, item in enumerate(fourth_line):
    
   
    item = item.split(",")
    
    for i, item in enumerate(item):
        #print(i, item)
        if i == 0:
            #print(item)
            new_dict4["name"] = item
            #print(new_dict)
        if i == 1:
            #print(item)
            new_dict4["city"] = item
            #print(new_dict)                   
        if i == 2:
            #print(item)
            new_dict4["food"] = item
            #print(new_dict)
        if i == 3:
            #print(item)
            new_dict4["relation"] = item
            #print(new_dict)



#print(new_dict)
#print(new_dict2)
#print(new_dict3)
#print(new_dict4)

contacts = []
contacts.append(new_dict)
contacts.append(new_dict2)
contacts.append(new_dict3)
contacts.append(new_dict4)
#print(contacts)

options = '''
    1. Read the contacts list
    2. add a new contact
    3. Remove a contact from the list
    4. Update a contacts info
    5. Quit


'''



    

while True:
    user_input = input(options)
    if user_input == "1":
        print(contacts)

    elif user_input == "2":
        new_name =  input(f"Please enter the name of the new contact: ")
        new_city =  input(f"Please enter the city they live in: ")
        new_food =  input(f"Please enter their favorite food: ")
        new_relation = input(f"Please enter their Realtionship to you: ")
        

        new_dict_5 = {"name":new_name, "city":new_city, "food":new_food, "relation":new_relation}
        
        contacts.append(new_dict_5)
        print(contacts)

    elif user_input == "3":
        contact_to_remove = input(f"what item do you want to remove? ")
        for ct in contacts:
            if ct == contact_to_remove:
                contacts.remove(ct)
                   
    elif user_input == "4":
        contact_to_change = input(f"what item would you like to change? ")
        list_dict = [item for item in contacts if item["name"] == contact_to_change]
        contact_index = contacts.index(list_dict[0])

   
        
        attribute_to_change = input(f"What attribute would you like to change? ")
        
        new_change = input(f"What would you like to change it to? ")
        
        #find out which attribute needs to change and just change that one
        
        contacts[contact_index][attribute_to_change] = new_change
        print(contacts)

    elif user_input == "5":
        print("Done")
        break







print(contacts)