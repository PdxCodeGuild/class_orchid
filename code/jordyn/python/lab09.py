def valley(reverse, index, forward):
    '''Records a valley index'''
    if reverse > index and forward > index:
        return True
    else:
        return False

def peaks(reverse, index, forward):
    '''Records a peak index'''
    if reverse < index and forward < index:
        return True
    else:
        return False

def peaks_and_valleys():
    '''Records peak and valley index in order of appearance'''
    ordered_pv = {}
    order = 0 #easier access to above dictionary
    index = 0 #Skipping first index because it cannot be a peak or valley data point

    while index <= len(peaks_valleys) - 2:
        p_v_index = peaks_valleys[index]
        if index == 0:
            p_v_index_reverse = peaks_valleys[index] - 1
        else:
            p_v_index_reverse = peaks_valleys[index - 1]
        if index == len(peaks_valleys):
            p_v_index_forward = peaks_valleys[index] +1
        else:
            p_v_index_forward = peaks_valleys[index +1]
        is_peak = peaks(p_v_index_reverse, p_v_index, p_v_index_forward)
        is_valley = valley(p_v_index_reverse, p_v_index, p_v_index_forward)
        if is_peak == True:
            order += 1
            ordered_pv[order] = f"Peak Index: {index}, Height of: {peaks_valleys[index]}."
        if is_valley == True:
            order += 1
            ordered_pv[order] = f"Valley Index: {index}, Depth of: {peaks_valleys[index]}."
        index += 1
    return ordered_pv

def create_display():
    '''Creates a displayable Dictionary'''
    row = 9
    while row >= 1:
        row_list = []
        for value in peaks_valleys:
            if value < row:
                row_list.append(' ')
            else:
                row_list.append('x')

        display_case[row] = row_list
        row -= 1
    return display_case

def water_sim(water_display):
    '''fills valleys with water'''
    index = 0
    peak_row = []
    peak_column = []

    while index <= len(peaks_valleys) - 2:
        p_v_index = peaks_valleys[index]
        if index == 0:
            p_v_index_reverse = peaks_valleys[index] - 1
        else:
            p_v_index_reverse = peaks_valleys[index - 1]
        if index == len(peaks_valleys):
            p_v_index_forward = peaks_valleys[index] +1
        else:
            p_v_index_forward = peaks_valleys[index +1]
        peaks_only = peaks(p_v_index_reverse, p_v_index, p_v_index_forward)
        if peaks_only:
            peak_row.append(peaks_valleys[index])
            peak_column.append(index)
        index += 1
    water_display = peak_to_peaks(peak_row, peak_column, water_display)

def peak_to_peaks(peaks_row, peaks_column, water_display):
    '''Boolean check for empty space between peaks, nesting function to then fill'''
    index = 0
    print("water display\n")
    while index < len(peaks_row):
        row = peaks_row[index]
        column = peaks_column[index]
        step_down = column + 1
        discover_column = step_down
        while discover_column < len(peaks_valleys) and row > 0:
            if water_display[row][discover_column] == ' ':
                discover_column += 1
                continue
            else:
                valley_fill(row, step_down, water_display)
                row -= 1
                step_down += 1
                discover_column = step_down + 1
        index += 1

def valley_fill(row, column, water_display):
    '''Fills empty spaces in discovered open columns'''
    while water_display[row][column] != 'x':
        if water_display[row][column] == ' ':
            water_display[row][column] = 'o'
        column += 1

peaks_valleys = [5, 4, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9] #Plus and Minus 1 ordered list to create peak and valley info
display_case = {} #Declaring a dictionary
peaks_valleys_index = []
p_v_indexed = peaks_and_valleys() #Callable variable with ordered peak and valley information
display_case = create_display() #Creates visual data

for x in display_case:
    print(display_case[x])
for x in p_v_indexed:
    print(p_v_indexed[x])
water_display = display_case
water_sim(water_display)
for x in water_display:
    print(water_display[x])
