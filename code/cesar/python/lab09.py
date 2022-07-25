'''
Lab 09: Peaks and Valley
###############################
Define the following functions:
peaks - Returns the indices of peaks. A peak has a lower number on both the left and the right.
valleys - Returns the indices of 'valleys'. A valley is a number with a higher number on both the left and the right.
peaks_and_valleys - uses the above two functions to compile a single list of the peaks and valleys in order of appearance in the original data.
'''


data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

# print(len(data))
def peak(data):
    
    peaks_list = []

    for i, num in enumerate(data):
        if data[i -1] < data[i] and data[i + 1] < data[i]:
            peaks_list.append(data[i])
        
    return peaks_list

peak(data)
            
        

