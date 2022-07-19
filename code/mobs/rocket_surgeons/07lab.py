##Version 1 Jack-o-lope

# 1 gestational pair = 2 offspring per year / cycles every +2 to population every four years// 
# 2 die every 10 years

"""

population = 2

#yr_1 through yr_3 nothing happens for first pair

time = 0
years = {

    #'born': 0
    #'died' : 0
   # 'population' : 2

}

births = {
    'age 0' = 
    'age 1' =
    'age_2' =
    'age_3' =
}



if years == range(1, 4):

elif years == range(4, 9):
    run formula for 2 babies each year

elif years == range(9-11):
    run formula for exponential babies, start elderly

elif years == 10:
    start death, exponential babies, elderly

elif years > 12:
    run fomula for death, exponential babies, exponential elderly


age = [ ('group_0'), 
    ('group_2')
]

offspring =[]

def growth(time, population):
    offspring = []
    for _ in range (5):
        population = population * (1 + 1) **(time) #how do you write a formula w/o pissing off python?
        time += 1
        years.append(time)
        offspring.append(population)

    return offspring

print(growth(time, population))
print(population)
print(time)
#for _ range(5):
#    
# 
# population * (1 + 100%) ** time

#breeding age formula added for population at year five 

while population < 1000:
    run the growth function
    run the death function
    run growth - death for total pop
    append.variable(Time)

def alive
= alive - dead


t = how many cycles of growth """

"""
final_value = initial_amount *(1+rate of growth) **time

growth rate = 100% = 100
initial_amount = 2
final_value = 1000

add 4 on the end | how long these two will take to make 1000 babies


"""
"""
pop_by_age = [0,0,0,0,2] #don't forget the first 3 years
total_pop = sum(pop_by_age)
 #still need to work deaths in
for age in pop_by_age:
    # enumerate function can recall index and value
    # need to be able to recall breeding age animals and add them together
    
    print(age)
    
"""

#nonbreeding_pop =
#breeding_pop = 

#.insert

# The goal is to calculate how many years it will take for two age 0 jackalopes to create a population of 1000.

# - Jackalopes are reproductive from ages 4-8 and die at age 10.
# - Gestation is instantaneous. Each gestation produces two offspring.
# - Jackalopes are hermaphrodites, it takes a pair to reproduce, but any pair will do

# With these conditions in mind, we can represent our population as a list of ints.


jackalopes = [0, 0]

# population = len(jackalopes)

# the jackalopes get older
# enumerate is a helper function that you can use to run a for loop
# and have access to the the index (i) of the element as well as the element itself (jackalope)

years = 0
while len(jackalopes) <= 1000:
    years += 1
    for i, jackalope in enumerate(jackalopes):
        # print(i, jackalope)
        # jackalopes[i] == jackalope # True
        if jackalope >= 4 and jackalope <= 8:
            jackalopes.append(0)
        jackalopes[i] += 1
    while 10 in jackalopes:
        jackalopes.remove(10)
    print(len(jackalopes))
print(years)