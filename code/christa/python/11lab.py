# Lab 11: Compute Automated Readability Index
#open, encode, read, and rename book
with open('war_and_peace.txt', 'r', encoding= 'utf_8') as book_file:
   book = book_file.read()
#print(wp)

#def ari(wp):   
characters = (len(book))
#print(characters)

sentences = len(book.splitlines())
#print(sentences)

book_words = book.split(" ")
words = []
word_count = 0
for i, word in enumerate(book_words):
    words.append(i)
    word_count += 1
#print(word_count)

ari = (4.71 * (characters/word_count)) + (0.5 * (word_count/sentences)) - 21.43
ari = round(ari)
#need to round ari up to nearest int 
#print(ari)

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

ari_score = ari
reading_level = ari_scale[ari]['ages']
age_appropriate = ari_scale[ari]['grade_level']

print(f'\n The ARI for war_and_peace.txt is {ari_score}.')
print(f'\n This corresponds to a {reading_level} level of difficulty.')
print(f'\n The book is suitable for an average person {age_appropriate} years old.\n')