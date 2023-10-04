def selection_sort(arr):
    size = len(arr)
    for i in range(size):
        min = i
        for j in range(i + 1, size):
            if arr[j] < arr[min]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]


if __name__ == '__main__':
    elements = [5,9,2,1,67,34,88,34]
    print("Given array : " )
    print(elements)
    selection_sort(elements)
    print("Sorted array : " )
    print(elements)
