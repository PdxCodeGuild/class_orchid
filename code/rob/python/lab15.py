import math
#part 1
def linear_search(nums, value):
    if value in nums:
        return nums.index(value)
    else:
        return 'not found'

print('linear search: ', linear_search([1,2,3,4,5,6,7,8], 5))

#part 2
def binary_search(nums, nums_len, value):
    nums.sort()
    low = nums[0]
    high = nums[-1]
    while low <= high:
        mid = math.floor((low + high) / 2)
        if nums[mid] < value:
            low = mid + 1
        elif nums[mid] > value:
            high = mid - 1
        else:
            return nums[mid]
    return 'unsuccessful'

binary = [1,8,9,5,4,3,6,7,2]

print('binary search: ', binary_search(binary, len(binary), 2))

#part 3
def bubble_sort(A: list):
    n = len(A)
    
    while True:
        swapped = False
        for i in range(1, n):
            if A[i - 1] > A[i]:
                current = A[i]
                prev = A[i - 1]
                A[i] = prev
                A[i - 1] = current
                swapped = True
        if not swapped:
            break
    print('bubble sort: ', A)

bubble_sort([1,9,7,8,6,3,5,4,2])

#part 4
def insertion_sort(A: list):
    i = 1
    while i < len(A):
        j = i
        while j > 0 and A[j - 1] > A[j]:
            current = A[j]
            prev = A[j - 1]
            A[j] = prev
            A[j - 1] = current
            j -= 1
        i += 1
    print('insertion sort: ', A)

insertion_sort([1,9,8,2,4,3,7,5,6])

#part 5
def quicksort_recursive(A, low, high):
    if low < high:
        p = partition(A, low, high)
        quicksort_recursive(A, low, p)
        quicksort_recursive(A, p + 1, high)

def partition(A, low, high):
    pivot = A[low + (high - low) // 2]
    i = low
    j = high
    while True:
        while A[i] < pivot:
            i += 1
        while A[j] > pivot:
            j -= 1
        if i >= j:
            return j
        a_i = A[i]
        a_j = A[j]
        A[i] = a_j
        A[j] = a_i

def quicksort(A):
    quicksort_recursive(A, 0, len(A) - 1)
    print(A)

quicksort([5,1,3,9,8,7,2])