import math


with open('book.txt', 'r') as book:
    contents = book.read()
    # print(contents)



# create variable characters:words:sentences


# taking sentences directly from file using certain punctuation to find end of sentence
number_of_sentences = 0
for x in contents:
    if x in['.','?','!']:
        number_of_sentences += 1
print(number_of_sentences)



# same thing as number_of_sentences but searching for spaces instead
number_of_words = 0 
for x in contents:
    if x in [' ']:
        number_of_words += 1
print(number_of_words)




number_of_characters = 0
for x in contents:
    number_of_characters += len(x)
print(number_of_characters)




# 4.71*(char/words)+0.5*(word/sentences)-21.43 = ARI
# using math.ceil to round up
ARI = 4.71 * (number_of_characters/number_of_words)+0.5*(number_of_words/number_of_sentences)-21.43
ARI_final = math.ceil(ARI)

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


# This is me printing the data in the sentences using f strings
grade_level = ari_scale[ARI_final]
print(f'The ARI for {book.name} is {ARI_final} ')
print(f'This corresponds to a {grade_level["grade_level"]} level of difficulty.')
print(f'That is suitable for an average person {grade_level["ages"]} years old\n')






