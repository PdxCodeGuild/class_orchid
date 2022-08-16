


with open('data/contacts.csv', 'r') as file:
    lines = file.read().split('\n')
    

headers = lines[0]
headers = headers.split(" , ")
header = headers[0]
header = header.split(",")

first_line = lines[1]
first_line = first_line.split(" , ")
second_line = lines[2]
second_line = second_line.split(" , ")
third_line = lines[3]
third_line = third_line.split(" , ")
fourth_line = lines[4]
fourth_line = fourth_line.split(" , ")



for i, item in enumerate(header):
    if i == 1:
        dict = {}
        dict.update(enumerate(header))
        new_dict = {}
        for k, v in dict.items():
            new_dict[v] = k

    
    

for i, item in enumerate(first_line):
    
   
    item = item.split(",")
    
    for i, item in enumerate(item):
        
        if i == 0:
            new_dict["name"] = item
            
        if i == 1:
            new_dict["city"] = item
                               
        if i == 2:
            new_dict["food"] = item
            
        if i == 3:
            new_dict["relation"] = item
            
            
            
            
            

new_dict2 = {}
for i, item in enumerate(second_line):
    
   
    item = item.split(",")
    
    for i, item in enumerate(item):
        
        if i == 0:
            new_dict2["name"] = item
        if i == 1:
            new_dict2["city"] = item
        if i == 2:
            new_dict2["food"] = item
        if i == 3:
            new_dict2["relation"] = item
           
            
new_dict3 = {}
for i, item in enumerate(third_line):
    
   
    item = item.split(",")
    
    for i, item in enumerate(item):
        
        if i == 0:
            new_dict3["name"] = item
        if i == 1:
            new_dict3["city"] = item
        if i == 2:
            new_dict3["food"] = item
        if i == 3:
            new_dict3["relation"] = item
            
            
            
           



new_dict4 = {}
for i, item in enumerate(fourth_line):
    
   
    item = item.split(",")
    
    for i, item in enumerate(item):
        
        if i == 0:
            new_dict4["name"] = item
        if i == 1:
            new_dict4["city"] = item
        if i == 2:
            new_dict4["food"] = item
        if i == 3:
            new_dict4["relation"] = item
            
            
            


contacts = []
contacts.append(new_dict)
contacts.append(new_dict2)
contacts.append(new_dict3)
contacts.append(new_dict4)


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
        

    elif user_input == "3":
        contact_to_remove = input(f"what item do you want to remove? ")
        for ct in contacts:
            if ct["name"] == contact_to_remove:
                contacts.remove(ct)
                   
    elif user_input == "4":
        contact_to_change = input(f"what item would you like to change? ")
        list_dict = [item for item in contacts if item["name"] == contact_to_change]
        contact_index = contacts.index(list_dict[0])
        attribute_to_change = input(f"What attribute would you like to change? ")
        new_change = input(f"What would you like to change it to? ")
        contacts[contact_index][attribute_to_change] = new_change
    elif user_input == "5":
        print("Done")
        break

output = headers
for contact in contacts:
    
    
    output.append(",".join(contact.values()))



with open('data/contacts.csv', 'w') as f:
     f.write("\n".join(output))

   
        
        
        
        
        
        
        


