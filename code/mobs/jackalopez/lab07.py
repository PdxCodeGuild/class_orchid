jackalopes = [ 2, 10, ]

def one_year(): #adds 1 year to life
    for index,age in enumerate(jackalopes):
        jackalopes[index] = age +1
        
def prune():
    for index,age in enumerate(jackalopes):
        if age >= 10:
            jackalopes.pop(index)


one_year()
prune()


print(jackalopes)    

