jackalopes = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            
def one_year(index,age): #adds 1 year
    jackalopes[index] = age + 1

def prune(index,age): #removes the old
    if age >= 10:
        jackalopes.pop(index)

def birth(birthing_age,age): #finds population capable of birth
    if age in range(4,9):
        return birthing_age + 1 
    else:
        return birthing_age

birthing_age = 0

# while len(jackalopes) <= 1000:
for index,age in enumerate(jackalopes):
    one_year(index,age)
    prune(index,age)
    birthing_age = birth(birthing_age,age)


# print(birthing_age)


print(jackalopes)    

