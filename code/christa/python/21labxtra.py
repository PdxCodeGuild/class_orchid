# Extra Lab 21: Count Words
import string
"""with open('romance_of_lust.txt', 'r', encoding='utf-8') as book:
    little = book.read()"""

little = "all good boys go to heaven"

little = little.lower()
translator = str.maketrans('', '', string.punctuation)
book_without_punc = little.translate(translator)
word_list = book_without_punc.split(" ")

#turn list into a dictionary with words as keys and counts as values
word_dict ={}
word_count = 0

#words are keys count are values
for i, word in enumerate(word_list):
    if i in word_list:   #got an error here 
        word_count +=1
        word_dict[i] = word_count
    else:
        word_dict[i]= 1

STOPWORDS = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 
'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 
'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 
'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 
'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 
'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 
'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 
'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 
'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 
'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 
'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 
'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', 
"haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 
'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]

no_stop_words = [word for word in word_dict if word not in STOPWORDS()]

words = list(no_stop_words.items())  # .items() returns a list of tuples
words.sort(key=lambda tup: tup[1], reverse=True)  #sort largest to smallest, based on count
for i in range(min(10, len(words))):
    print(words[i])




print(words[i])




