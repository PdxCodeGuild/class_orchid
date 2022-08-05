# I am sorry this list comprehension looks like gobbledygook,
# but I was just so excited to challenge myself to make a tiny CRUD+REPL.
# Hey, it works!

# data path
csv_path = 'code/tony/python/data/lab12_data.csv'

with open(csv_path, 'r') as file:
    lines = file.read().split('\n')

# deserialize CSV (make a list of dicts)
headers = lines.pop(0).split(',')
data = [dict(zip(k,v)) for k,v in [[headers, line.split(',')] for line in lines]]

# loop until quit (input matches "q")
while True:
    # Build a UI presentable string from CSV field names
    choices = ', '.join(['"' + row.get('name').replace(r'\x2c',',') + '"' for row in data])
    entry = input('Operation [c,r,u,d,q]: ')
    if entry == 'c':
        # build a new record from CSV fields and user input
        record = dict(zip(headers,[input(f'{header}: ').replace(',',r'\x2c') for header in headers]))
        # require a unique value for name field
        while len([f for f in data if f['name'] == record.get('name')]):
            record.update({'name': input('Duplicate record. Enter a unique name:')})
        # add the record
        data.append(record)
    if entry == 'r':
        # presentable list for display
        print('\n'.join([', '.join([': '.join([k,'"' + v.replace(r'\x2c',',') + '"']) for k,v in list(row.items())]) for row in data]))
    if entry == 'u':
        sub_entry = input(f'Update [{choices}]: ')
        # collect values for each of the CSV field names
        record = dict(zip(headers,[input(f'{header}: ').replace(',',r'\x2c') for header in headers]))
        data = [f['name'] == sub_entry and f.update(record) or f for f in data]
    if entry == 'd':
        sub_entry = input(f'Delete [{choices}]: ').replace(',',r'\x2c')
        data = [f for f in data if sub_entry != f['name']]
    if entry == 'q':
        break

# serialize dict (builds string as CSV from list of dicts)
with open(csv_path, 'w') as file:
    file.write(','.join(headers) + '\n' + '\n'.join([','.join(list(f.values())) for f in data]))