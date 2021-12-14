def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest :
            smallest = arr[i]
            smallest_index = i
    return smallest_index

# Now you can use this function to write selection sort:

def selectionSort(arr):
    sorted_array = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        sorted_array.append(arr.pop(smallest))
    return sorted_array

print(selectionSort([5, 3, 6, 2, 10]))