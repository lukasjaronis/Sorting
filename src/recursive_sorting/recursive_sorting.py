# TO-DO: complete the helpe function below to merge 2 sorted arrays

ar1 = [2, 3, 20, 9, 8, 1]
ar2 = [3, 2, 21, 76, 4, 5]


def merge(sort_left, sort_right):
    elements = len(sort_left) + len(sort_right)
    merged_arr = [0] * elements  # creates a new array of values 0 with the length of left and right
    # TO-DO
    i = 0
    j = 0
    k = 0

    while i < len(sort_left) and j < len(sort_right):
        if sort_left[i] < sort_right[j]:
            merged_arr[k] = sort_left[i]
            i = i + 1
            k = k + 1
        else:
            merged_arr[k] = sort_right[j]
            j = j + 1
            k = k + 1
    while i < len(sort_left):
        merged_arr[k] = sort_left[i]
        i = i + 1
        k = k + 1
    while j < len(sort_right):
        merged_arr[k] = sort_right[j]
        j = j + 1
        k = k + 1
    return merged_arr


print(merge(ar1, ar2))


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # TO-DO
    if len(arr) < 2:
        return arr

    half = len(arr) // 2
    print(half)
    left = arr[:half]
    right = arr[half:]

    sort_left = merge_sort(left)
    sort_right = merge_sort(right)

    return merge(sort_left, sort_right)


print(merge_sort([32, 2, 6, 4, 3, 10]))


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    return arr
