with open("data/sence.txt", "r") as f:
    contents = f.read()

#print(contents)

characters = 0
for char in contents:
    characters += 1 

print("total characrers:   ", characters)    

#lines = list(contents)

#print(lines)
Total_words = len(contents.split())
print('Total words:   ', Total_words)
total_sentences = contents.count('.')

print('total sentences:    ', total_sentences)

ari = 4.71*(characters // Total_words) + 0.5 * (Total_words // total_sentences) - 21.43

rounded_ari = round(ari)
#print(ari)
print(rounded_ari)


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

print("the ari for sence.txt is ", rounded_ari )
print("this corresponds to an", ari_scale[rounded_ari]["grade_level"],"level of difficulty" )
print("this is suitable for an average person  ", ari_scale[rounded_ari]["ages"], "years old" )
