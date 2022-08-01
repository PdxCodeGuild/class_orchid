# reading a file

# the first argument is the file path to the text file to be read
# the second argument is the mode of opening the file ('r' for read mode)
# the encoding kwarg (keyword argument) may need to be set to 'utf-8'
with open('data/fire-and-ice.txt', 'r', encoding='utf-8') as f:
    contents = f.read()

print(contents) # the text of the poem

# splitting the text of the poem on new lines
lines = contents.split('\n')


print(lines) # a list the lines of the poem as strings