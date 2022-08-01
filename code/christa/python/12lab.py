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

# Line 0 are the headers, or keys for each dictionary
lines = contents.split('\n')
headers = lines[0]
key_s = headers.split(',')
row_lines = lines[1:]
values = row_lines.split(',')

cities = []





"""
Create
Retrieve
Update
Delete

Read
Evaluate
Print
Loop
"""





#Rows 1 through the end are the data. Each row will be a dictonary
#Empty list to append dictionaries to

