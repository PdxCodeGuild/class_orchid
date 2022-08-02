from string import punctuation
from random import random, choice

# reading a file

# the first argument is the file path to the text file to be read
# the second argument is the mode of opening the file ('r' for read mode)
# the encoding kwarg (keyword argument) may need to be set to 'utf-8'
in_filepath = '1 Python/examples/data/fire-and-ice.txt'
with open(in_filepath, 'r', encoding='utf-8') as f:
    contents = f.read()

# print(contents) # the text of the poem

# splitting the text of the poem on new lines
lines = contents.split('\n')

# print(lines) # a list the lines of the poem as strings

phrases = ['fr fr', 'no cap', 'and thats strait bussin']

remove_punctuation_dictionary = str.maketrans('', '', punctuation + '’')
print(remove_punctuation_dictionary)
for i, line in enumerate(lines):
    line = line.lower()
    line = line.translate(remove_punctuation_dictionary)
    if random() < 0.333: # one third chance of this happening
        line += ' ' + choice(phrases)
    # end each loop iteration by changing the list
    lines[i] = line

# for i in range(len(lines)):
#     lines[i] = lines[i].lower().translate(remove_punctuation_dictionary)

print(lines)

output_content = '\n'.join(lines)
out_filepath = '1 Python/examples/data/fire-and-ice-fr-fr.txt'
with open(out_filepath, 'w', encoding='utf-8') as f:
    f.write(output_content)