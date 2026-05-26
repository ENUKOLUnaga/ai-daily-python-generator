def bubble_sort(arr):
    # get the length of the array
    n = len(arr)
    
    # repeat the process until the array is sorted
    for i in range(n):
        # create a flag that will allow the function to terminate early if there's nothing left to sort
        swapped = False
        
        # start looking at each item of the list one by one, comparing it with its adjacent value
        for j in range(n - i - 1):
            # if we find an element that is greater than the next element in the list
            if arr[j] > arr[j + 1]:
                # swap them
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                # set the flag to True so we'll loop again
                swapped = True
        
        # if no two elements were swapped by inner loop, the list is sorted
        if not swapped:
            break

    # return the sorted array
    return arr

# test the function
arr = [64, 34, 25, 12, 22, 11, 90]
print("Original array:", arr)
print("Sorted array:", bubble_sort(arr))