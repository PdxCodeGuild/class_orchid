import math
import string
from unicodedata import name


ari_scale = {
     1: {'ages':   '5-6', 'grade_level': 'Kindergarten'},
     2: {'ages':   '6-7', 'grade_level':    '1st Grade'},
     3: {'ages':   '7-8', 'grade_level':    '2nd Grade'},
     4: {'ages':   '8-9', 'grade_level':    '3rd Grade'},
     5: {'ages':  '9-10', 'grade_level':    '4th Grade'},
     6: {'ages': '10-11', 'grade_level':    '5th Grade'},
     7: {'ages': '11-12', 'grade_level':    '6th Grade'},
     8: {'ages': '12-13', 'grade_level':    '7th Grade'},
     9: {'ages': '13-14', 'grade_level':    '8th Grade'},
    10: {'ages': '14-15', 'grade_level':    '9th Grade'},
    11: {'ages': '15-16', 'grade_level':   '10th Grade'},
    12: {'ages': '16-17', 'grade_level':   '11th Grade'},
    13: {'ages': '17-18', 'grade_level':   '12th Grade'},
    14: {'ages': '18-22', 'grade_level':      'College'}
}

with open('thinketh.txt', 'r') as f:
    contents = f.read()
    words = contents.split()
    

sentence_counter = 0  
for sentence in contents:
    if sentence in ('.', '?', '!'):
        sentence_counter  += 1
print (sentence_counter)

word_counter = len(words)

print(word_counter)

char_counter = 0

for char in contents:
    if char in string.ascii_letters:
        char_counter += 1

print(char_counter)

ari = float(4.71*(char_counter/word_counter)+0.5*(word_counter/sentence_counter)-21.43)

round_up = math.ceil(ari)

ari_values = ari_scale.get(round_up)

grade = ari_scale[round_up]['grade_level']
ages = ari_scale[round_up]['ages']

print (f'''

{'*'*40}

The ARI for ______.txt is {round_up}.

This correesponds to a {grade} level of diffifulty.

This means that it is suitable for an "average" person who is {ages} years old.

{'*'*40}
''')