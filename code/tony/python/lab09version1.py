# test data
data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

def peaks(data):
    """return the peak indices"""
    ret = []
    for i, val in enumerate(data):
        if i > 1 and i+1 < len(data) and data[i-1] < val > data[i+1]: # greater than adjacent values
            ret.append(i)
    return ret

def valleys(data):
    """return the valley indices"""
    ret = []
    for i, val in enumerate(data):
        if i > 1 and i+1 < len(data) and data[i-1] > val < data[i+1]: # lesser than adjacent values
            ret.append(i)
    return ret

def peaks_and_valleys(data):
    """return sorted indices of peaks and valleys"""
    ret = peaks(data) + valleys(data)
    ret.sort()
    return ret

# demonstrate the functions and print the results
print(f'\
peaks(data) = {peaks(data)}\n\
valleys(data) = {valleys(data)}\n\
peaks_and_valleys(data) = {peaks_and_valleys(data)}\
')