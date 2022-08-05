with open('yellow/the-yellow-wallpaper.txt', 'r', encoding='utf-8') as f:
    yellow_wallpaper = f.read()

yellow_wallpaper_split = yellow_wallpaper.split()

number_words = len(yellow_wallpaper_split)

#getting the number of words from the split version of yellow wallpaper
number_words_replaced = yellow_wallpaper.replace(" ","")
# found information on pythonexamples.org
#print(number_words_replaced)

number_of_characters = len(number_words_replaced)
#using len() to grab the number of characters from the replaced version of number of words
print(number_of_characters)

sentences = 0

for character in yellow_wallpaper:
    if character == '.':
        sentences += 1
    elif character == '?':
        sentences += 1
    elif character == '!':
        sentences += 1

ari_math = int(4.71 * (number_of_characters/number_words) + 0.5 * (number_words/sentences)-21.43)

ari_ages_key = 'ages'

ari_grade_key = 'grade_level'
#how to get one value out of nested dictionaries
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

print(f'\nThe ARI for yellow_wallpaper.txt is {ari_math} \nThis corresponds to a {ari_scale[ari_math][ari_grade_key]} Grade level of difficulty \nthat is suitable for an average person {ari_scale[ari_math][ari_ages_key]} years old.')

#i went to w3 schools and geeks for geeks for references