file_path = 'code/rob/python/lab12/lab12.csv'

with open(file_path, 'r') as f:
    contents = f.read()

lines = contents.split('\n')

title_names = lines[0].split(',')
lines.pop(0)
list_of_dicts = []

for row in lines:
    i = 0
    items = row.split(',')
    dict_to_add = {}
    while i < len(title_names):
        dict_to_add.update({title_names[i]: items[i]})
        i += 1
    list_of_dicts.append(dict_to_add)

def create_entry():
    list_of_dicts.append({
        'name': input('Enter a name: '),
        'role': input('Enter a role: '),
        'type': input('Enter a type: '),
        'skins': input('Enter the number of skins: '),})

def read_entry():
    name = input('Enter a name to see their data: ')
    for dict in list_of_dicts:
        if dict['name'] == name:
            print(dict)

def update_entry():
    name = input('Enter a name: ')
    attribute = input('Enter an attribute to update: ')
    change = input('Enter the new value: ')
    for dict in list_of_dicts:
        if dict['name'] == name:
            dict.update({attribute: change})

def delete_entry():
    name = input('Enter a name to delete: ')
    for dict in list_of_dicts:
        if dict['name'] == name:
            list_of_dicts.remove(dict)

exit = ''
print('CSV info')
while exit != 'y':
    print('\nOptions: see all(1), create(2), read(3), update(4), delete(5).')
    option = input('Option: ')
    if option == '':
        break
    if not option.isnumeric():
        print('Not a valid option.\n')
    elif int(option) == 1:
        for item in list_of_dicts:
            print(item)
    elif int(option) == 2:
        create_entry()
    elif int(option) == 3:
        read_entry()
    elif int(option) == 4:
        update_entry()
    elif int(option) == 5:
        delete_entry()
    else:
        exit = input('Not an option, are you done? (y/n): ')

for item in list_of_dicts:
    print(item)

update_csv = ''
temp_keys = []
temp_values = []

for dict in list_of_dicts:
    temp_v = []
    for key, value in dict.items():
        if key not in temp_keys:
            temp_keys.append(key)
        temp_v.append(value)
    temp_values.append(temp_v)
for t in temp_keys:
    update_csv += t
    if t != temp_keys[-1]:
        update_csv += ','
    elif t == temp_keys[-1]:
            update_csv += '\n'
for value in temp_values:
    for item in value:
        update_csv += item
        if item != value[-1]:
            update_csv += ','
        elif item == value[-1]:
            update_csv += '\n'

print(update_csv)
# name,role,type,skins
# pele,jg,phys,9
# thana,jg,phys,12
# freya,carry,mag,7
# ymir,supp,mag,14
# chacc,solo,phys,8