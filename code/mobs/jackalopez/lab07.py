import math

jackalopes = [ 0, 0]
            
def one_year(index,age): #adds 1 year
    jackalopes[index] = age + 1

def birth(birthing_age,age): #finds population capable of birth
    age += 1
    if age in range(4,9):
        return birthing_age + 1 
    else:
        return birthing_age

birthing_age = 0
new_pop = 1
year = 1

while len(jackalopes) <= 1000: #population loop
    birthing_age = 0
    new_pop = 1
    for index,age in enumerate(jackalopes): #finds population capable of birth
        one_year(index,age)
        birthing_age = birth(birthing_age,age)

    while 10 in jackalopes: #removes all at age 10
        for index,age in enumerate(jackalopes):
            if age >= 10:
                jackalopes.pop(index)

    while new_pop <= birthing_age: #adds new population to end of list
        jackalopes.append(0)
        new_pop += 1

    year += 1


print(year)