# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    arrA_index = 0
    arrB_index = 0
    index = 0
    while arrA_index < len(arrA) and arrB_index < len(arrB):
        if arrA[arrA_index] < arrB[arrB_index]:
            merged_arr[index] = arrA[arrA_index]
            index += 1
            arrA_index += 1
        else:
            merged_arr[index] = arrB[arrB_index]
            index += 1
            arrB_index += 1

    while arrA_index < len(arrA):
        merged_arr[index] = arrA[arrA_index]
        index += 1
        arrA_index += 1

    while arrB_index < len(arrB):
        merged_arr[index] = arrB[arrB_index]
        index += 1
        arrB_index += 1

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively


def merge_sort(arr):
    # Your code here
    start = 0
    end = len(arr)
    if end > start + 1:
        mid = int((start + end) / 2)
        # print(arr[0:mid], arr[mid:end], start, mid, end)
        arrA = merge_sort(arr[0:mid])
        arrB = merge_sort(arr[mid:end])
        arr = merge(arrA, arrB)
    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists
# or data structures; it can only re-use the memory it was given as input


def merge_in_place(arr, start, mid, end):
    # Your code here
    pass


def merge_sort_in_place(arr, l, r):
    # Your code here
    pass
