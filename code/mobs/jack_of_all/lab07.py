"""
Lab 07: Jackalope Simulator -- Mob
"""

jackalopes = [0,0]
population = 0
year = 0

while population <= 1000:
    population = len(jackalopes)

    #increase by 1
    for index, jack in enumerate(jackalopes):
        mate_check = index + 1
        jackalopes[index] += 1
    #check if age >= 4 and <= 8
        if jack >= 4 and jack <= 8 and (index % 2) == 0:
            jackalopes.extend([0,0])
        
    while 10 in jackalopes:
        for index, jack in enumerate(jackalopes):
            if jack == 10:
                jackalopes.pop(index)
    
        

    year += 1
    print('year: ', year,'population: ', population)
    # print(jackalopes)
