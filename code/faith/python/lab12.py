with open('contacts.csv', 'r') as file:
    lines = file.read().split('\n')
# print(lines)

# splitting list into a list of lists
split_list = []
for line in lines:
    split_list.append(line.split(','))

# print(split_list)

keys = split_list[0]
# print(keys)


contact_list = []
for value in split_list[1:]:
    contact_list.append(dict(zip(keys,value)))

print(contact_list)

# version 1 complete


















# people = {}




# people = {}
# for line in lines:
   
#     # print(linelist)



# people =[
#     {'name': 'bob', 'favorite food': 'apple'},
#     {'name': 'samantha','favorite food': 'pizza'},
#     {'name': 'lilly','favorite food': 'meatloaf'},
#     {'name': 'david','favorite food': 'ribs'},
# ]

