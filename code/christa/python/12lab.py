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
    contents = f.readlines()

# Line 0 are the headers, or keys for each dictionary
"""lines = contents.split('\n')
headers = lines[0]
key_s = headers.split(',')"""
contents = [row_lines[:-1] for row_lines in contents]
sheet = [row_lines.split(',') for row_lines in contents]
cities = []
#sheet = lines[:-1]

for row_lines in sheet[1:]:
    poker_run = {}
    for i, place in enumerate(row_lines):
        poker_run[sheet[0][i]]= place
    cities.append(poker_run)

print(cities)

#Rows 1 through the end are the data. Each row will be a dictonary
#Empty list to append dictionaries to




    



#print(rows)
#dictionaries are each row 1:12
#keys in the dictionaries are row 0 or columns...

