data = [1, 2, 3, 4,	5, 6, 7, 6, 5, 4, 5, 6,	7, 8, 9, 8,	7, 6, 7, 8,	9]

def peaks(data_param):
    peak = []
    for i in range(1, len(data_param)-1):
        if data_param[i-1] < data_param[i] and data_param[i+1] < data_param[i]:
            peak.append(i)
    return peak

peaks_list = peaks(data)
#print(peaks_list)

def valleys(data_param):
    valleys = []
    for i in range(1, len(data_param)-1):
        if data_param[i-1] > data_param[i] and data_param[i+1] > data_param[i]:
            valleys.append(i)
    return valleys

valleys_list = valleys(data)
#print(valleys_list)

result = peaks_list + valleys_list
result.sort()
print(result)