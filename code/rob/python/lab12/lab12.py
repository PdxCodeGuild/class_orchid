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
    
    while i < len(items):
        dict_to_add.update({title_names[i]: items[i]})
        i += 1
    list_of_dicts.append(dict_to_add)

def create_entry():
    name = input('Enter a name: ')
    for dict in list_of_dicts:
        if name == dict['name']:
            while name == dict['name']:
                name = input('Name exist, please enter another name: ')
                
    list_of_dicts.append({
        'name': name,
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

def get_key_values():
    for dict in list_of_dicts:
        temp_v = []
        for key, value in dict.items():
            if key not in temp_keys:
                temp_keys.append(key)
            temp_v.append(value)
        temp_values.append(temp_v)
def keys_to_csv(csv):
    for t in temp_keys:
        csv += t
        if t != temp_keys[-1]:
            csv += ','
        elif t == temp_keys[-1]:
                csv += '\n'
    return csv
def values_to_csv(csv):
    for value in temp_values:
        for item in value:
            csv += item
            if item != value[-1]:
                csv += ','
            elif item == value[-1]:
                if value != temp_values[-1]:
                    csv += '\n'
    return csv

get_key_values()
update_csv = keys_to_csv(update_csv)
update_csv = values_to_csv(update_csv)

with open(file_path, 'w') as f:
    f.write(update_csv)

# name,role,type,skins
# pele,jg,phys,9
# thana,jg,phys,12
# freya,carry,mag,7
# ymir,supp,mag,14
# chacc,solo,phys,8