'''Jen Williams
PDX Code Guild Bootcamp - Orchid
lab 12: Contact List'''

import string
with open('rabbits.csv', 'r') as file:
    lines = file.read().split('\n')
#print(lines)
headers = lines[0].split(',')

rabbits = []

for i, line in enumerate(lines):
    print(line)
    if i > 0:
        line = line.split(',')
        print(line)
        create_rabbit = {
            
            headers[0]: line[0], 
            headers[1]: line[1],
            headers[2]: line[2],
            headers[3]: line[3],
            headers[4]: line[4],

            }

        rabbits.append(create_rabbit)

#print(rabbits[1])

options = '''
Please select from the following actions:
    1. Read the breed information
    2. Add a breed to the list
    3. Remove a breed from the list
    4. Update a breed
    5. Save changes and quit
    6. Quit without saving
'''

while True: 
    user_action = input(options)

    if user_action == '1':
    # read
    
        for rabbit in rabbits:
            print(rabbit, "\n") 

    elif user_action == '2':
    # add
        breed_add = input("Which rabbit breed would you like to add? ")
        pose_add = input("What is this breed's pose? ")
        size_add = input("what is this breed's size? ")
        ear_add = input("What is this breed's ear carriage? ")
        fur_add = input("What is this breed's fur type? ")

        new_rabbit = {
            
            headers[0]: breed_add, 
            headers[1]: pose_add,
            headers[2]: size_add,
            headers[3]: ear_add,
            headers[4]: fur_add,

            }

        rabbits.append(new_rabbit)

    elif user_action == '3':
     #remove
        breed_remove = input("Which rabbit breed would you like to remove? ")  
        is_done = False
    
        for rabbit in rabbits:
            #print(rabbit)
            if rabbit.get('breed') == breed_remove:
                rabbits.remove(rabbit)
                is_done = True
                print(f"You have successfully removed {breed_remove}. ")
        if not is_done: 
            print(f"I'm sorry, {breed_remove} was not found. ")

    elif user_action == '4':
        breed_update = input("Which breed would you like to update? ")
        is_done = False

        for rabbit in rabbits: 
            if rabbit.get('breed') == breed_update:
                new_name = input("What is the breed name? ")
                new_pose = input("What is the breed pose? ")
                new_size = input("What is the breed size? ")
                new_ears = input("What is the breed ear carriage? ")
                new_fur = input("What is the breed fur type? ")

                updated_rabbit = {
            
                    headers[0]: new_name, 
                    headers[1]: new_pose,
                    headers[2]: new_size,
                    headers[3]: new_ears,
                    headers[4]: new_fur,

                    }
                rabbit.update(updated_rabbit)
                is_done = True
                print(f"You have successfully updated {breed_update}")
        if not is_done: 
            print(f"I'm sorry, {breed_update} was not found. ")

    elif user_action == '5':
        if rabbit:
            output = ', '.join(rabbit.keys()) + '\n'

            for rabbit in rabbits:
                output = output + ', '.join(rabbit.values()) + '\n'
            output = output.strip()
            out_filepath = 'rabbits.csv'
            with open(out_filepath, 'w', encoding='utf-8') as f:
                f.write(output)
                print("Your data has been saved. ")
        else:
            print("You have not made any changes. Nothing has been saved.")
        print("Goodbye. ")
        break
       
    elif user_action == '6':
        print("Goodbye")
        break

    else:
       print("The option you have chosen is invalid, please choose again. ")
