filepath = 'code/pete/python/examples/data/cities.csv'

with open(filepath, 'r') as f:
    contents = f.read()
# print(contents)
lines = contents.split('\n')
# print(lines)
# lines is a list of the lines in the csv
# the first item in lines has the headers
# these will be the keys in each dictionary
# the other lines will be the values
headers = lines[0] # the first line in the csv has the headers/keys
print(headers, type(headers))
headers = headers.split(',')
print(headers, type(headers)) # this is now a list of the keys for the dictionary

# your goal in part 1 of contacts list
# is to turn the string from the csv
# into a list of dictionaries like this:
countries = [
    {
        'name': 'portland',
        'country': 'US',
        'cuisine': 'everything',
        'climate': 'temperate',
        'language': 'english',
    },
    {
        'name': 'kansas city',
        'country': 'US',
        'cuisine': 'bbq',
        'climate': 'temperate',
        'language': 'english',
    },
    # ... then the other dictionaries for each citiy
]
