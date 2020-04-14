# TO-DO: Complete the selection_sort() function below

arr = [4, 10, 3, 20, 31]


#      0  1  2  3   4   5  6

# it takes 1 index and loops through until it finds the lower index number.

def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        # range (start(0), stop(array length) - 1)
        current_index = i
        # getting index of i
        smallest_index = current_index
        # smallest index = current iterated index
        # first loops is where we select the current item in array
        print(arr)
        for j in range(i, len(arr)):
            # range stars at index and ends length of array
            # this loops actually changes the selection
            if arr[smallest_index] > arr[j]:
                smallest_index = j

        # TO-DO: swap

        arr[current_index], arr[smallest_index] = arr[smallest_index], arr[current_index]

    return arr


print(f'sort {selection_sort(arr)}')

# TO-DO:  implement the Bubble Sort function below

bubble_arr = [23, 3, 1, 52, 21]


def bubble_sort(arr):
    # resets the swap loop function every time it passes through
    swaps = True
    while swaps:
        swaps = False
        for i in range(0, len(arr) - 1):
            if arr[i] > arr[i + 1]:
                # swap
                # temp = arrays index
                temp = arr[i]
                # array index now = array index + 1 (aka the next index)
                arr[i] = arr[i + 1]
                # the next index becomes the temp
                arr[i + 1] = temp
                swaps = True

    return arr


print(f'bubble {bubble_sort(bubble_arr)}')


# STRETCH: implement the Count Sort function below

def count_sort(arr, maximum=-1):

    return arr
