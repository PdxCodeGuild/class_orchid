

with open('lab12_contacts_test.csv', 'r') as file:
    lines = file.read().split('\n')
    print(lines)

print(type(lines))