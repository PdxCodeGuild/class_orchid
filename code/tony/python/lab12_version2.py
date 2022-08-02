with open('code/tony/python/data/lab12_data.csv', 'r') as file:
    lines = file.read().split('\n')

# deserialize CSV (make a list of dicts)
headers = lines.pop(0).split(',')
data = [dict(zip(k,v)) for k,v in [[headers, line.split(',')] for line in lines]]

# loop until quit (input matches "q")
while True:
    # Build a UI presentable string from CSV field names
    choices = ', '.join([row.get('name') for row in data])
    entry = input('Operation [c,r,u,d,q]: ')
    if entry == 'c':
        # build a new record from CSV fields and user input
        record = dict(zip(headers,[input(f'{header}: ') for header in headers]))
        # require a unique value for name field
        while len([f for f in data if f['name'] == record.get('name')]):
            record.update({'name': input('Duplicate record. Enter a unique name:')})
        # add the record
        data.append(record)
    if entry == 'r':
        # presentable list for display
        print('\n'.join([', '.join([': '.join([k,v]) for k,v in list(row.items())]) for row in data]))
    if entry == 'u':
        sub_entry = input(f'Update [{choices}]: ')
        # collect values for each of the CSV field names
        record = dict(zip(headers,[input(f'{header}: ') for header in headers]))
        data = [f['name'] == sub_entry and f.update(record) or f for f in data]
    if entry == 'd':
        sub_entry = input(f'Delete [{choices}]: ')
        data = [f for f in data if sub_entry != f['name']]
    if entry == 'q':
        break
