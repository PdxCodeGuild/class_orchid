# Lab 12: Contact List
# csv file is a data table with rows and columns

# 1. Build a CSV ('comma separated values') 
# 2. Open the CSV, 
# 3. Convert the lines of text into a list of dictionaries 
# 4. one dictionary for each row. 
# 5. The text in the header represents the keys, 
# 6. The text in the other lines represent the values.

filepath = 'code/christa/python/cities.csv'

with open(filepath, 'r') as f:
    contents = f.read()

lines = contents.split('\n')
columns = lines[0]
columns = columns.split(',')

rows = contents.splitlines('\n')
print(rows)

cities = []




#print(columns)