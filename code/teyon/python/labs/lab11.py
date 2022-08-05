#print out the welcome message 
print("\nWelcome to the ARI Scale Calculator")

#add the file to the python code and set it to read to extract the information we are looking for
with open('../data/theclouds.txt', 'r') as the_clouds_file:
    #converting the txt file into variable contents to be used throughtout the code
    contents = the_clouds_file.read()


#get the amount of characters by placing the contents of the book in the length function
characters = len(contents)

#identifying a sentence by counting the amount of periods, questions marks and exclamation marks 
#in the docucment which identify when a sentence has ended
period = '.'
question_mark = '?'
exclamation = '!'

#created a variable of zero to later keep a running count of the sentences counted
sentences = 0
#for loop that checks the document for '.', '?', '!' 
for character in contents:
    if character == period or character == question_mark or character == exclamation:
        #running counter that updates each iteration that one of the above characters are found
        sentences += 1

#created a words variable of zero, will be used later to give a running counter of words
words = 0
#here we replace all \n with spaces because there will be escape characters
#after we split the contents of the book into a list, but we cant split a list
#so we eliminate all escape characters before we split the spaces.
content_words = contents.replace('\n', ' ')

#split the content into a list removing all spaces, but taking each word a making
#it an item in a list
split_content = content_words.split(' ')

#After we split the list there we still some empty spaces left that we being counted as items 
#in the list, so we run a while loop that states that while there are empty spaces in the list
#we will remove them one at a time and continue looping until all are gone 
while '' in split_content:
    split_content.remove('')

#now that all words have become items in a list and we have removed all empty spaces from the 
#list as items, we will use a for loop to count each word every iteration through
for word in split_content:
    #each iteration a word(list item) is counted it will be added to the running 
    #counter for words
    words += 1


#dictionary that holds the ARI scale
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

#formula that calculates the ARI scale
ari = 4.71 * (characters / words) + 0.5 * (words / sentences) - 21.43

#use the round function to round up the float into an integer. 
# This will be the number that corresponds the specific dictionary in the ari_scale
ari_score = round(ari)

#Takes the dictionary inside the ari dictionary the corresponds to the ARI score
#and isolates the ages key in that dictionary to produce the given value
ari_ages = ari_scale[ari_score]['ages']
#Takes the dictionary inside the ari dictionary the corresponds to the ARI score
#and isolates the grade level key in that dictionary to produce the given value
ari_grade_level = ari_scale[ari_score]['grade_level']

#print statement the reports the ari scale number, age and grade level based on the ARI calculation
print(f"""\nThe ARI score for the selected title is {ari_score}.
This corresponds to a {ari_grade_level} level of difficulty
that is suitable for an average person {ari_ages} years old.
""")