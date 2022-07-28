import sys, os, math, string

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

with open(f'{basedir}/{filepath}', 'r') as myfile:
    book_str = myfile.read()

book_str = book_str.translate(str.maketrans('—-', '  '))
book_str = book_str.translate(str.maketrans('', '', string.punctuation + '“’‘”'))
book_str = book_str.lower()
book_list = book_str.split()

stopwords = [
    'i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 
    "youre", "youve", "youll", "youd", 'your', 'yours', 'yourself', 'yourselves', 
    'he', 'him', 'his', 'himself', 'she', "shes", 'her', 'hers', 'herself', 'it', 
    "its", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 
    'which', 'who', 'whom', 'this', 'that', "thatll", 'these', 'those', 'am', 'is', 
    'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 
    'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 
    'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 
    'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 
    'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 
    'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 
    'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 
    'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "dont", 'should', 
    "shouldve", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "arent", 
    'couldn', "couldnt", 'didn', "didnt", 'doesn', "doesnt", 'hadn', "hadnt", 'hasn', 
    "hasnt", 'haven', "havent", 'isn', "isnt", 'ma', 'mightn', "mightnt", 'mustn', "mustnt", 
    'needn', "neednt", 'shan', "shant", 'shouldn', "shouldnt", 'wasn', "wasnt", 'weren', 
    "werent", 'won', "wont", 'wouldn', "wouldnt"
]

book_dict = {}
for word in book_list:
    if not word in stopwords:
        book_dict[word] = book_dict.get(word) and book_dict[word] + 1 or 1

words = list(book_dict.items()) # .items() returns a list of tuples
words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
    print(words[i])