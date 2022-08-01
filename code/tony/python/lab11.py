import sys, os, math

basedir = f'{sys.path[0]}/data/lab11books'
filepaths = os.path.exists(basedir) and os.listdir(basedir)
if not filepaths:
    print('Book files missing! Try this first:\n  git checkout tony/python/lab11\nThen come back and try again. Exiting.')
    exit(1)

print('')
for lineno, filepath in enumerate(filepaths):
    lineno = str(lineno).rjust(2, ' ')
    print(f'[{lineno}] {filepath}')

user_input = ''
while not user_input == 'q' and not user_input in [str(s) for s in range(len(filepaths))]:
    user_input = input('\nChoose a book [number], or quit [q]: ')

if user_input == 'q': quit()

filepath = filepaths[int(user_input)]

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

def get_ari(filepath):
    with open(filepath, 'r') as myfile:
        book_str = myfile.read()
    num_chars = len(book_str.replace(' ', ''))
    num_words = len(book_str.split(' '))
    num_sentences = 1
    for ch in book_str:
        if '.' == ch: num_sentences += 1
    num_sentences = len(book_str.split('.'))  # + len(book_str.split('!')) + len(book_str.split('?'))
    # print(f'chars: {num_chars}\nwords: {num_words}\nsentences: {num_sentences}')
    return num_chars / num_words * 4.71 + num_words / num_sentences * 0.5 - 21.43

def print_ari(ari_score):
    ari_score = ari_score <= 14 and ari_score or 14
    ari = ari_scale.get(ari_score)
    if not ari: return
    print(f"""
{'-' * 56}

The ARI for {filepath} is {ari_score}
This corresponds to a {ari.get('grade_level')} level of difficulty
that is suitable for an average person {ari.get('ages')} years old.

{'-' * 56}
""")

print_ari(math.ceil(get_ari(f'{basedir}/{filepath}')))
