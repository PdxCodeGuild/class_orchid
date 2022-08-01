from random import shuffle
"""
Access element from list: mylist[i]
Given the list of seasons, print out 'summer'
"""
seasons = ['spring', 'summer', 'fall', 'winter']
print(seasons[1])

"""
Access element from nested lists: mylist[i][j]
Given the 2D list of seasons, print out 'july'
"""
spring = ['march', 'april', 'may']
summer = ['june', 'july', 'august']
fall = ['september', 'october', 'november']
winter = ['december', 'january', 'febuary']

seasons2d = [spring, summer, fall, winter]
print(seasons2d[1])
print(seasons2d[1][1]) # july
print(seasons2d[1][1][0]) # j (the j in july)

"""
Assignment mylist[i] = value
In the list seasons, change 'fall' to 'autumn'
"""
seasons[2] = 'autumn'
print(seasons)

"""
Assignment to nested lists
Fix the 'febuary' typo in winter THROUGH seasons2d
"""
# winter = seasons2d[3]
# winter[2] = 'february'
seasons2d[3][2] = 'february'
print(seasons2d)

"""
Loops
Loop over seasons to print out each season
"""
seasons = ['spring', 'summer', 'autumn', 'winter']
for season in seasons:
    print(season)

"""
Loop over seasons to print out each season using range() and len()
"""
print(seasons) # ['spring', 'summer', 'autumn', 'winter']
print(len(seasons)) # 4
print(range(len(seasons))) # range(0, 4) # essentially the list: [0, 1, 2, 3]
for i in range(len(seasons)):
    print(seasons[i])

"""
Nested Loops
Loop over seasons2d AND the nested lists to print out each month
"""
for season in seasons2d:
    # print(season)
    for month in season:
        print(month)

"""
Using range() and len(), loop over seasons2d to print out each month
"""
for i in range(len(seasons2d)):
    season = seasons2d[i]
    # print(seasons2d[i])
    for j in range(len(season)):
        month = season[j]
        print(month)

for i in range(len(seasons2d)):
    for j in range(len(seasons2d[i])):
        print(seasons2d[i][j])

"""
Inclusion: element in mylist
Append: mylist.append(element)
Use in and append to makes sure all the items_to_add are in grocery_list just once
"""
grocery_list = ['apples', 'bananas', 'oranges']
items_to_add = ['bananas', 'blueberries', 'oranges', 'strawberries']
for item in items_to_add:
    if item not in grocery_list:
        grocery_list.append(item)
print(grocery_list)

"""
Insert: mylist.insert(index, element)
Add mangos to the top of the list
"""
grocery_list = ['apples', 'bananas', 'oranges']
grocery_list.insert(0, 'mangos')
print(grocery_list)

"""
Remove: mylist.remove(element)
Remove bananas from the list with .remove()
"""
grocery_list = ['apples', 'bananas', 'oranges']
grocery_list.remove('bananas')


"""
Pop: mylist.pop(index)
Using .pop(), remove brocolli from fruits and add it to vegetables
"""
fruits = ['apples', 'oranges', 'brocolli', 'cherries']
vegetables = ['potatoes', 'radishes', 'celery']
item = fruits.pop(2)
print(item) # brocolli
vegetables.append(item)
print(fruits, vegetables)

"""
Index: mylist.index(element)
Remove oranges from the randomized list with .pop()
"""
grocery_list = ['apples', 'bananas', 'oranges']
shuffle(grocery_list)  # grocery_list is now randomly shuffled
print(grocery_list)
oranges_index = grocery_list.index('oranges')
print(oranges_index)
grocery_list.pop(oranges_index)
print(grocery_list)
# super slick one-liner 😎
# grocery_list.pop(grocery_list.index('bananas'))
# print(grocery_list)


"""
Remove all the mangos from too_many_mangos
"""
too_many_mangos = ['apples', 'mangos', 'bananas', 'mangos',
                   'blueberries', 'mangos', 'oranges', 'mangos', 'mangos']
while 'mangos' in too_many_mangos:
    too_many_mangos.remove('mangos')
print(too_many_mangos)

"""
Slicing mylist[start:end:step]
Use slicing to print out a list of the programming langagues
"""

languages = ['Python', 'JavaScript', 'Japanese', 'English', 'Arabic', 'Greek', 'Hindi']
print(languages[0:2])
print(languages[:2]) # the first value can be omitted if starting at 0

languages = ['Chinese', 'Spanish', 'Arabic', 'Python', 'JavaScript', 'C#', 'Java']
print(languages[3:7])
print(languages[3:]) # the second value can be omitted if going to the end of the list

languages = ['English', 'Thai', 'French', 'German', 'Rust', 'C', 'Go', 'Assembly', 'COBOL', 'Icelandic', 'Italian']
print(languages[4:9])

languages = ['JavaScript', 'English', 'French', 'Rust', 'Norwegian', 'Danish', 'Python']
print(languages[::3])


languages = ['Swahili', 'Go', 'Afrikaans', 'Java', 'Romansh', 'GDScript', 'Quechua']
print(languages[1::2])
# print(languages[::]) # copy of original list
# print(languages[::1]) # copy of original list

"""
Use slicing to print out a list of the course sections in the order we will be covering them
"""
languages_frameworks_engines_etc = ['Unity', 'Angular', 'French', 'Django Rest Framework', 'Russian', 'Lua', 'Vue', 'Pascal', 'Godot', 'JavaScript', 'Korean', 'PHP', 'Django', 'Perl', 'Dutch', 'CSS', 'Express', 'HLSL', 'HTML', 'Unreal Engine', 'Dothraki', 'Flask', 'Elvish', 'Doggo-Speak', 'Python', 'High Valyrian', 'Morse Code', 'C++']

# print(languages_frameworks_engines_etc[::-1]) # gives you the list reversed
print(languages_frameworks_engines_etc[-4::]) # will start at python (you can use - numbers to access starting from the back of the list)
print(languages_frameworks_engines_etc[-4:2:-3])
print(languages_frameworks_engines_etc[::3])

# hey!  we want all the words through moon and nothing else
# you don't know where 'moon' is in this list
words = ['horse', 'bed', 'night', 'moon', 'key', 'telephone']
index_of_moon = words.index('moon')
new_words = words[:index_of_moon + 1]
print(new_words)