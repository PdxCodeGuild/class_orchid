'''
Lab 09: Peaks and Valley
###############################
Define the following functions:
peaks - Returns the indices of peaks. A peak has a lower number on both the left and the right.
valleys - Returns the indices of 'valleys'. A valley is a number with a higher number on both the left and the right.
peaks_and_valleys - uses the above two functions to compile a single list of the peaks and valleys in order of appearance in the original data.
'''

data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

"""
def peaks function takes in a parameter data. using for loop to pull out the index, number value. 
To check on the bountries of the list I used an if to check for i that is greater than 0 and less than the len -1 
which is the last index in the list. 

I then checked to see if num was greater than data[i-1] (value to the left) and less greater than data[i+1] (value to the right).
append to empty list the i = index. The reverse was done with valleys. 
"""
def peak(data):
    peaks_list = []
    for i, num in enumerate(data):
        if 0 < i  < (len(data) - 1) and data[i -1] < num > data[i + 1]:
            peaks_list.append(i)
    return peaks_list
    

def valleys(data):
    valleys_list = []
    for i, num in enumerate(data):
        if 0 < i < (len(data) - 1) and data[i - 1] > num < data[i + 1]:
            valleys_list.append(i)
    return valleys_list


def peaks_and_valleys(data):
    peaks_and_valleys_list = peak(data) + valleys(data)
    peaks_and_valleys_list.sort()
    return peaks_and_valleys_list


print(f'The peaks in index are: {peak(data)}')
print(f'The valleys in index are: {valleys(data)}')
print(f'Both the peaks and valleys are: {peaks_and_valleys(data)}')
    
    