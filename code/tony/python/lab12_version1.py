with open('code/tony/python/data/lab12_data.csv', 'r') as file:
    lines = file.read().split('\n')
    print(lines)

headers = lines.pop(0).split(',')
data = [dict(zip(k,v)) for k,v in [[headers, line.split(',')] for line in lines]]

print()
for datum in data:
    for header in headers:
        print(f'{header}: {datum[header]}')
    print()