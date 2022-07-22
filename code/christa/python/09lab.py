###LAB 09: Peaks and Valleys 


#peaks(data) = [6, 14] | valleys(data) = [9, 17]  |  peaks_and_valleys(data) = [6, 9, 14, 17]

# 1. peaks - returns indices of peaks. A peak has a lower number on both the left and right
# x > y > z 

# 2. valley - returns indices of valleys. A valley is a number with a higher number on both the left and right
# x < y < z

# 3. peaks_and_valleys - uses the above two ****functions**** to compile a single list of the peaks and valleys
#       in order of appearance in the original data
#  Step three tells me I need to have two functions/ one each for step one and for step two...awesome...

shasta = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

#I named the mountain Shasta because it was the first that popped into my mind and sounded cooooler than data
###need to work on incorporating peaks and valleys combined lists outside of functions....
### used realpython.com for tutorial on enumerate vs range
#### used tutorialspoint.com for finding peak indices in a lists

def peak(shasta):          #define a function to find peaks of the Shasta list
    peaks = []             #create an open list for appended indices
    length = len(shasta)    #len of shasta for comparison in loop and conditionaal
    for i, pike in enumerate(shasta): # start a for loop to check each indice use enumerate instead of range to keep track of each index (I think)
        if i > 0 and i < length -1:  # check each indice in the list starting and ending with indices that have numbers both to the left and right 
            if shasta[i-1] < pike > shasta[i + 1]: # basically if both the numbers to the left and right of i are less than i than i is a peak
                peaks.append(i)                    #appends the peak to the peaks list
    return peaks                                   #this function SHOULD return the peaks list when called upon
#print(peak(shasta))

def valley(shasta):       #define a funciton to find valleys of the Shasta list
    valleys = []             #create an open list for appendices    
    length = len(shasta)         #len of shasta for comparison in loop and conditional
    for i, val in enumerate(shasta):   #start a loop to check each indice use enumerate to track the value of and place holder of the index.. 
        if i > 0 and i < length -1:    #checks each indice with a number to the left and right of it
            if shasta[i-1] > val < shasta[i+1]:  #if the value to the left and right of i are greater than i than i is a valley
                valleys.append(i)    #append indices for valleys to the valleys list
    return valleys                    #return the valleys list when this function is called upon
#print(valley(shasta))

peaks_and_valleys = (peak(shasta)) + (valley(shasta))   #combines the peaks and valleys lists created by the functions into one comprehensive list
peaks_and_valleys.sort()                                #sorts the list so the peaks and valleys are in order 
#print(peaks_and_valleys)

print(f'\nFor Mount Shasta, {shasta} the following locations in the data set are peaks and valleys.\n')
print(f'The indices for peaks in Shasta are {peak(shasta)} and the valleys are {valley(shasta)}.\n')  #print using f statement to tell the user what data they are looking at
print(f'The combined indices for peaks and valleys in Shasta are {peaks_and_valleys}.\n')