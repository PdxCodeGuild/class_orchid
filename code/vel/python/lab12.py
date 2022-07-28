"""
Lab 12: Contact list
"""
filepath = 'chiefs/chiefs_goats.csv'

with open(filepath, 'r') as f:
    contents = f.read()
print(contents)