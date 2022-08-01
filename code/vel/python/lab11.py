import string

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

with open('the_raven/the_raven.txt', 'r') as f:
    raven = f.read()

# get number of words
raven_2 = raven

raven_2 = raven_2.split()

num_words = len(raven_2) # find a way to strip empty space and punc

# get number of characters

replaced_raven = raven.replace(" ", "")

num_characters = len(replaced_raven)

# get number of sentences

sentences = 0

for char in raven:
    if char == '.':
        sentences += 1
    elif char == '!':
        sentences += 1
    elif char == '?':
        sentences += 1

ari = int(4.71*(num_characters/num_words) + 0.5 * (num_words/sentences) - 21.43)

print(f"""The ARI for the book The Raven is {ari}
This corresponds to a {ari_scale[ari]['grade_level']} of difficulty
that is suitable for an average person {ari_scale[ari]['ages']} years old.
""")





