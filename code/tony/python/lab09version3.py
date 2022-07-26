# test data
data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

def peaks_and_valleys(data):
    """return indices of peaks and valleys"""
    ret = []
    for i, val in enumerate(data):
        if i <= 1 or i+1 >= len(data): continue # skip first and last values
        if data[i-1] < val > data[i+1] or data[i-1] > val < data[i+1]:
            ret.append(i)
    return ret

liquid = 0 # running total of liquid
prev = 0 # previous loop value for comparison
for i in peaks_and_valleys(data):
    if data[i] < prev:
        w = prev - data[i]
        liquid += w * w # assume triangle symmetry
    prev = data[i]

print(f'{liquid} units of liquid in valleys')