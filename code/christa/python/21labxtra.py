# Extra Lab 21: Count Words

import string

with open('romance_of_lust.txt', 'r', encoding='utf-8') as book:
    little = book.read().lower()

translator = str.maketrans('', '', string.punctuation)
book_without_punc = little.translate(translator)
word_list = book_without_punc.split(" ")

#turn list into a dictionary with words as keys and counts as values
word_dict ={}
word_count = 0

#words are keys count are values
for i, word in enumerate(word_list):
    #if i in word_list:   #got an error here 
        word_count +=1
        word_dict[i] = word_count
    #else:
        word_dict[i]= 1


words = list(word_dict.items())  # .items() returns a list of tuples
words.sort(key=lambda tup: tup[1], reverse=True)  #sort largest to smallest, based on count
for i in range(min(10, len(words))):
    print(words[i])

print(words[i])




