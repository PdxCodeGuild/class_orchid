import string
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

characters = string.ascii_letters + '=+-_)(*&^%$#@"\',<>~`;:[]/{\}'

sentence_ends = '?!.'

file_path = 'Around_The_World_In_80_Days.txt'

with open(file_path, 'r', encoding='utf-8') as c:
    content = c.read()

'''
Letter Counter
Word Counter
Sentence Counter
'''

def letter_count():
    '''counts every no space and non punctuation'''
    letter_c = 0
    for x in content:
        if x in characters:
            letter_c += 1
        else:
            letter_c += 0
    return letter_c

def word_count():
    '''seperates every word into data in a list, returns the length of the list for word count'''
    word = ''
    word_list = []
    for x in content:
        if x in characters:
            word += x
        elif x == ' ':
            word_list.append(word)
            word = ''
        elif x in sentence_ends:
            word_list.append(word)
            word = ''
        else:
            word += ''
    word_c = len(word_list)
    return word_c
        
def sentence_count():
    '''seperates sentences into data in a list, returns length of sentence list'''
    sentence = ''
    sentence_list = []
    for x in content:
        if x in characters or x == ' ':
            sentence += x
        elif x in sentence_ends:
            sentence_list.append(sentence)
            sentence = ''
        else:
            sentence += ''
    sentence_c = len(sentence_list)
    return sentence_c

def ari(characters, words, sentences):
    '''calculates the ARI score of a text file'''
    ari_scale = math.ceil(((characters / words) * 4.71) + ((words / sentences) * 0.5) - 21.43)
    print(ari_scale)
    return ari_scale

def main():
    sentences = sentence_count()
    words = word_count()
    character = letter_count()
    print(sentences)
    print(words)
    print(character)
    ari_score = ari(character, words, sentences)

    print(f'''--------------------------------------------------------

    The ARI for {file_path} is {ari_score}
    This corresponds to a {ari_scale[ari_score]['grade_level']} Grade level of difficulty
    that is suitable for an average person {ari_scale[ari_score]['ages']} years old.
    
    --------------------------------------------------------''')

main()