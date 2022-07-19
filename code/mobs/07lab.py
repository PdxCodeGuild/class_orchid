##Version 1 Jack-o-lope

# 1 gestational pair = 2 offspring per year / cycles every +2 to population every four years// 
# 2 die every 10 years



population = 2

#yr_1 through yr_3 nothing happens for first pair

time = 0
years = []
birth_rate = [ ('group_0'), 
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

print(growth(2, 2))
print(population)
print(time)
#for _ range(5):
#    
# 
# population * (1 + 100%) ** time

#breeding age formula added for population at year five 
"""
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