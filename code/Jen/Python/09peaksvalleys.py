"""

Define the following functions:

    peaks - Returns the indices of peaks. A peak has a lower number on both the left and the right.

    valleys - Returns the indices of 'valleys'. A valley is a number with a higher number on both the left and the right.

    peaks_and_valleys - uses the above two functions to compile a single list of the peaks and valleys in order of appearance in the original data.


>>> data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
>>> peaks(data)
[6, 14]
>>> valleys(data)
[9, 17]
>>> peaks_and_valleys(data)
[6, 9, 14, 17]

"""

"""


data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

compare number to previous index this is a function with parameters
    if the number is higher, see if the next number is higher
        continue that until it is no longer true
            that is the peak
                add it to the peak list

compare number to the previous index this is a function with parameters
    if the number is lower, see if the next number is lower
        continue that until it is no longer true
            that is the valley
                add it to the valley list

maybe extend to combine peaks and valleys lists                

"""
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

# right numbers, need to stop them from adding so many times.


print(f"Peaks = {peaks}")
print(f"Valleys = {valleys}")
peaks.extend(valleys)
peaks.sort()
print(f"Peaks and valleys = {peaks}")
        




