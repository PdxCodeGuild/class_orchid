#created a variable called file path which is the data we want to read
filepath = '../data/contacts.csv'

#make the data in the file readable
with open(filepath, 'r') as f:
    contents = f.read()


#creates a list of the lines
lines = contents.split('\n')


#creates headers as the first line
header = lines[0]
#created an individual list of the header
header = header.split(',')

#blank list which will hold the list of contacts without the header
list_of_contacts = []

#the final list that will hold the dictionaries we will create later
list_of_dicts = []

#list of contacts without header 
contacts = lines[1:]

#for loop that is saying for each lines in all the lines of contacts
for contact in contacts:
    #we want to take the line we are iterating through and turn it into a list
    contact = contact.split(",")
    #we want to append the blank list of contacts with each new list created every iteration
    list_of_contacts.append(contact)

#for loop that iterates through every new list we created and appended to the list of contacts   
for list in list_of_contacts:
    #empty dictionary that will hold each contact with header
    dict = {}
    #
    
    for i,thing in enumerate(list):
        #dict[header[i]] translates too (dict = header index 0 which is name)
        #which translates too (name = thing in index 0).
        dict[header[i]] = thing
    #list of dicts appends with every newly created dictionary callec dict, this is done at the same level
    #as the for loop because we only want to append it after each item in the list has been updated into the 
    #newly created dictionary and not every iteration through.
    list_of_dicts.append(dict)
#print the list of dictionaries
print(list_of_dicts)




