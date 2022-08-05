"""
Lab 12: Contact list
"""

"""
now that headers are removed, lets match the data to the headers by index
"""

filepath = 'chiefs/chiefs_goats.csv'

with open(filepath, 'r') as f:
    contents = f.read()
    
lines = contents.split("\n")

headers_line = lines[0].split(',')
chiefs = []
for line in lines[1:]:
    add = {}
    line = line.split(',')
    """zip function pairs the first iterator item together with the second iterator item (ex QB: Patrick Mahomes)"""
    chiefs.append(dict(zip(headers_line, line))) 


# headers_list = headers_line.split(',')
# position_key = headers_list[0]
# name_key = headers_list[1]
# num_key = headers_list[2]
# nickname_key = headers_list[3]

# for index in range(1,len(lines)):
#     data ={}
#     line = lines[index].split(',')
#     data[position_key] = line[0]
#     data[name_key] = line[1]
#     data[num_key] = line[2]
#     data[nickname_key] = line[3]
#     chiefs.append(data)
# def add_to_player_dict(data):
#     chiefs = []
#     for i in range(len(data)):
#         player_dict = {}
#         player_info = data[i].split(',') 
#         for i,key in enumerate(headers_list):
#             player_dict[key] = player_info[i] 
#         chiefs.append(player_dict)
#     return chiefs

options = '''
Please select from the following actions:
    1. Retrieve the list
    2. Add a player to the list
    3. Remove a player from the list
    4. Update a player on the list
    5. Quit
'''

while True:
    """Im trying to get a print all conditional if the user wants to print the list to check for all of the players"""
    user_input = input(options) 
    if user_input == '1':
        search = False
        retrieved_player = input('Which player are you looking for? If unsure type "All": ').title()
        if retrieved_player == 'All':
            search = True
            print(chiefs)
        else:
            for player in chiefs:
                if retrieved_player == player['Name']:
                    search = True
                    print(player)
        if not search:
            print(f'{retrieved_player} is not a Chiefs GOAT')
        
    elif user_input == '2':
        players_dict = {}
        new_player_po = input("\nWho should we add? Let's start with abbreviated position:  ").upper()
        players_dict['Position'] = new_player_po
        
        new_player_name = input("Players name? ").title()
        players_dict['Name'] = new_player_name

        new_player_number = input("Players number? ")
        players_dict['Number'] = new_player_number
        
        new_player_nickname = input("Players nickname if he has one! ").title()
        if new_player_nickname == "":
            players_dict['Nickname'] = '-'
        else:
            players_dict['Nickname'] = new_player_nickname
        
        chiefs.append(players_dict)
        
        print(f"\nYou just added \nPosition: {new_player_po}, Name: {new_player_name}, Number: {new_player_number}, Nickname: {new_player_nickname}.")
        
    elif user_input == '3':
        search = False
        remove_player = input('Which player do you want to remove? ').title()
        for player in chiefs:
            if remove_player == player['Name']:
                search = True
                chiefs.remove(player)
                print(f'Successfully removed {remove_player}')
        if not search:
            print(f'{remove_player} is not a Chiefs GOAT')
    
    elif user_input == '4':
        player_change = input('What player should we change? (Ex. Patrick Mahomes): ').title()
        for player in chiefs:
            if player_change == player['Name']:

                change_key = input('What should we change? (Ex. Number): ').title()
                change_value = input('What are we changing it to? ').title()
                player[change_key] = change_value 

        print(f"Succesfully changed '{player_change}' to '{change_value}'")
    
    elif user_input == '5':
        print("\nGoodbye")
        break
    else:
        print("\nThat is not a valid entry")


with open('chiefs/chiefs_goat2.csv','w') as f:
    
    f.write(', '.join(headers_line))
    for index in range(len(chiefs)):
        f.write('\n')
        f.write(f', '.join(chiefs[index].values()))
        

