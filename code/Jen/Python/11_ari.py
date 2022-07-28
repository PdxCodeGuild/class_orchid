'''Jen Williams
PDX Code Guild Bootcamp - Orchid
lab 11: ARI - Made up option'''


import string
import math

file = open('underground.txt') 
document = file.read()
file.close()


#count the sentences
document = document.replace('!', '.')
document = document.replace('?', '.')
document_sentences = document.split('.')
sentences = len(document_sentences)
#print(document_sentences)
#print(sentences)
#print(document)

#Strip the punctuation

translator = str.maketrans('', '', string.punctuation)
no_punct = document.translate(translator)


#print(no_punct)


#count the characters
character_list = []
for char in document:
    char = char.lower()
    character_list.append(char)
characters = len(character_list)
#print(characters)


#count the words
document_words = document.split()
words = len(document_words)
#print(words)

#calculate the score
score = 4.71 * (characters/words) + .5 * (words/sentences) - 21.43
score = math.ceil(score)
#print(score)


#provide the scale
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

#find the score on the scale and print
print(f"The ARI for the selected text is {score}.  This corresponds to a {ari_scale.get(score)['grade_level']} reading level of difficulty that is suitable for an average person {ari_scale.get(score)['ages']} years old.")

