import random
#created a dictionary in order to store the cconversions
converter = {
    'ft' : 3.6576,
    }

#i labeled the input info which is the place where user will type in the number
info = input('please enter the number of feet: ')
#i then turned the string into an interger in order to be able to us is to convert from ft to meters.
info = int(info)

print(f"{info} ft when converted to meters gives you {info * converter['ft']} m.")
#i cited my programming_102 lab for the math conversion