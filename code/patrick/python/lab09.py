data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
def peaks(data):
    peak_2 = []
    for i in range(1, len(data) -1):
        if data[i] > data[i-1] and data[i] > data[i+1]: 
            #peak_2 = []
            #print(data[i])
            peak_2.append(i)
            
    return peak_2    
            

peaks(data)




def valleys(data):
    valley_2 = []
    for i in range(1, len(data) -1):
        if data[i] < data[i-1] and data[i] < data[i+1]: 
            
            
            valley_2.append(i)
    return valley_2
            
            
valleys(data)


def peaks_and_valleys(data):
    peak_and_valley = []
    
        
    peak_and_valley.extend(valleys(data))
    peak_and_valley.extend(peaks(data))
    peak_and_valley.sort()
    return peak_and_valley



print(peaks_and_valleys(data))



