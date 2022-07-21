"""
Lab 09: Peaks and Valleys
"""
data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

def find_peaks():
    peaks = []
    for i in range(1, len(data)-1): # range(start, stop, step) start = 1
        if data[i -1] < data[i] and data[i + 1] < data[i]:
            peaks.append(data[i])
    return peaks

#IndexError index out of range

def find_valleys():
    valleys = []
    for i in range(1, len(data)-1):
        if data[i -1] > data[i] and data[i + 1] > data[i]:
            valleys.append(data[i])
    return valleys

def peaks_valleys():
    peaks_and_valleys = []
    peaks_and_valleys.extend(find_valleys()) # function object is not iterable, '()' makes that function iterable.
    peaks_and_valleys.extend(find_peaks())
    peaks_and_valleys.sort()
    return peaks_and_valleys

print(peaks_valleys())





# print(type(find_valleys()))

# print(type(find_valleys))
