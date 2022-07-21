
'''Jen Williams
PDX Code Guild Bootcamp
Class Orchid
lab 9: Peaks and Valleys'''

data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
peaks = []
valleys = []


for index in range(1,20):
    number_before = data[index-1]
    number_after = data[index+1]
    if number_before < data[index] > number_after:
        peaks.append(index)
    elif number_before > data[index] < number_after:  
        valleys.append(index)


print(f"Peaks = {peaks}")
print(f"Valleys = {valleys}")
peaks.extend(valleys)
peaks.sort()
print(f"Peaks and valleys = {peaks}")
        




