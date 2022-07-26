"""
Lab 09: Peaks and Valleys
"""
data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

def find_peaks():
    peaks = []
    for i in range(1, len(data)-1): # range(start, stop, step) start = 1
        if data[i -1] < data[i] and data[i + 1] < data[i]:
            peaks.append(i)
    return peaks

#IndexError index out of range

def find_valleys():
    valleys = []
    for i in range(1, len(data)-1):
        if data[i -1] > data[i] and data[i + 1] > data[i]:
            valleys.append(i)
    return valleys

def peaks_valleys(lst):
    peaks = find_peaks()
    valleys = find_valleys()
    peaks.extend(valleys)
    peaks.sort()
    return peaks

print(f'peaks > {find_peaks()}')

print(f'\nvalleys >{find_valleys()}\n')

print(f'peaks and valleys >{peaks_valleys(data)}\n')





# print(type(find_valleys()))

# print(type(find_valleys))
