'''Jen Williams
PDX Code Guild Bootcamp - Orchid
lab 11: ARI'''

import string

underground = """

Because part of the joy of creating a piece of art is in knowing that
many people can - and are - enjoying it. Particularly people who can't
otherwise afford to pay $11 USD for a book. People such as cash strapped
hackers. This book is about them, their lives and obsessions. It rubs
clear a small circle in the frosted glass so the reader can peer into
that hazy world. `Underground' belongs on the Net, in their ephemeral
landscape.

The critics have been good to `Underground', for which I am very
grateful. But the best praise came from two of the hackers detailed in
the book. Surprising praise, because while the text is free of the
narrative moralising that plague other works, the selection of material
is often very personal and evokes mixed sympathies. One of the hackers,
Anthrax dropped by my office to say `Hi'. Out of the blue, he said with
a note of amazement, `When I read those chapters, it was so real, as if
you had been right there inside my head'. Not long after Par, half a
world away, and with a real tone of bewildered incredulity in his voice
made exactly the same observation. For a writer, it just doesn't get any
better than that.

"""
#Make sure the sentences are correct



#count the sentences
underground.replace('!', '.')
underground.replace('?', '.')

underground_sentences = underground.split('. ')
sentences = len(underground_sentences)
#print(underground_sentences)
#print(sentences)


#strip the punctuation
no_punct = underground.strip(string.punctuation)


#count the characters
character_list = []
for char in underground:
    char = char.lower()
    character_list.append(char)
characters = len(character_list)
#print(characters)


#count the words
underground_words = underground.split()
words = len(underground_words)
#print(words)

#calculate the score
score = 4.71 * (characters/words) + .5 * (words/sentences) - 21.43
score = round(score)
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
print(f"The ARI for the selected paragraph in chapter one of Suelette Dreyfus's 'Underground' is {score}.  This corresponds to a {ari_scale.get(score)['grade_level']} reading level of difficulty that is suitable for an average person {ari_scale.get(score)['ages']} years old.")
