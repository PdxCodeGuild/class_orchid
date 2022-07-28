import math

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

with open('code/rob/python/lab11/lab11.txt', 'r') as f:
    content = f.read()

words = content.split()
word_count = float(0)
sentence_count = float(0)
char_count = float(0)
for word in words:
    word_count += 1
    char_count += len(word)
    if '.' in word or '!' in word or '?' in word:
        sentence_count += 1

ARI = math.ceil(((4.71*(char_count / word_count)) + (0.5*(word_count / sentence_count))) - 21.43)

print('----------------------------------------------------------------------------')
print(f'\nThe ARI for \'Relativity : the Special and General Theory\' is {ARI}.')
print(f"This corresonds to a {ari_scale[ARI]['grade_level']} level of difficulty")
print(f"that is suitable for an average person {ari_scale[ARI]['ages']} years old.\n")
print('----------------------------------------------------------------------------')
