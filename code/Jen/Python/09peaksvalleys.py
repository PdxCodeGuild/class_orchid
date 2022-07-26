
'''Jen Williams
PDX Code Guild Bootcamp
Class Orchid
lab 9: Peaks and Valleys'''

data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
peaks_list = []
valleys_list = []

def peaks(i, number, number_before, number_after):
    if number_before < number > number_after:
        return i
    else:
        i = 0
        return i
 


def valleys(i, number, number_before, number_after):
    if number_before > number < number_after:
        return i
    else:
        i = 0
        return i


def peaks_valleys(peaks_list, valleys_list):
    peaks_list.extend(valleys_list)
    peaks_list.sort()
    consolidated = peaks_list
    return consolidated


for i, number in enumerate(data):
    if i in range(1,19):
        #print(data)
        peak = peaks(i, number, data[i-1], data[i+1])
        if peak:
            peaks_list.append(i)
        
        valley = valleys(i, number, data [i-1], data[i+1])
        if valley:
            valleys_list.append(i)


print(f"Peaks = {peaks_list}")
print(f"Valleys = {valleys_list}")
print(f"Peaks and valleys = {peaks_valleys(peaks_list, valleys_list)}")