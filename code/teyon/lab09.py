#list of numbers used to determine peaks and valleys
list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]


#function defined as peaks which determines which numbers in the list are peaks 
def peaks(list_of_numbers):

    #blank peak list which will hold the peak values 
    peak_list = []
    #Saying for indices in the range of the length of the list. Range views the function as 0-20
    #and len views the list as 21 items, so by adding -1 the length and the range both view
    #the list up too 20.
    for i in range(len(list_of_numbers)-1):
        #if index is not equal too 0, than we want to review both the left and right side of the
        #index. index 0 does not have a left side so we dont want it to go to the end of the list
        if i != 0:
            
            #variables that hold each index and the number to the left and right of the index
            #as the for loop iterates through, as long as the index is not 0 it will hold each 
            #of these numbers to determine if the middle number is highter than the left and right.
            middle_number = list_of_numbers[i]
            right_number = list_of_numbers[i + 1]
            left_number = list_of_numbers[i - 1]
            #if statement that checks if the left and right numbers are lower than the middle number[i]
            #if so [i](index) will be appended to the blank peak_list
            if left_number < middle_number > right_number:
                peak_list.append(i)
    #returns the peak_list     
    return peak_list
        

#function defined as valleys which determines which numbers in the list are valleys
def valleys(list_of_numbers):
    
    #blank valley_list which will hold the valleys values 
    valley_list= []
    #Saying for indices in the range of the length of the list. Range views the function as 0-20
    #and len views the list as 21 items, so by adding -1 the length and the range both view
    #the list up too 20.
    for i in range(len(list_of_numbers)-1):
        #if index is not equal too 0, than we want to review both the left and right side of the
        #index. index 0 does not have a left side so we dont want it to go to the end of the list
        if i != 0:
            #variables that hold each index and the number to the left and right of the index
            #as the for loop iterates through, as long as the index is not 0 it will hold each 
            #of these numbers to determine if the middle number is highter than the left and right.
            middle_number = list_of_numbers[i]
            right_number = list_of_numbers[i + 1]
            left_number = list_of_numbers[i - 1]
            #if statement that checks if the left and right numbers are lower than the middle number[i]
            #if so [i](index) will be appended to the blank valley_list
            if left_number > middle_number < right_number:
                valley_list.append(i)
           
    return valley_list
    # print(f"Valleys:{valley_list}")

#function that will combine both the peak_list and valley_list into one list
def peaks_and_valleys(peak_list, valley_list):
    ##list called peaks and valleys list that will pass in two list parameters and combine the two
    peaks_and_valleys_list = peak_list + valley_list
    #sorts the list after we have combined them
    peaks_and_valleys_list.sort()
    #returns the peaks and valleys list
    return peaks_and_valleys_list

#variable that holds the results value contained in the peaks function
peak_list = peaks(list_of_numbers)

#variable that holds the results of the valleys function
valley_list = valleys(list_of_numbers)

#variable that holds the results value of the peaks and vallets function
peaks_and_valleys_list = peaks_and_valleys(peak_list, valley_list)


#print peaks
print(f"Peaks:{peak_list}")

#print valleys
print(f"Valleys:{valley_list}")



#print both peaks and valleys
print(f"Peaks and Valleys:{peaks_and_valleys_list}")




