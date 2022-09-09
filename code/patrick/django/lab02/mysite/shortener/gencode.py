import random
import string
def gen():
    letters = string.ascii_letters
 
    

    digits =  string.digits

    all_characters = letters  + digits

    password = ""
    counter = 0
    while counter < 6:
        random_char = random.choice(all_characters)
        password = password + random_char    
        counter = counter + 1
    return password

print(gen())
    

#password = import.random(all_characters)

